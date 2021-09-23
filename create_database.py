import pandas as pd
import psycopg2

params_database = {
    "host"      : "localhost",
    "user"      : "postgres",
    "password"  : "postgres",
    "port"      : "5432"
}

def create_database():
    sql = '''CREATE database movies''';
    #create a database
    conn = None
    
    try:
        # read the connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params_database)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_database()