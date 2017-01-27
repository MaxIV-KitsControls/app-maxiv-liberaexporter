"""
Prometheus exporter which sends Libera platform metrics to prometheus server.
The prometheus server,however needs to be configured to poll it, e.g. "<hostname>:9110
"""
from prometheus_client import start_http_server, Gauge
import time, sys, subprocess, re
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
        #raise RuntimeError("Platform is not running!")
        return 0
    else:
        return 1


def getrafboards():
    """
    Returns a list of strings with the numbers of the raf boards (Normally 3-5)
    In case of error raise RuntimeError exception
    """
    p=subprocess.Popen(["libera-ireg", "dump", "-P", "boards.", "--level=1"], stdout=subprocess.PIPE)

    output,err=p.communicate()

    #if any error occur raise and exit
    if p.returncode==1:
        raise RuntimeError("Error while executing libera-ireg dump -P boards. --level=1 command")

    #output = subprocess.check_call(["libera-ireg", "dump", "-P", "boards.", "--level=1"], stdout=subprocess.PIPE) 

    #Get list of raf boards
    boardlist=re.findall(r'raf([1-7])', output, re.MULTILINE)
    return boardlist

def gather_data(period=1):
    """
    Function which inits the metrics and runs the main loop that publishes metrics forever
    """
    # INIT, prepare metric lists to be able to be used by Prometheus

    #Create a Gauge metric which monitors the platform service
    platformd_metric = Gauge("platformd_service_status", "Metric to monitor platform service")
    #Set initial value
    platformd_metric.set(check_platformd())

    #Connect to libera
    try:
        #create the pylibera object
        platform = pylibera.PyLiberaClient(root_type="platform")
        #Get number of raf boards
        rafboardlist=getrafboards()
    except RuntimeError as e:
        #Check if platform is still alive
        platform_status = check_platformd()
        #set the metric (0 or 1)
        platformd_metric.set(check_platformd())
        #raise exception and exit
        raise e

    #Create a dict type {node,Gauge} (node for each raf board)
    raf_metrics = dict((node.format(raf), Gauge("libera_raf{0}_{1}".format(raf, name), desc))
        #Assign each raf board No to each raf board
         for name, desc, node in config.gauges_raf_list
            for raf in rafboardlist

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
            #Check if platform is still alive
            platform_status = check_platformd()
            #set the metric (0 or 1)
            platformd_metric.set(check_platformd())
            #raise exception and exit
            raise e

        #While delay
        time.sleep(period)

def main():
    # Start up the server to expose the metrics.
    start_http_server(9232)
    
    # Gather metrics
    gather_data(10)


if __name__ == '__main__':
    main()
    
