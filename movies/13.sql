SELECT name FROM people WHERE people.id IN  -- Get the names of all the actors who starred in the movie
(SELECT DISTINCT person_id FROM stars WHERE movie_id IN  -- find all person_id's that starred in Kevin Bacons movie
(SELECT movie_id FROM stars where person_id =  -- find all movies Id's that kevin bacon was in
(SELECT id FROM people WHERE name = "Kevin Bacon" AND birth = 1958))) -- start by selecting Kevin Bacon's ID
AND name != "Kevin Bacon";  -- don't select Kevin Bacon's name
