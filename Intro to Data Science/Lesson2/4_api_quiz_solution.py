import json
import requests

# works

def api_get_request():
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    # return ... # return the top artist in Spain


# if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain
    api_key = "ad1ccfe66fe5a920da16284639bf1c1d"
    method ="geo.getTopArtists"
    parameters = "&country=spain&format=json"
    url = "http://ws.audioscrobbler.com/2.0/?method=" + method + "&api_key=" + api_key + parameters
    data = requests.get(url).text
    data = json.loads(data)
    #print type(data)
    #print api_get_request(url) 
    #print data
    #print data['topartists']['artist']['name']
    print data['topartists']['artist']['rank' == 1]['name']
    # actual solution with picking first line instead of rank 1
    print data['topartists']['artist'][0]['name']

api_get_request()

