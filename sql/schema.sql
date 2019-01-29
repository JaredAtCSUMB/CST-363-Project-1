CREATE DATABASE  IF NOT EXISTS `jadautorepair` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `jadautorepair`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: jadautorepair
-- ------------------------------------------------------
-- Server version	5.7.15-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car` (
  `car_id` int(11) NOT NULL AUTO_INCREMENT,
  `car_make` varchar(120) NOT NULL,
  `car_model` varchar(120) NOT NULL,
  `car_year` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`car_id`),
  KEY `fk_car_cus_idx` (`customer_id`),
  CONSTRAINT `fk_car_cus` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'Toyota','TO 2001',2001,1),(2,'Toyota','YAO 29',2012,1),(3,'Toyota','TOA VA3',2019,2),(4,'Mercedes Benz ','MEA 001',2018,2),(5,'Mercedes Benz ','MEA 2001',2000,3),(6,'Honda','HIN 333',2011,4),(7,'Honda','HONV2',2009,5),(8,'Honda','TIAV 34',2011,6),(9,'General Motors','GM 2009',2008,7);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `username` varchar(120) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Jeremy','Lawrence','jeryam','ADFAS333','123-4567-889'),(2,'Santiago','Genovese','stangia','ADF#!E','456-4556-566'),(3,'Michael','Bailey','mchea','DOA34,','111-2345-678'),(4,'Mose','McBroom','mose233','BAA?#$','543-5678-222'),(5,'Rex','Woodard','rexwoda','@#A3445','233-4444-122'),(6,'Yvonne','Nicholson','ahcoanichen','$AB3Ada','345-2956-445'),(7,'Lori','Grieco','lorigeara233','d%A5?!','220-2345-555');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `username` varchar(60) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Karen','Farrell','kan1','123456'),(2,'Anthony','Mirabal','aut2','454$@1'),(3,'Bernice','Infante','brea3','34334A'),(4,'Crystal','Cramer','cryle','A3455$#'),(5,'Lisa','Knarr','la34','G$>2'),(6,'Louise','Williamson','lau5443','TGANBA#'),(7,'George','Reyes','dgao34','@!AB#'),(8,'Teri','Boswell','teaab34','34BA3.A!'),(9,'Walter','Hein','wat34','BAD3$#A)');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `car_id` int(11) NOT NULL,
  `service_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `fk_o_car_idx` (`car_id`),
  KEY `fk_o_serv_idx` (`service_id`),
  CONSTRAINT `fk_o_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_o_serv` FOREIGN KEY (`service_id`) REFERENCES `service` (`service_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2018-12-01',1,1),(2,'2018-12-01',2,2),(3,'2018-12-12',3,3),(4,'2018-12-13',4,4),(5,'2018-12-14',5,5),(6,'2018-12-14',6,6),(7,'2018-12-15',7,7),(8,'2018-12-15',1,8);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(120) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES (1,'Oil change','36.62'),(2,'Brake repair','69.99'),(3,'Transmission repair','32.77'),(4,'Radiator repair','26.99'),(5,'Water Pumps','36.99'),(6,'Timing Belts','34.99'),(7,'Anti-Lock Brakes (ABS)','95.99'),(8,'Power Windows & Doors','26.50'),(9,'Wheel Alignments','31.25'),(10,'Steering','56.25'),(11,'Fix Rattles, Squeaks & Bangs','53.29');
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'jadautorepair'
--

--
-- Dumping routines for database 'jadautorepair'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-25 14:45:46
