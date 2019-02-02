USE `jadautorepair_dw`;

insert into jadautorepair_dw.customer (customer_id, first_name, last_name, username, password, phone_number)
SELECT customer_id, first_name, last_name, username, password, phone_number
FROM jadautorepair.customer;

insert into jadautorepair_dw.car (car_id, car_make, car_model, car_year, customer_id)
SELECT car_id, car_make, car_model, car_year, customer_id
from jadautorepair.car;

insert into jadautorepair_dw.service (service_id, service_name, price)
SELECT service_id, service_name, price
from jadautorepair.service;


insert into jadautorepair_dw.orders(car_id, customer_id, service_id, order_year, order_month, order_day, amount)
SELECT jadautorepair.car.car_id, jadautorepair.customer.customer_id, jadautorepair.service.service_id, 
year(order_date), month(order_date), day(order_date), sum(price)
from jadautorepair.car, jadautorepair.customer, jadautorepair.service, jadautorepair.orders
where jadautorepair.car.car_id = jadautorepair.orders.car_id and
jadautorepair.customer.customer_id = jadautorepair.car.customer_id and
jadautorepair.service.service_id = jadautorepair.orders.service_id
group by jadautorepair.car.car_id, jadautorepair.customer.customer_id, jadautorepair.service.service_id, 
year(order_date), month(order_date), day(order_date);

