CREATE TABLE `football` (
	`game-date` VARCHAR(50) NOT NULL,
	`homeTeam` VARCHAR(50) NOT NULL,
	`homeScore` TINYINT(4) NOT NULL,
	`awayTeam` VARCHAR(50) NOT NULL,
	`awayScore` VARCHAR(50) NOT NULL,
	`league` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`game-date`, `homeTeam`),
	INDEX `game-date` (`game-date`),
	INDEX `homeTeam` (`homeTeam`),
	INDEX `league` (`league`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
