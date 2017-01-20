"""
Prometheus exporter which sends Libera platform metrics to prometheus server.
The prometheus server,however needs to be configured to poll it, e.g. "<hostname>:9110
"""
from prometheus_client import start_http_server, Gauge
import time, sys
import pylibera
import commands
import config #Configuration file with the metric information 

def check_platformd():
    """
    Simple function checks if platform service is running and return 1 (For running) and 0 (Not running)
    Used to set the platformd metric value
    """
    output = commands.getoutput('ps -A')
    if 'libera-platform' not in output:
        print("Platform is not running!")
        return 0
    else:
        return 1


def gather_data(period=1):
    """
    Function which inits the metrics and runs the main loop that publishes metrics forever
    """
    # INIT, prepare metric lists to be able to be used by Prometheus
    
    #create the pylibera object
    platform = pylibera.PyLiberaClient(root_type="platform")

    #Create a Gauge metric which monitors the platform service
    platformd_metric = Gauge("platformd_service_status", "Metric to monitor platform service")
    #Set initial value
    platformd_metric.set(check_platformd())

    #Create a dict type {node,Gauge} (node for each raf board)
    raf_metrics = dict((node.format(raf), Gauge("libera_raf{0}_{1}".format(raf, name), desc))
        #Assign each raf board No to each raf board
         for name, desc, node in config.gauges_raf_list
            for raf in ["3"]#,"4","5"] #TODO get raf list automatically

            )

    #Create a dict type {node,Gauge} (node for each raf board)
    board_metrics = dict((node, Gauge("libera_{0}".format(name), desc))

        for name, desc, node in config.gauges_list
            )


    #merge dicts by value type (for platform.GetDouble, platform.GetString etc..)
    all_metrics = dict(raf_metrics.items() + board_metrics.items())

    #Run main export looop forever!
    while True:
        try:

            for node,metric in all_metrics.items():
                #print node
                metric.set(platform.GetValue(node))
        except RuntimeError as e:
            raise e
            #print ImportError(e)
            #print "Unexpected error:", sys.exc_info()[0]
            #print('Exception at metric {0}'.format(node))
            #Check if platformd is down - set the metric accordingly (..and Prometheus will send the alert)
            platform_status = check_platformd()
            platformd_metric.set(check_platformd())
            # # re init object ?? (or raise exception and exit?)
            # if platform_status == 1:
            #     # Maybe check for connection-reconnection
            #     print("Restarting platform connection") 
            #     platform.init()
            #     #platform = pylibera.PyLiberaClient(root_type="platform")

        print("End of parse")
        #While delay
        time.sleep(period)


if __name__ == '__main__':
    
    # Start up the server to expose the metrics.
    start_http_server(9110)
    
    # Gather metrics
    gather_data(10)