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

-- Dump della struttura di tabella gestione_progetti.appartiene
DROP TABLE IF EXISTS `appartiene`;
CREATE TABLE IF NOT EXISTS `appartiene` (
  `ID_Task` int(11) NOT NULL,
  `ID_WP` int(11) NOT NULL,
  `ES` date NOT NULL,
  `LS` date NOT NULL,
  `LF` date NOT NULL,
  `RF` date NOT NULL,
  `Stato` varchar(50) NOT NULL DEFAULT '',
  `Note` tinytext NOT NULL,
  KEY `ID_Task` (`ID_Task`),
  KEY `ID_WP` (`ID_WP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.appartiene: ~0 rows (circa)

-- Dump della struttura di tabella gestione_progetti.deliverables
DROP TABLE IF EXISTS `deliverables`;
CREATE TABLE IF NOT EXISTS `deliverables` (
  `ID_Milestone` int(11) NOT NULL,
  `ID_Risorse` int(11) NOT NULL,
  KEY `ID_Milestone` (`ID_Milestone`),
  KEY `ID_Risorse` (`ID_Risorse`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.deliverables: ~0 rows (circa)

-- Dump della struttura di tabella gestione_progetti.milestone
DROP TABLE IF EXISTS `milestone`;
CREATE TABLE IF NOT EXISTS `milestone` (
  `ID_Milestone` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Milestone` varchar(50) NOT NULL DEFAULT '',
  `Data` date NOT NULL,
  PRIMARY KEY (`ID_Milestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.milestone: ~0 rows (circa)

-- Dump della struttura di tabella gestione_progetti.necessita
DROP TABLE IF EXISTS `necessita`;
CREATE TABLE IF NOT EXISTS `necessita` (
  `ID_Task` int(11) NOT NULL,
  `ID_Risorse` int(11) NOT NULL,
  KEY `ID_Task` (`ID_Task`),
  KEY `ID_Risorse` (`ID_Risorse`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.necessita: ~0 rows (circa)

-- Dump della struttura di tabella gestione_progetti.produce
DROP TABLE IF EXISTS `produce`;
CREATE TABLE IF NOT EXISTS `produce` (
  `ID_Risorse` int(11) NOT NULL,
  `ID_WP` int(11) NOT NULL,
  `Quantita` int(10) NOT NULL,
  KEY `ID_Risorse` (`ID_Risorse`),
  KEY `ID_WP` (`ID_WP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.produce: ~0 rows (circa)

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

-- Dump dei dati della tabella gestione_progetti.progetto: ~2 rows (circa)
INSERT INTO `progetto` (`ID_Progetto`, `Nome`, `Descrizione`, `Data_Inizio`, `Data_Fine`) VALUES
	(1, 'festa', 'piccola festa a casa', '2005-02-10', '2005-02-11'),
	(3, 'Festona', 'grande festa in ristorante', '2010-07-19', '2010-07-20');

-- Dump della struttura di tabella gestione_progetti.risorsa
DROP TABLE IF EXISTS `risorsa`;
CREATE TABLE IF NOT EXISTS `risorsa` (
  `ID_Risorsa` int(11) NOT NULL AUTO_INCREMENT,
  `Descrizione_Risorsa` text NOT NULL,
  `Quantita` int(15) NOT NULL DEFAULT 0,
  `UnitaDiMisura` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID_Risorsa`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.risorsa: ~0 rows (circa)

-- Dump della struttura di tabella gestione_progetti.task
DROP TABLE IF EXISTS `task`;
CREATE TABLE IF NOT EXISTS `task` (
  `ID_Task` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Task` varchar(50) NOT NULL DEFAULT '',
  `Descrizione_Task` tinytext NOT NULL,
  PRIMARY KEY (`ID_Task`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dump dei dati della tabella gestione_progetti.task: ~0 rows (circa)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
