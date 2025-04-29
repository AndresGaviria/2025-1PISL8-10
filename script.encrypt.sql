CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_personas;

CREATE TABLE `db_personas`.`estados` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(500) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_personas`.`personas` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `cedula` VARCHAR(500) NOT NULL UNIQUE,
    `nombre` VARCHAR(500) NOT NULL,
    `estado` INT NOT NULL,
    `fecha` DATETIME NOT NULL,
    `activo` BIT NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_personas__estados` FOREIGN KEY (`estado`) REFERENCES `estados`(`id`)
);

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_select_estados`()
BEGIN
    SELECT `id`,
        `nombre`
    FROM `db_personas`.`estados`;
END$$

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_insert_estados`(
    IN `Nombre` VARCHAR(500),
    INOUT `Respuesta` INT
)
BEGIN
    INSERT INTO `db_personas`.`estados` (`nombre`) 
    VALUES (`Nombre`);

    SET `Respuesta` = 0;
END$$