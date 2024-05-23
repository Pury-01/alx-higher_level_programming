-- lists all cities contained in the hbtn_0d_usa database
-- each record displays cities.id-cities.name-states.name
-- results sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
