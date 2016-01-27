
# google_traffic
 
 Google Maps tool for obtaining estimated trip times.
 
# Description
 
 traffic_times.py is a Python 2 script that retrieves 3 travel duration estimates working off the assuption that you depart at the current time.
 
# Google API Key Requirements
 
 For this project, you'll need a Google API Key. You can do so here:
 https://developers.google.com/maps/documentation/javascript/get-api-key#key
 
 1. Create a Google Developer Project. [Link](https://console.developers.google.com/project)
 2. Enable Google Maps Directions API.
   1. Click 'Use Google APIs' (a blue box).
   2. Stay on Overview tab.
   3. Click more in Google Maps API section.
   4. Click 'Google Maps Directions API'.
   5. Click 'Enable API' button.
 3. Create Server API Key.
   1. Click Credentials tab.
   2. Click New credentials.
   3. Click API key.
   4. Click Server key.
   5. Name your key.
   6. Click Create.
   7. Copy your key.
 4. Set googleMaps.self.key to your API key.
 
# Usage
  
  
 +```traffic_times.py [-h] [-tm {best_guess,pessimistic,optimistic,all}] [-d {to_work,from_work}]```
 +
 +### Arguments
 +
 +```
 +-h, --help              shows this help message and exit
 +-tm {best_guess,pessimistic,optimistic,all}, --traffic-model {best_guess,pessimistic,optimistic,all}
 +                        traffic model to use
 +-d {to_work,from_work}, --direction {to_work,from_work}
 +                        direction of travel
 +
 +```
 +
# Recommended Setup
  
I have my crontab setup to run the following:
 
Run to_work during morning commute times:
*/10 11-15 * * 1-5 /usr/bin/python traffic_times.py -tm all -d to_work
 
Run from_work during evening commute times:
*/10 19-23 * * 1-5 /usr/bin/python traffic_times.py -tm all -d from_work
 
I run the r script from time to time to update graphs (Rscript traffic_plots.R)
