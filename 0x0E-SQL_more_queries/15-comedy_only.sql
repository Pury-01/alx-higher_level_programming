-- lists all comedy shows in hbtn_0d_tvshows database
-- each record displays tv_show.title

SELECT title FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY title;
