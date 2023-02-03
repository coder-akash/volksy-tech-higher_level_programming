-- task
select distinct name from tv_shows inner join tv_show_genres on tv_shows.id = tv_show_genres.show_id inner join tv_genres on tv_show_genres.genre_id = tv_genres.id where title <> 'Dexter' order by name;
