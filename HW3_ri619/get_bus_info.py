import requests
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#Check for the correct number of arguments. If incorrect, exit program and print the following. 
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Please provide your API key, Bus line, and csv file to write to.")
    sys.exit()
    

#If the number of arguments is correct, load the API key, Bus line, and 
#  output file in the following variables. 
API = sys.argv[1]
bus_line = sys.argv[2]
fout = open(sys.argv[3], "w")
    

#Pull data from MTA using the API key and Bus line. Load the json into a 
#  response variable. 
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + str(API) + "&VehicleMonitoringDetailLevel=calls&LineRef=" + str(bus_line)
response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)


#Using the response variable, parse to the relevant information. In this case,
#  it is the data of each bus on the line currently.
veh_monitoring = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses = len(veh_monitoring)


#write to the output file.
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")


#This for loop, loops through the list provided in the json. For each index,
#  we load the location data. Then we try pulling the stop name and stop status.
#  Since some busses do not have this, if we get a 'KeyError', we fill in the
#  stop name and stop status with 'N/A' values. After getting this info,
#  write to the output file.
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
    

fout.close()    
