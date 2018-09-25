import requests
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib



if not len(sys.argv) == 4:
    print("Invalid number of arguments. Please provide your API key, Bus line, and csv file to write to.")
    sys.exit()
    
API = sys.argv[1]
bus_line = sys.argv[2]
fout = open(sys.argv[3], "w")
    

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + str(API) + "&VehicleMonitoringDetailLevel=calls&LineRef=" + str(bus_line)
response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)



veh_monitoring = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses = len(veh_monitoring)

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")


for i in range(num_buses):
    loc = veh_monitoring[i]['MonitoredVehicleJourney']['VehicleLocation']
    longitude = loc['Longitude']
    latitude = loc['Latitude']
    try:
        stops = veh_monitoring[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
        stop_name = stops[0]['StopPointName']
        stop_status = stops[0]['Extensions']['Distances']['PresentableDistance']
    except KeyError:
        stop_name = 'N/A'
        stop_status = 'N/A'
    str_to_write = str(latitude) + "," + str(longitude) + "," + str(stop_name) + "," + str(stop_status)
    fout.write(str_to_write)
    fout.write("\n")
    

    
