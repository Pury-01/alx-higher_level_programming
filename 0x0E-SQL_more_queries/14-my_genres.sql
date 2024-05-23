-- uses hbtn_0d_tvshows database to list all genres of the show
-- named Dexter. Displays tv_genres.name

SELECT name FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON Tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY name;
