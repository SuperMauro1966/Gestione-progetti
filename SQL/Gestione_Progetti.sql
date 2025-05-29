-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              10.6.22-MariaDB - mariadb.org binary distribution
-- S.O. server:                  Win64
-- HeidiSQL Versione:            12.10.0.7000
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dump della struttura del database gestione_progetti
DROP DATABASE IF EXISTS `gestione_progetti`;
CREATE DATABASE IF NOT EXISTS `gestione_progetti` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `gestione_progetti`;

-- Dump della struttura di tabella gestione_progetti.deliverable
DROP TABLE IF EXISTS `deliverable`;
CREATE TABLE IF NOT EXISTS `deliverable` (
  `ID_Milestone` int(11) NOT NULL,
  `ID_Risorse` int(11) NOT NULL,
  `Quantita` int(10) NOT NULL,
  PRIMARY KEY (`ID_Milestone`,`ID_Risorse`) USING BTREE,
  KEY `FK_deliverables_risorsa` (`ID_Risorse`) USING BTREE,
  KEY `FK_deliverables_milestone` (`ID_Milestone`) USING BTREE,
  CONSTRAINT `FK_deliverables_milestone` FOREIGN KEY (`ID_Milestone`) REFERENCES `milestone` (`ID_Milestone`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_deliverables_risorsa` FOREIGN KEY (`ID_Risorse`) REFERENCES `risorsa` (`ID_Risorsa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
