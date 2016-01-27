#####################################################################
#googleMaps API tool for pulling time duration from 'home' to 'work'#
#Author: Michael Smith#
#####################################################################

import urllib,time,datetime,sys
import json,pprint

# info about locations
home = '123+Park+Place+Chicago+IL'
work = '456+Other+Place+Chicago+IL'

class googleMaps:
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/directions/json?'
        self.key = 'API KEY GOES HERE'

    #function for creating new observation given a origin, destination, and model of traffic
    #options for traffic model are ('best_guess','pessimistic','optimistic')  
    def get_time(self, origin, destination, traffic_model):
        url = self.url+'origin='+origin+'&destination='+destination+'&key='+self.key+'&departure_time=now&traffic_model='+traffic_model
        json_url = urllib.urlopen(url).read()
        json_dict = json.loads(json_url)
        time_estimate = json_dict['routes'][0]['legs'][0]['duration_in_traffic']['value'] /60
        current_time = time.localtime(time.time())
        if origin == home:
            return [time_estimate,traffic_model,current_time[6],current_time[3]-6,current_time[4],'to_work']
        else:
            return [time_estimate,traffic_model,current_time[6],current_time[3]-6,current_time[4],'from_work']

    #function to write the new observation created in get_time() in a csv string
    def to_csv(self,list):
        return ','.join([str(list[0]),str(list[1]),str(list[2]),str(list[3]),str(list[4]),str(list[5])+'\n']) 

    #function to write take existing csv file (could be nonexistent) and append the new line from get_time()
    def write_csv(self,list,filename):
        with open(filename,'a') as f:
            f.write(self.to_csv(list))
        f.close()

# put it all together!
# call the script with "python travel_times.py to_work" to get time from 'home' to 'work' 
# or "python travel_times.py from_work" to get time from 'work' to 'home' as defined at the top.
# script returns time estimation for all 3 types of traffic models

if __name__ == "__main__":
    try:
        arg = sys.argv[1]
        if arg == 'to_work':
            for model in ['best_guess','pessimistic','optimistic']:
                time_list = googleMaps().get_time(home,work,model)
                googleMaps().write_csv(time_list,'/destination/path/to/csv/file.csv')

        elif sys.argv[1] == 'from_work':
            for model in ['best_guess','pessimistic','optimistic']:
                time_list = googleMaps().get_time(work,home,model)
                googleMaps().write_csv(time_list,'/destination/path/to/csv/file.csv')

    except:
        print('Missing argument: needs either "to_work" or "from_work"')
