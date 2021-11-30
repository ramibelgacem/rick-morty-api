import json
import os
from psycopg2 import connect, Error

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
EPISODE_DATA_PATH = os.path.join(
    CURRENT_PATH,
    '../data/rick_morty-episodes_v1.json')
CHARACETR_DATA_PATH = os.path.join(
    CURRENT_PATH,
    '../data/rick_morty-characters_v1.json')

try:
    conn = connect(
        dbname="rick_morty",
        user="odoo",
        host="localhost",
        password="postgres",
        connect_timeout=3
    )

    cur = conn.cursor()
    print("created cursor object:", cur)
except (Exception, Error) as err:
    print("psycopg2 connect error:", err)
    conn = None
    cur = None

if cur is not None:
    try:
        episodes_characters = {}
        with open(EPISODE_DATA_PATH) as episodes_json:
            episodes_list = json.load(episodes_json)
            for episode in episodes_list:
                episodes_characters[episode['id']] = episode['characters']
                del episode['characters']

                table_name = "episodes"
                columns = list(episode.keys())
                columns[columns.index('episode')] = 'reference'
                columns = ', '.join([str(x) for x in columns])
                values = ', '.join(
                    ["'" + str(x).replace("'", "''") + "'"
                     for x in list(episode.values())]
                )

                sql_string = f"INSERT INTO {table_name} ({columns}) \
                                VALUES ({values})"
                print(sql_string)

                cur.execute(sql_string)
                conn.commit()
            print('\nfinished INSERT INTO episodes')

        with open(CHARACETR_DATA_PATH) as characters_json:
            characters_list = json.load(characters_json)
            for character in characters_list:
                del character['episode']

                table_name = "characters"
                columns = ', '.join([str(x) for x in list(character.keys())])
                values = ', '.join(
                    ["'" + str(x).replace("'", "''") + "'"
                     for x in list(character.values())]
                )

                sql_string = f"INSERT INTO {table_name} ({columns}) \
                                VALUES ({values})"
                print(sql_string)

                cur.execute(sql_string)
                conn.commit()
            print('\nfinished INSERT INTO characters')

        for episode in episodes_characters:
            for character in episodes_characters[episode]:
                table_name = 'episode_character'
                columns = ', '.join(['episode_id', 'character_id'])
                values = ', '.join([str(episode), str(character)])

                sql_string = f"INSERT INTO {table_name} ({columns}) \
                                VALUES ({values})"
                print(sql_string)

                cur.execute(sql_string)
                conn.commit()
        print('\nfinished INSERT INTO many2many')
    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()
    # close the cursor and connection
    cur.close()
    conn.close()
