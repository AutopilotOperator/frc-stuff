import requests
from sql import insert_team, insert_event, create_match_table, drop_match_table
from api import BlueAllianceAPI




def fetch_teams():
    blue_alliance_api = BlueAllianceAPI()

    did_end = False
    current_page = 0
    while not did_end:
        teams = blue_alliance_api.get_teams(page=current_page)
        current_page += 1
        print(current_page)
        if len(teams) < 1:
            did_end = True
        for team in teams:
            # print(team)
            try:
                insert_team(team["team_number"], team["nickname"], team["country"], team["city"], team["rookie_year"])
            except Exception as e:
                print(e)
                print(team)
                continue

    
    return teams

def fetch_events():
    blue_alliance_api = BlueAllianceAPI()
    
    did_end = False
    current_year = 1990
    while not did_end:
        events = blue_alliance_api.fetch_events(current_year)
        current_year += 1
        if current_year >= 2024:
            did_end = True
        
        for event in events:
            # print(event)
            try:
                insert_event(event["key"], event["event_type_string"], event["event_type"], event["start_date"], event["end_date"], event["country"])
            except Exception as e:
                print(e)
                print(event["key"], event["event_type_string"], event["event_type"], event["start_date"], event["end_date"], event["country"])
                # print(event)
                continue

    
    return events



    

def fetch_all_matches():
    pass


if __name__ == "__main__":
    # create_all_tables()
    # fetch_teams()
    # fetch_events()
    # create_event_table()
    # drop_event_table()
    # drop_match_table()
    create_match_table()