-- Script that lists all shows contained in the database
SELECT tv_shows.title, tv_show_genres.genre_id -- Query to join shows and genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title;
