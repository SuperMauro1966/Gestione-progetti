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
CREATE DATABASE IF NOT EXISTS `gestione_progetti` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `gestione_progetti`;

-- Dump della struttura di tabella gestione_progetti.appartiene
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
  KEY `ID_WP` (`ID_WP`),
  CONSTRAINT `FK_appartiene_task` FOREIGN KEY (`ID_Task`) REFERENCES `task` (`ID_Task`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_appartiene_work package` FOREIGN KEY (`ID_WP`) REFERENCES `work_package` (`ID_WP`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.deliverable
CREATE TABLE IF NOT EXISTS `deliverable` (
  `ID_Milestone_D` int(11) NOT NULL,
  `ID_Risorse_D` int(11) NOT NULL,
  `Quantita` int(10) NOT NULL,
  PRIMARY KEY (`ID_Milestone_D`,`ID_Risorse_D`) USING BTREE,
  KEY `FK_deliverables_risorsa` (`ID_Risorse_D`) USING BTREE,
  KEY `FK_deliverables_milestone` (`ID_Milestone_D`) USING BTREE,
  CONSTRAINT `FK_deliverables_milestone` FOREIGN KEY (`ID_Milestone_D`) REFERENCES `milestone` (`ID_Milestone`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_deliverables_risorsa` FOREIGN KEY (`ID_Risorse_D`) REFERENCES `risorsa` (`ID_Risorsa`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.milestone
CREATE TABLE IF NOT EXISTS `milestone` (
  `ID_Milestone` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Milestone` varchar(50) NOT NULL DEFAULT '',
  `Data_Milestone` date NOT NULL,
  PRIMARY KEY (`ID_Milestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.necessita
CREATE TABLE IF NOT EXISTS `necessita` (
  `ID_Task_N` int(11) NOT NULL,
  `ID_Risorse_N` int(11) NOT NULL,
  KEY `ID_Task` (`ID_Task_N`) USING BTREE,
  KEY `ID_Risorse` (`ID_Risorse_N`) USING BTREE,
  CONSTRAINT `FK_necessita_risorsa` FOREIGN KEY (`ID_Risorse_N`) REFERENCES `risorsa` (`ID_Risorsa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_necessita_task` FOREIGN KEY (`ID_Task_N`) REFERENCES `task` (`ID_Task`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.produce
CREATE TABLE IF NOT EXISTS `produce` (
  `ID_Risorse_P` int(11) NOT NULL,
  `ID_WP_P` int(11) NOT NULL,
  `Quantita` int(10) NOT NULL,
  KEY `ID_Risorse` (`ID_Risorse_P`) USING BTREE,
  KEY `ID_WP` (`ID_WP_P`) USING BTREE,
  CONSTRAINT `FK_produce_risorsa` FOREIGN KEY (`ID_Risorse_P`) REFERENCES `risorsa` (`ID_Risorsa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_produce_work package` FOREIGN KEY (`ID_WP_P`) REFERENCES `work_package` (`ID_WP`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.progetto
CREATE TABLE IF NOT EXISTS `progetto` (
  `ID_Progetto` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_P` varchar(50) NOT NULL DEFAULT '',
  `Descrizione_P` varchar(50) NOT NULL DEFAULT '0',
  `Data_Inizio` date NOT NULL,
  `Data_Fine` date NOT NULL,
  PRIMARY KEY (`ID_Progetto`),
  UNIQUE KEY `idx_progetto_nome` (`Nome_P`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.risorsa
CREATE TABLE IF NOT EXISTS `risorsa` (
  `ID_Risorsa` int(11) NOT NULL AUTO_INCREMENT,
  `Descrizione_Risorsa` text NOT NULL,
  `Quantita_R` int(15) NOT NULL DEFAULT 0,
  `UnitaDiMisura` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID_Risorsa`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.scompone
CREATE TABLE IF NOT EXISTS `scompone` (
  `ID_WBS` int(11) NOT NULL,
  `ID_WBS(padre)` int(11) NOT NULL,
  KEY `ID_WBS` (`ID_WBS`),
  KEY `ID_WBS(padre)` (`ID_WBS(padre)`),
  CONSTRAINT `FK_scompone_wbs` FOREIGN KEY (`ID_WBS(padre)`) REFERENCES `wbs` (`ID_WBS`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.task
CREATE TABLE IF NOT EXISTS `task` (
  `ID_Task` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_Task` varchar(50) NOT NULL DEFAULT '',
  `Descrizione_Task` tinytext NOT NULL,
  PRIMARY KEY (`ID_Task`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.wbs
CREATE TABLE IF NOT EXISTS `wbs` (
  `ID_WBS` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_WBS` varchar(50) NOT NULL DEFAULT '0',
  `Descrizione_WBS` text NOT NULL,
  `ID_Progetto_WBS` int(11) NOT NULL,
  PRIMARY KEY (`ID_WBS`),
  KEY `ID_Progetto` (`ID_Progetto_WBS`) USING BTREE,
  CONSTRAINT `FK_wbs_progetto` FOREIGN KEY (`ID_Progetto_WBS`) REFERENCES `progetto` (`ID_Progetto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella gestione_progetti.work_package
CREATE TABLE IF NOT EXISTS `work_package` (
  `ID_WP` int(11) NOT NULL AUTO_INCREMENT,
  `Nome_WP` varchar(50) NOT NULL DEFAULT '0',
  `Descrizione_WP` varchar(50) NOT NULL DEFAULT '0',
  `Note` text NOT NULL,
  `ID_WBS_WP` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`ID_WP`),
  KEY `ID_WBS` (`ID_WBS_WP`) USING BTREE,
  CONSTRAINT `FK_work package_wbs` FOREIGN KEY (`ID_WBS_WP`) REFERENCES `wbs` (`ID_WBS`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- L’esportazione dei dati non era selezionata.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
