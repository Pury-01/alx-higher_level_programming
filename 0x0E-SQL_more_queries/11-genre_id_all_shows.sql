-- lists all shows contained in hbtn_0d_tvshows
-- displays tv_shows.title - tv_show_genres.genre_id
-- results sorted in ascending order 
-- displays NULL if show doesn't have a genre

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows, title, tv_show_genres.genre_id;
