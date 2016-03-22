import psycopg2 as postgres
from psycopg2.extras import RealDictCursor

conn = postgres.connect("dbname=brew user=postgres", cursor_factory=RealDictCursor)
cur = conn.cursor()


def get_all_beers():
  cur.execute('SELECT * FROM beers')
  beers = cur.fetchall()
  return beers or []


def save_new_beer(values):
  cur.execute("INSERT INTO beers (name, abv, rating) VALUES (%s, %s, %s) RETURNING *",
    (values['name'], values['abv'], values['rating']))
  conn.commit()
  beer = cur.fetchone()
  return beer

def delete_beer(beer_id):
  cur.execute("DELETE FROM beers WHERE id=%s", [beer_id])
  conn.commit()
  return get_all_beers()

