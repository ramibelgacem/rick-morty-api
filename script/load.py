import json
import os

from decouple import config
from psycopg2 import connect, Error

DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST', default='localhost')
DATABASE_PORT = config('DATABASE_PORT', default='5432')
DATABASE_NAME = config('DATABASE_NAME')

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
EPISODE_DATA_PATH = os.path.join(
    CURRENT_PATH,
    '../data/rick_morty-episodes_v1.json')
CHARACETR_DATA_PATH = os.path.join(
    CURRENT_PATH,
    '../data/rick_morty-characters_v1.json')


def connect_db():
    try:
        conn = connect(
            dbname=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            connect_timeout=3
        )

        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print("Successfully connected to database\n"
              "PostgreSQL database version:", db_version)
    except (Exception, Error) as e:
        print("Database connection error:", e)
        conn = None
        cur = None

    return cur, conn


def import_data(cur, conn):
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

                    cur.execute(sql_string)
                    conn.commit()
                print('\nSuccessfully importing episodes')

            with open(CHARACETR_DATA_PATH) as characters_json:
                characters_list = json.load(characters_json)
                for character in characters_list:
                    del character['episode']

                    table_name = "characters"
                    columns = ', '.join(
                        [str(x) for x in list(character.keys())])
                    values = ', '.join(
                        ["'" + str(x).replace("'", "''") + "'"
                         for x in list(character.values())]
                    )

                    sql_string = f"INSERT INTO {table_name} ({columns}) \
                                    VALUES ({values})"

                    cur.execute(sql_string)
                    conn.commit()
                print('\nSuccessfully importing characters')

            for episode in episodes_characters:
                for character in episodes_characters[episode]:
                    table_name = 'episode_character'
                    columns = ', '.join(['episode_id', 'character_id'])
                    values = ', '.join([str(episode), str(character)])

                    sql_string = f"INSERT INTO {table_name} ({columns}) \
                                    VALUES ({values})"

                    cur.execute(sql_string)
                    conn.commit()
            print('\nSuccessfully importing episode_character')
        except (Exception, Error) as error:
            print("\nExecuting query error:", error)
            conn.rollback()
        finally:
            cur.close()
            conn.close()


if __name__ == "__main__":
    cur, conn = connect_db()
    import_data(cur, conn)
