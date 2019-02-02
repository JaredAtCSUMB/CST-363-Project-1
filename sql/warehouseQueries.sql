/*
OLAP Questions Our App Will Answer:

1) customers have more than 1 car in the shop
2) services (and cost) each vehicle has received by year, month, day
3) Which services are used most in year
4) What time (year, month, day) are the services are used
5) The average number of customers each year, month
6) How much they spend on average per year
*/
select customer.customer_id, customer.first_name, customer.last_name
from customer, orders
where customer.customer_id = orders.customer_id
group by customer.customer_id, customer.first_name, customer.last_name
having count(distinct orders.car_id) > 1;

select service.service_id, service_name, order_year, order_month, order_day, sum(amount) as total
from service, orders
where service.service_id = orders.service_id
group by service.service_id, service_name, order_year, order_month, order_day with rollup;

select service.service_id, service_name, order_year as 'year', count(*) as times
from service, orders
where service.service_id = orders.service_id
group by service.service_id, service_name, order_year
order by times desc
limit 1;

select service.service_id, service_name, order_year as 'year', order_month as 'month', order_day as 'day', count(*) as 'number of times used'
from service, orders
where service.service_id = orders.service_id
group by service.service_id, service_name, order_year, order_month, order_day
order by count(*) desc;

select order_year as 'year', order_month as 'month', avg(customer_id) as 'average number of customers'
from orders
group by order_year, order_month;

select order_year as 'year', avg(amount) as 'average spending'
from orders
group by order_year;



