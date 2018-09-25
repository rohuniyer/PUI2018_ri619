#This file should take in live bus locations based on certain routes

import requests
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#Check that the number of arguments given is correct. If not, exit program and 
# ask for the correct arguments.
if not len(sys.argv) == 3:
    print("Invalid number of arguments. Please provide your API key and Bus line.")
    sys.exit()
    
API = sys.argv[1]
bus_line = sys.argv[2]
    

#Use givent API key and bus line to pull relevant data from MTA.
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + str(API) + "&VehicleMonitoringDetailLevel=calls&LineRef=" + str(bus_line)
response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)


#Parse through the returned json data and determine the number of buses 
# currently active.
veh_monitoring = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses = len(veh_monitoring)

print("Bus Line: " + bus_line)
print("Number of Active Buses: " + str(num_buses))


#For the number of buses active, parse to the location data and record that for 
# each bus. Then print out said location data. 
for i in range(num_buses):
    loc = veh_monitoring[i]['MonitoredVehicleJourney']['VehicleLocation']
    longitude = loc['Longitude']
    latitude = loc['Latitude']
    print("Bus " + str(i) + " is at latitude " + str(latitude) + " and longitude " + str(longitude))
    




