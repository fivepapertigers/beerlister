CREATE TABLE beers (id serial, name text, abv int, rating int);
CREATE UNIQUE INDEX beer_name on beers (LOWER(name));