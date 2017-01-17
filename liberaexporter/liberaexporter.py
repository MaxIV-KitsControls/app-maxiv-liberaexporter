"""
Prometheus exporter which sends Libera platform metrics to prometheus server.
The prometheus server,however needs to be configured to poll it, e.g. "<hostname>:9110
"""

from prometheus_client import start_http_server, Gauge
import pylibera
import time
import config
#from config import gauges_temp_raf_list
#import psutil

#host="127.0.0.1"

def gather_data(period=1):
    """
    The main loop that publishes metrics forever
    """

    #initiate raf node depending on raf boards
    #for raf in ["raf3","raf4","raf5"]:
    #    for tupl in config.gauges_temp_raf_list:
    #        tupl[2]=tupl[2].format(raf)

    #Create Dict Metrics
    # raf_metrics = dict((name, Gauge("libera_{0}".format(name), desc))
    #     #Later on we can have labels according to each raf module i.e [raf3,ra4,raf5]
    #     for name, desc in config.gauges_temp_raf_list
    # )


    #Create a dict type {node,Gauge} (node for each raf board)
    raf_metrics = dict((node.format(raf), Gauge("libera_raf{0}_{1}".format(raf, name), desc))

        for name, desc, node in config.gauges_temp_raf_list
            for raf in ["3"]#,"4","5"] #TODO get raf list automatically
    )

    # #Create Utilities info for metrics
    # raf_utilities = dict((name, node.format(raf))
    #     #Later on we can have labels according to each raf module i.e [raf3,ra4,raf5]
    #     for name in config.gauges_temp_raf_list 
    #         for raf in ["raf3","raf4","raf5"]
    # )
    
    #print raf_metrics
    while True:

        try:
            for node,metric in raf_metrics.items():
                #print node
                metric.set(platform.GetValue(node))
        except:
            print('Exception at metric {0}'.format(node))

        #While delay
        time.sleep(period)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9110)
    #create the pylibera object
    platform = pylibera.PyLiberaClient("127.0.0.1", "platform")
    # Gather metrics
    gather_data(10)