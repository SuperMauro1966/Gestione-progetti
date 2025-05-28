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

-- Dump della struttura di tabella gestione_progetti.milestone
DROP TABLE IF EXISTS `milestone`;
CREATE TABLE IF NOT EXISTS `milestone` (
  `ID_Milestone` int(11) NOT NULL,
  `Nome_Milestone` varchar(50) NOT NULL DEFAULT '',
  `Data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.progetto
DROP TABLE IF EXISTS `progetto`;
CREATE TABLE IF NOT EXISTS `progetto` (
  `ID_Progetto` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) NOT NULL DEFAULT '',
  `Descrizione` varchar(200) NOT NULL DEFAULT '0',
  `Data_Inizio` date NOT NULL,
  `Data_Fine` date NOT NULL,
  PRIMARY KEY (`ID_Progetto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.risorsa
DROP TABLE IF EXISTS `risorsa`;
CREATE TABLE IF NOT EXISTS `risorsa` (
  `ID_Risorsa` int(11) NOT NULL,
  `Descrizione_Risorsa` text NOT NULL,
  `Quantita` int(15) NOT NULL DEFAULT 0,
  `UnitaDiMisura` varchar(50) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
