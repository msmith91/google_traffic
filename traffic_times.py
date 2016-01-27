#!/usr/bin/env python

__doc__ = 'Google Maps tool for obtaining estimated trip times.'
__author__ = 'Michael Smith'
__license__ = 'MIT'

import urllib, time, datetime, sys, os.path, json, pprint, argparse

parser = argparse.ArgumentParser(description='Google Maps tool for obtaining estimated trip times.')
parser.add_argument("-tm", "--traffic-model", help="traffic model to use",
                    type=str, choices=['best_guess', 'pessimistic', 'optimistic', 'all'])
parser.add_argument("-d", "--direction", help="direction of travel", 
                    type=str, choices=['to_work', 'from_work'])
parser.add_argument("-dt", "--departure-time", help="time of departure", 
                    type=int) #does nothing as of now
args = parser.parse_args()

#Preset Locations, separated by +s.
home = '300+Upper+Brook+St,+Manchester'
work = '700+Stockport+Rd,+Manchester'
#CSV File to write to.
csv_file = '/destination/path/to/csv/file.csv'

direction = args.direction
traffic_model = args.traffic_model

class googleMaps:
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/directions/json?'
        self.key = 'API KEY GOES HERE'

    def get_time(self, origin, destination, traffic_model):
        """Return observations for a given trip.

        Parameters:
            self - unknown
            origin - string - the begining location of the trip.
            destination - string - the end location of the trip.
            traffic_model - best_guess|pessimistic|optimistic - the traffic model to use for time estimation.
        """
        url = self.url+'origin='+origin+'&destination='+destination+'&key='+self.key+'&departure_time=now&traffic_model='+traffic_model
        json_url = urllib.urlopen(url).read()
        json_dict = json.loads(json_url)
        time_estimate = json_dict['routes'][0]['legs'][0]['duration_in_traffic']['value'] /60
        current_time = time.localtime(time.time())
        if origin == home:
            return [time_estimate,traffic_model,current_time[6],current_time[3]-6,current_time[4],'to_work']
        else:
            return [time_estimate,traffic_model,current_time[6],current_time[3]-6,current_time[4],'from_work']

    def to_csv(self,list):
        """Convert array to CSV format.

        Parameters:
            self - unknown
            list - array - the array to be converted to CSV format.
        """
        return ','.join([str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5])+'\n']) 

    #function to write take existing csv file (could be nonexistent) and append the new line from get_time()
    def write_csv(self,list,filename):
        """Append array to CSV file.

        Parameters:
            self - unknown
            list - array - the array to be appended to the CSV file.
            filename - string - the CSV file the array should be appended to.
        """
    #    self.check_csv(filename)
        with open(filename,'a') as f:
            f.write(self.to_csv(list))
        f.close()

    def check_csv(self, filename):
        """Ensure file existance.

        Parameters:
            self - unknown
            filename - string - the file whos existance will be ensured.
        """
        if os.path.isfile(filename):
            return
        else:
            file_directory = os.path.dirname(filename)
            os.makedirs(file_directory)
            open(filename, 'a').close()

if __name__ == "__main__":
    if direction == 'to_work':
        if traffic_model == 'all':
            for model in ['best_guess', 'pessimistic', 'optimistic']:
                time_list = googleMaps().get_time(home, work, model)
                googleMaps().write_csv(time_list, csv_file)
        else:
            time_list = googleMaps().get_time(work, home, traffic_model)
            googleMaps().write_csv(time_list, csv_file)

    elif direction == 'from_work':
        if traffic_model == 'all':
            for model in ['best_guess', 'pessimistic', 'optimistic']:
                time_list = googleMaps().get_time(work, home, model)
                googleMaps().write_csv(time_list, csv_file)
        else:
            time_list = googleMaps().get_time(work, home, traffic_model)
            googleMaps().write_csv(time_list, csv_file)
