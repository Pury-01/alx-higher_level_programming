-- lists all shows contained in hbtn_0d_tvshows
-- shows have atleast 1 genre linked

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
