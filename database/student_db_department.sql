-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: student_db
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `department_name` varchar(100) NOT NULL,
  `college_code` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_name`),
  KEY `fk_department_college1_idx` (`college_code`),
  CONSTRAINT `fk_department_college1` FOREIGN KEY (`college_code`) REFERENCES `college` (`college_code`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('English Department','CASS'),('History Department','CASS'),('Political Science Department','CASS'),('Psychology Department','CASS'),('Sociology Department','CASS'),('Accountancy Department','CBAA'),('Economics Department','CBAA'),('Hospitality & Tourism Management Department','CBAA'),('Marketing Department','CBAA'),('Computer Application Department','CCS'),('Computer Science Department','CCS'),('Departamento ng Filipino at ibang mga Wika','CCS'),('Information Technology Department','CCS'),('Physical Education Department','CED'),('Professional Education Department','CED'),('Science and Mathematics Department','CED'),('Technology Teacher Education Department','CED'),('Chemical Engineering and Technology Department','COET'),('Civil Engineering Department','COET'),('Electrical and Electronics Engineering and Technology','COET'),('Materials and Resources Engineering and Technology Department','COET'),('Mechanical Engineering and Technology Department','COET'),('Nursing Department','CON'),('Biological Sciences Department','CSM'),('Chemistry Department','CSM'),('Mathematics & Statistics Department','CSM'),('Physics Department','CSM');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-14 14:40:21
