SET SQL_SAFE_UPDATES = 0; /* use this to turn off "Safe Mode" in MySQL */

USE sakila;

select address, city
from address as a
join city as c
on (a.city_id = c.city_id);


select address, city
from address a
join city c
using (city_id);

select * from film;

DESCRIBE film;

select count(film_id) as 'number_of_movies' /*doesn't make sense*/
from film;

select rating, count(film_id) as 'total film'
from film
group by rating
order by rating;

/* or */

select rating, sum(film_id) as 'total film'
from film
group by rating
order by rating;

/* or */

select rating, min(film_id) as 'total film'
from film
group by rating
order by rating;

/* or */

select rating, max(film_id) as 'total film'
from film
group by rating
order by rating;


select film_id from film;

select rental_duration, avg(rental_rate) as "Average Rental Rate"
from film
group by rental_duration
having rental_duration < 6; /* notice this */

/* or */

select rental_duration, avg(rental_rate) as "Average Rental Rate"
from film
where rental_duration < 6; /* notice this */
group by rental_duration




