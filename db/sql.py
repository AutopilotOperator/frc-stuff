import sqlite3


conn = sqlite3.connect('tba.db')
cursor = conn.cursor()

#  a query that creates a table with the following columns:  team_id, name, country, city, rookie_year 

CREATE_TEAM_TABLE_QUERY = """ CREATE TABLE IF NOT EXISTS Team (
    team_id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    city TEXT,
    rookie_year INTEGER
)"""

# a query that creates an event table with table with the following columns: event_id, type_name, type_id, start_date, end_date, region
CREATE_EVENT_TABLE_QUERY = """ CREATE TABLE IF NOT EXISTS Event ( 
    event_id TEXT PRIMARY KEY,
    type_name TEXT,
    type_id INTEGER,
    start_date TEXT,
    end_date TEXT,
    region TEXT
)"""

#  a query the creates a match table with the following columns: match_id, event_id, red1, red2, red3, blue1, blue2, blue3, winner, score_blue, score_red, match_number, blue_rp, red_rp
CREATE_MATCH_TABLE_QUERY = """ CREATE TABLE IF NOT EXISTS Match (
    match_id TEXT PRIMARY KEY,
    event_id TEXT,
    red_1_team_id INTEGER,
    red_2_team_id INTEGER,
    red_3_team_id INTEGER,
    blue_1_team_id INTEGER,
    blue_2_team_id INTEGER,
    blue_3_team_id INTEGER,
    winning_alliance TEXT,
    score_blue INTEGER,
    score_red INTEGER,
    match_number INTEGER,
    blue_rp INTEGER,
    red_rp INTEGER,
    foul_count INTEGER,
    foul_points INTEGER,
    FOREIGN KEY (event_id) REFERENCES Event (event_id),
    FOREIGN KEY (red_1_team_id) REFERENCES Team (team_id),
    FOREIGN KEY (red_2_team_id) REFERENCES Team (team_id),
    FOREIGN KEY (red_3_team_id) REFERENCES Team (team_id),
    FOREIGN KEY (blue_1_team_id) REFERENCES Team (team_id),
    FOREIGN KEY (blue_2_team_id) REFERENCES Team (team_id),
    FOREIGN KEY (blue_3_team_id) REFERENCES Team (team_id)
    )"""


DROP_EVENT_TABLE_QUERY = """DROP TABLE IF EXISTS Event"""
DROP_MATCH_TABLE_QUERY = """DROP TABLE IF EXISTS Match"""
DROP_TEAM_TABLE_QUERY = """DROP TABLE IF EXISTS Team"""


class SQLUtilities:
    def __init__(self):
        self.conn = sqlite3.connect('tba.db')
        self.cursor = self.conn.cursor()
    
    def close(self):
        self.conn.close()

    def run_query(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(f"Error running query: {query}")
            print(f"Error message: {e}")
            self.conn.close()
            raise e
    
    def drop_all_tables(self):
        self.run_query(DROP_EVENT_TABLE_QUERY)
        self.run_query(DROP_MATCH_TABLE_QUERY)
        self.run_query(DROP_TEAM_TABLE_QUERY)

    def create_all_tables(self):
        self.run_query(CREATE_TEAM_TABLE_QUERY)
        self.run_query(CREATE_EVENT_TABLE_QUERY)
        self.run_query(CREATE_MATCH_TABLE_QUERY)



    def insert_team(self, team_id, name, country, city, rookie_year):
        self.cursor.execute("INSERT INTO Team VALUES (?, ?, ?, ?, ?)", (team_id, name, country, city, rookie_year))
        self.conn.commit()


def insert_team(team_id, name, country, city, rookie_year):
    cursor.execute("INSERT INTO Team VALUES (?, ?, ?, ?, ?)", (team_id, name, country, city, rookie_year))
    conn.commit()

def insert_event(event_id, type_name, type_id, start_date, end_date, region):
    cursor.execute("INSERT INTO Event VALUES (?, ?, ?, ?, ?, ?)", (event_id, type_name, type_id, start_date, end_date, region))
    conn.commit()

def create_all_tables():
    cursor.execute(CREATE_TEAM_TABLE_QUERY)
    conn.commit()
    cursor.execute(CREATE_EVENT_TABLE_QUERY)
    conn.commit()
    cursor.execute(CREATE_MATCH_TABLE_QUERY)
    conn.commit()
    conn.close()


def create_event_table():
    cursor.execute(CREATE_EVENT_TABLE_QUERY)
    conn.commit()
    conn.close()

def drop_event_table():
    cursor.execute(DROP_EVENT_TABLE_QUERY)
    conn.commit()
    conn.close()

def drop_match_table():
    cursor.execute(DROP_MATCH_TABLE_QUERY)
    conn.commit()
    conn.close()


def create_match_table():
    cursor.execute(CREATE_MATCH_TABLE_QUERY)
    conn.commit()
    conn.close()


def select_all_events():
    cursor.execute("SELECT * FROM Event")
    events = cursor.fetchall()
    conn.close()
    return events