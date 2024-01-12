from dotenv import load_dotenv
import os
import requests


class BlueAllianceAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('TBA_API_KEY')
        if not self.api_key:
            raise Exception('TBA_API_KEY was not found in environmental variables')
        self.base_url = 'https://www.thebluealliance.com/api/v3/'


    def fetch_data(self, endpoint):
        url = self.base_url + endpoint
        headers = {
            'X-TBA-Auth-Key': self.api_key
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None
        

    def fetch_team_list(self, page):
        endpoint = 'teams/' + str(page)
        data = self.fetch_data(endpoint)
        return data
    
    def fetch_year_events(self, year):
        endpoint = 'events/' + str(year)
        data = self.fetch_data(endpoint)
        return data
    
    def fetch_event_matches(self, event_key):
        endpoint = 'event/' + event_key + '/matches'
        data = self.fetch_data(endpoint)
        return data
    
    