DROP DATABASE  IF EXISTS `jadautorepair_dw`;
CREATE DATABASE  IF NOT EXISTS `jadautorepair_dw`;
USE `jadautorepair_dw`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `username` varchar(120) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

CREATE TABLE `car` (
  `car_id` int(11) NOT NULL AUTO_INCREMENT,
  `car_make` varchar(120) NOT NULL,
  `car_model` varchar(120) NOT NULL,
  `car_year` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`car_id`),
  KEY `fk_car_cus_idx` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;


CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(120) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

CREATE TABLE `orders` (
  `car_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `order_year` int(11) NOT NULL,
  `order_month` int(11) NOT NULL,
  `order_day` int(11) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`car_id`,`customer_id`,`service_id`,`order_year`,`order_month`,`order_day`),
  KEY `fk_o_service_idx` (`service_id`),
  KEY `fk_o_cust_idx` (`customer_id`),
  CONSTRAINT `fk_o_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_o_cust` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_o_service` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
