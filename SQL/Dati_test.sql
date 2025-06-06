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

-- Dump dei dati della tabella gestione_progetti.appartiene: ~12 rows (circa)
INSERT INTO `appartiene` (`ID_Task`, `ID_WP`, `ES`, `LS`, `LF`, `RF`, `Stato`, `Note`) VALUES
	(1, 1, '2025-06-21', '2025-06-22', '2025-06-24', '2025-06-23', 'non inizioato', '--'),
	(3, 2, '2025-06-23', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(4, 2, '2025-06-20', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(5, 3, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(6, 3, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(7, 4, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(9, 1, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(10, 3, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(10, 4, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(2, 1, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(9, 2, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--'),
	(8, 4, '2025-06-22', '2025-06-23', '2025-06-25', '2025-06-23', 'iniziato', '--');

-- Dump dei dati della tabella gestione_progetti.deliverable: ~3 rows (circa)
INSERT INTO `deliverable` (`ID_Milestone_D`, `ID_Risorse_D`, `Quantita`) VALUES
	(2, 4, 1),
	(2, 5, 2),
	(2, 6, 4);

-- Dump dei dati della tabella gestione_progetti.milestone: ~3 rows (circa)
INSERT INTO `milestone` (`ID_Milestone`, `Nome_Milestone`, `Data_Milestone`, `ID_Progetto_Milestone`) VALUES
	(1, 'nuova milestone', '2025-06-09', 4),
	(2, 'M1', '2025-06-22', 8),
	(3, 'M2', '2025-06-24', 8);

-- Dump dei dati della tabella gestione_progetti.necessita: ~4 rows (circa)
INSERT INTO `necessita` (`ID_Task_N`, `ID_Risorse_N`) VALUES
	(1, 4),
	(2, 5),
	(3, 5),
	(4, 6);

-- Dump dei dati della tabella gestione_progetti.produce: ~3 rows (circa)
INSERT INTO `produce` (`ID_Risorse_P`, `ID_WP_P`, `Quantita`) VALUES
	(4, 1, 2),
	(5, 2, 2),
	(5, 3, 3);

-- Dump dei dati della tabella gestione_progetti.progetto: ~4 rows (circa)
INSERT INTO `progetto` (`ID_Progetto`, `Nome_P`, `Descrizione_P`, `Data_Inizio`, `Data_Fine`) VALUES
	(4, 'festa', 'piccola festa a casa', '2025-05-29', '2025-05-30'),
	(5, 'matrimonio', 'matrimonio in riva al mare', '2025-06-06', '2025-06-07'),
	(6, 'consegna', 'consegna di vari pacchi', '2025-06-01', '2025-06-03'),
	(8, 'P1', 'progetto d\'esempio', '2025-06-20', '2025-06-25');

-- Dump dei dati della tabella gestione_progetti.risorsa: ~3 rows (circa)
INSERT INTO `risorsa` (`ID_Risorsa`, `Descrizione_Risorsa`, `Quantita_R`, `UnitaDiMisura`) VALUES
	(4, 'acqua', 3, 'litri'),
	(5, 'lavoro', 4, 'ore'),
	(6, '6 pezzi di lana', 6, 'pezzi');

-- Dump dei dati della tabella gestione_progetti.scompone: ~0 rows (circa)

-- Dump dei dati della tabella gestione_progetti.task: ~10 rows (circa)
INSERT INTO `task` (`ID_Task`, `Nome_Task`, `Descrizione_Task`) VALUES
	(1, 'task 1', 'primo task di WPG11'),
	(2, 'task 2', 'secondo task'),
	(3, 'task 3', 'terzo task'),
	(4, 'task 4', 'quarto task'),
	(5, 'task 5', 'quinto task'),
	(6, 'task 6', 'sesto  task'),
	(7, 'task 7', 'settimo task'),
	(8, 'task 8', 'ottavo task'),
	(9, 'task 9', 'nono task'),
	(10, 'task 10', 'decimo task');

-- Dump dei dati della tabella gestione_progetti.wbs: ~4 rows (circa)
INSERT INTO `wbs` (`ID_WBS`, `Nome_WBS`, `Descrizione_WBS`, `ID_Progetto_WBS`) VALUES
	(1, 'wbs_progetto_festa', 'wbs di primo livello', 4),
	(3, 'wbs primaria', 'prima wbs del progetto', 5),
	(4, 'WBS1', 'wbs per P1', 8),
	(5, 'WBS2', 'seconda wbs per P1', 8);

-- Dump dei dati della tabella gestione_progetti.work_package: ~0 rows (circa)
INSERT INTO `work_package` (`ID_WP`, `Nome_WP`, `Descrizione_WP`, `Note`, `ID_WBS_WP`) VALUES
	(1, 'WPG11', 'primo work package associato a wbs1', '--', 4),
	(2, 'WPG12', 'secondo work package associato a wbs1', 'WBS1', 4),
	(3, 'WPG21', 'primo work package associato al secondo', '--', 5),
	(4, 'WPG22', 'secondo work package associato a wbs2', '--', 5);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
