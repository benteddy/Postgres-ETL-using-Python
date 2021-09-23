import pandas as pd
import psycopg2

params_table = {
    "host"      : "localhost",
    "database"  : "movies",
    "user"      : "postgres",
    "password"  : "postgres",
    "port"      : "5432"
}

def insert_movies(movie_list):
    """ insert multiple movies into the movies table  """
    movies = pd.read_csv("data/movies.csv")
    tuples = [tuple(x) for x in movies.to_numpy()]
    sql = "INSERT INTO movies(MOVIES, YEAR, GENRE, RATING, ONE_LINE, STARS, VOTES, RunTime, Gross) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params_table)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,movie_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == '__main__':
    # insert multiple movies
    insert_movies(tuples)