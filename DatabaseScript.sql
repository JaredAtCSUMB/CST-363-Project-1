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
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `branch` (
  `BranchID` int(11) NOT NULL AUTO_INCREMENT,
  `BranchName` varchar(120) NOT NULL,
  `StreetAddress` varchar(120) NOT NULL,
  `City` varchar(120) NOT NULL,
  `State` char(2) NOT NULL,
  `ZIP` char(5) NOT NULL,
  PRIMARY KEY (`BranchID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES (1,'JAD Linden 1','2044 Duke Lane','Linden','NJ','07036'),(2,'JAD Ellensburg 2','76 Goodwin Avenue','Ellensburg','WA','98926'),(3,'JAD New York 3','2746 Oakwood Avenue','New York','NY','10016'),(4,'JAD Houston 4','4741 Brooke Street','Houston','TX','56922'),(5,'JAD Miami 5','2118 Tyler Avenue','Miami','FL','12967');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car` (
  `CarID` int(11) NOT NULL AUTO_INCREMENT,
  `RegistrationNumber` varchar(30) NOT NULL,
  `Year` int(11) NOT NULL,
  `Model` varchar(50) NOT NULL,
  `Maker` varchar(50) NOT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  PRIMARY KEY (`CarID`),
  KEY `fk_car_cust_idx` (`CustomerID`),
  CONSTRAINT `fk_car_cust` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'BA 985PA',2019,'VA Z001','Toyota',1),(2,'AX 895AX',2018,'BA Max 1','General Motors',2),(3,'BA 159MM',2105,'HT 234','Honda',3),(4,'TV 459BB',2010,'TU VX','Toyota',4),(5,'KA 894LA',2000,'GM 334','General Motors',5),(6,'ZZ 512TV',2014,'YA 2014','Toyota',6),(7,'VB 259BB',2013,'Sport 303','Honda',7),(8,'TV 256ZA',2012,'MB 3456','Mercedes Benz ',1);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `CustomerID` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(60) NOT NULL,
  `LastName` varchar(60) NOT NULL,
  `EmailAddress` varchar(120) DEFAULT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL,
  `StreetAddress` varchar(120) DEFAULT NULL,
  `City` varchar(120) DEFAULT NULL,
  `State` char(2) DEFAULT NULL,
  `ZIP` char(5) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Jeremy','Lawrence','jeryam@gmail.com','659-8959-569','3752 Cimmaron Road','Placentia','CA','26598'),(2,'Santiago','Genovese','stangia@hotmail.com','569-9587-895','4052 Kooter Lane','Charlotte','NC','96856'),(3,'Michael','Bailey','mchea@gmail.com','359-8561-852','3710 Cedar Lane','Boston','MA','63595'),(4,'Mose','McBroom','mose233@gmail.com','256-8912-854','3282 Bryan Street','Greensboro','MA','32584'),(5,'Rex','Woodard','rexwoda@hotmail.com','256-9512-741','2493 Oakdale Avenue','Okeechobee','NC','12584'),(6,'Yvonne','Nicholson','ahcoanichen@gmail.com','112-9654-521','3786 B Street','New Brighton','CA','12541'),(7,'Lori','Grieco','lorigeara233@hotmail.com','321-9865-852','1836 Christie Way','Framingham','NY','36598');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `ItemID` int(11) NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(120) NOT NULL,
  `Price` double NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Front Right Outer door handle',2.39),(2,'Door control module',6.26),(3,'Front Right Side Door Glass',12.25),(4,'Speaker 01',26.99),(5,'Performance Battery',2.99),(6,'Battery tray',52.62),(7,'Distributor Cap',15.24),(8,'Ignition magneto',26.24),(9,'Coolant temperature sensor',26.24),(10,'Power window switch',25.65),(11,'Air intake manifold',12.55),(12,'Mounting',16.17),(13,'Water pump pulley',12.54),(14,'Exhaust manifold gasket',21.59);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mechanic`
--

DROP TABLE IF EXISTS `mechanic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mechanic` (
  `MechanicID` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(60) NOT NULL,
  `LastName` varchar(60) NOT NULL,
  `EmailAddress` varchar(120) DEFAULT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL,
  `StreetAddress` varchar(120) DEFAULT NULL,
  `City` varchar(120) DEFAULT NULL,
  `State` char(2) DEFAULT NULL,
  `ZIP` char(5) DEFAULT NULL,
  `BranchID` int(11) NOT NULL,
  PRIMARY KEY (`MechanicID`),
  KEY `fk_mechanic_branch_idx` (`BranchID`),
  CONSTRAINT `fk_mechanic_branch` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mechanic`
--

LOCK TABLES `mechanic` WRITE;
/*!40000 ALTER TABLE `mechanic` DISABLE KEYS */;
INSERT INTO `mechanic` VALUES (1,'Karen','Farrell','karen@gmail.com','562-8959-865','4733 Five Points','Glen Burnie','MD','62658',1),(2,'Anthony','Mirabal','abnato@gmail.com','754-2568-412','1503 Woodland Drive','Chicago','IL','23515',1),(3,'Bernice','Infante','breandd@hotmail.com','485-4598-451','1447 Cottrill Lane','Maryland Heights','MO','12574',1),(4,'Crystal','Cramer','cyracla@hotmail.com','123-4582-125','2148 Abner Road','Lac Du Flambeau','WI','96548',1),(5,'Lisa','Knarr','lisa@gmail.com','1395-451-125','2032 Chandler Drive','Joplin','MO','12685',1),(6,'Louise','Williamson','lause@hotmail.com','4569-865-425','815 Conifer Drive','Issaquah','WA','12358',2),(7,'George','Reyes','geaoread@yahoo.com','1238-854-562','2685 Steve Hunt Road','Boca Raton','FL','18565',3),(8,'Teri','Boswell','terrowbose@gmail.com','1238-956-456','856 Patterson Fork Road','Chicago','IL','23541',4),(9,'Walter','Hein','waterhea@gmail.com','1358-594-854','469 Timberbrook Lane','Glenwood Springs','CO','25648',5);
/*!40000 ALTER TABLE `mechanic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderline`
--

DROP TABLE IF EXISTS `orderline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderline` (
  `OrderLineID` int(11) NOT NULL AUTO_INCREMENT,
  `OrderID` int(11) NOT NULL,
  `ServiceID` int(11) NOT NULL,
  PRIMARY KEY (`OrderLineID`),
  KEY `fk_ol_orders_idx` (`OrderID`),
  KEY `fk_ol_service_idx` (`ServiceID`),
  CONSTRAINT `fk_ol_order` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`OrderID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ol_service` FOREIGN KEY (`ServiceID`) REFERENCES `service` (`ServiceID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderline`
--

LOCK TABLES `orderline` WRITE;
/*!40000 ALTER TABLE `orderline` DISABLE KEYS */;
INSERT INTO `orderline` VALUES (1,1,1),(2,1,2),(3,2,3),(4,3,4),(5,4,5),(6,5,3),(7,6,1),(8,7,2),(9,8,3);
/*!40000 ALTER TABLE `orderline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderlineitem`
--

DROP TABLE IF EXISTS `orderlineitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderlineitem` (
  `OrderLineID` int(11) NOT NULL AUTO_INCREMENT,
  `ItemID` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`OrderLineID`),
  KEY `fk_oli_item_idx` (`ItemID`),
  CONSTRAINT `fk_oli_item` FOREIGN KEY (`ItemID`) REFERENCES `item` (`ItemID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_oli_ol` FOREIGN KEY (`OrderLineID`) REFERENCES `orderline` (`OrderLineID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderlineitem`
--

LOCK TABLES `orderlineitem` WRITE;
/*!40000 ALTER TABLE `orderlineitem` DISABLE KEYS */;
INSERT INTO `orderlineitem` VALUES (1,3,1),(2,4,2),(3,1,1);
/*!40000 ALTER TABLE `orderlineitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderlinemachanic`
--

DROP TABLE IF EXISTS `orderlinemachanic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderlinemachanic` (
  `OrderLineID` int(11) NOT NULL,
  `MechanicID` int(11) NOT NULL,
  PRIMARY KEY (`OrderLineID`,`MechanicID`),
  KEY `fk_olm_me_idx` (`MechanicID`),
  CONSTRAINT `fk_olm_me` FOREIGN KEY (`MechanicID`) REFERENCES `mechanic` (`MechanicID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_olm_ol` FOREIGN KEY (`OrderLineID`) REFERENCES `orderline` (`OrderLineID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderlinemachanic`
--

LOCK TABLES `orderlinemachanic` WRITE;
/*!40000 ALTER TABLE `orderlinemachanic` DISABLE KEYS */;
INSERT INTO `orderlinemachanic` VALUES (1,1),(1,2),(1,3),(3,3),(5,3),(2,4),(6,4),(2,5),(7,5),(8,6),(9,7),(4,9);
/*!40000 ALTER TABLE `orderlinemachanic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `OrderID` int(11) NOT NULL AUTO_INCREMENT,
  `OrderDate` date NOT NULL,
  `CustomerID` int(11) NOT NULL,
  `CarID` int(11) NOT NULL,
  `BranchID` int(11) NOT NULL,
  PRIMARY KEY (`OrderID`),
  KEY `fk_orders_cust_idx` (`CustomerID`),
  KEY `fk_orders_car_idx` (`CarID`),
  KEY `fk_orders_branch_idx` (`BranchID`),
  CONSTRAINT `fk_orders_branch` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_car` FOREIGN KEY (`CarID`) REFERENCES `car` (`CarID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_cust` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2018-12-01',1,1,1),(2,'2018-12-01',2,2,1),(3,'2018-12-12',3,3,1),(4,'2018-12-13',4,4,1),(5,'2018-12-14',5,5,1),(6,'2018-12-14',6,6,1),(7,'2018-12-15',7,7,2),(8,'2018-12-15',1,8,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service` (
  `ServiceID` int(11) NOT NULL AUTO_INCREMENT,
  `ServiceName` varchar(120) NOT NULL,
  `Price` varchar(45) NOT NULL,
  PRIMARY KEY (`ServiceID`)
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

-- Dump completed on 2019-01-19 11:36:19
