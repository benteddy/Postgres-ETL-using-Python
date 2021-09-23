import pandas as pd
import psycopg2

params_table = {
    "host"      : "localhost",
    "database"  : "movies",
    "user"      : "postgres",
    "password"  : "postgres",
    "port"      : "5432"
}

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE movies (
            MOVIES varchar,
            YEAR varchar,
            GENRE varchar,
            RATING varchar,
            ONE_LINE varchar,
            STARS varchar,
            VOTES varchar,
            RunTime varchar,
            Gross varchar
        )
        """)
    conn = None
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params_table)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_tables()