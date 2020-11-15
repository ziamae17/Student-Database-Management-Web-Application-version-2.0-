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
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_code` varchar(10) NOT NULL,
  `course_name` varchar(50) DEFAULT NULL,
  `college_code` varchar(100) DEFAULT NULL,
  `department_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_code`),
  KEY `fk_course_college1_idx` (`college_code`) /*!80000 INVISIBLE */,
  KEY `fk_course_department1_idx` (`department_name`) /*!80000 INVISIBLE */,
  CONSTRAINT `fk_course_department1_idx` FOREIGN KEY (`department_name`) REFERENCES `department` (`department_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('BAE','BA English','CASS','English Department'),('BAFOL','BA Filipino & Other Languages','CASS','Departamento ng Filipino at ibang mga Wika'),('BAH','BA History','CASS','History Department'),('BAPS','BA Political Science','CASS','Political Science Department'),('BAS','BA Sociology','CASS','Sociology Department'),('BEEE','BEE English','CED','Professional Education Department'),('BEELE','BEE Language Education','CED','Professional Education Department'),('BEESH','BEE Science and Health','CED','Professional Education Department'),('BEESM','BEE Science and Mathematics','CED','Science and Mathematics Department'),('BPE','B Physical Education','CED','Physical Education Department'),('BSA','BS Accountancy','CBAA','Accountancy Department'),('BSB','BS Biology (General)','CSM','Biological Sciences Department'),('BSBABE','BS Business Administration (Business Economics)','CBAA','Economics Department'),('BSBAMM','BS Business Administration (Marketing Management)','CBAA','Marketing Department'),('BSBB','BS Biology (Botany)','CSM','Biological Sciences Department'),('BSBM','BS Biology (Marine)','CSM','Biological Sciences Department'),('BSBZ','BS Biology (Zoology)','CSM','Biological Sciences Department'),('BSC','BS Chemistry','CSM','Chemistry Department'),('BSCA','BS Computer Application','CCS','Computer Application Department'),('BSCE','BS Civil Engineering','COET','Civil Engineering Department'),('BSCME','BS Chemical Engineering','COET','Chemical Engineering and Technology Department'),('BSCOME','BS Computer Engineering','COET','Electrical and Electronics Engineering and Technology'),('BSCRE','BS Ceramics Engineering','COET','Materials and Resources Engineering and Technology Department'),('BSCS','BS Computer Science','CCS','Computer Science Department'),('BSE','BS Economics','CBAA','Economics Department'),('BSEB','BSE Biology','CED','Science and Mathematics Department'),('BSEC','BSE Chemistry','CED','Science and Mathematics Department'),('BSECE','BS Electronics and Communications Engineering','COET','Electrical and Electronics Engineering and Technology'),('BSEE','BS Electrical Engineering','COET','Electrical and Electronics Engineering and Technology'),('BSEET','BS Environmental Engineering Technology','COET','Materials and Resources Engineering and Technology Department'),('BSEF','BSE Filipino','CED','Professional Education Department'),('BSEGS','BSE General Science','CED','Science and Mathematics Department'),('BSEM','BSE Mathematics','CED','Science and Mathematics Department'),('BSEMAP','BSE Mapeh','CED','Technology Teacher Education Department'),('BSEN','BS Entrepreneurship','CBAA','Marketing Department'),('BSEP','BSE Physics','CED','Science and Mathematics Department'),('BSET','BSE TLE','CED','Technology Teacher Education Department'),('BSHM','BS Hospitality Mangement','CBAA','Hospitality & Tourism Management Department'),('BSID','BS Industrial Education (Drafting)','CED','Technology Teacher Education Department'),('BSIS','BS Information Systems','CCS','Information Technology Department'),('BSIT','BS Information Technology ','CCS','Information Technology Department'),('BSM','BS Mathematics','CSM','Mathematics & Statistics Department'),('BSMCE','BS Mechanical Engineering','COET','Mechanical Engineering and Technology Department'),('BSME','BS Metallurgical Engineering','COET','Materials and Resources Engineering and Technology Department'),('BSMNE','BS Mining Engineering ','COET','Materials and Resources Engineering and Technology Department'),('BSN','BS Nursing','CON',NULL),('BSP','BS Psychology','CASS','Psychology Department'),('BSPHY','BS Physics','CSM','Physics Department'),('BSS','BS Statistics','CSM','Mathematics & Statistics Department');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-14 14:40:22
