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


CREATE TABLE `football_member` (
	`league` VARCHAR(50) NOT NULL,
	`game_date` VARCHAR(50) NOT NULL,
	`teamName` VARCHAR(50) NOT NULL,
	`player` VARCHAR(50) NOT NULL,
	`type` VARCHAR(50) NOT NULL,
        `shirtNumber` INT NOT NULL,
	`position` VARCHAR(50),
	`posorder` CHAR(2),
        `stime` TINYINT(2),
        `goal` TINYINT(2),
	PRIMARY KEY (`league`, `game_date`, `teamName`, `player`, `type`, `shirtNumber`),
	INDEX `league` (`league`),
	INDEX `game_date` (`game_date`),
	INDEX `teamName` (`teamName`),
	INDEX `player` (`player`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;