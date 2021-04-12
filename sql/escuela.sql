/*  CREACION DE LA BASE DE DATOS DE BE ECO.  */

/*  CREATE DATABASE IF NOT EXISTS beecoN;  */

USE beecoN;

CREATE TABLE IF NOT EXISTS alumnos(
    id_alumno int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    primer_apellido varchar(50) NOT NULL,
    contrasena varchar(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS comentarios(
    id_alumno int(11) NOT NULL,
    opinion varchar(250) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE comentarios ADD FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno);

INSERT INTO alumnos(nombre, primer_apellido, contrasena, fecha_nacimiento)
VALUES 
('Mel', 'Litow', 'Maldonado', '2000-01-10');

INSERT INTO comentarios(id_alumno, opinion)
VALUES 
('1', 'Hace poco tiempo lei que para reducir el cambio climático, la ONU propone cumplir con el acuerdo de París para evitar que el planeta aumente más de 2 ºC, así como revisar cada cinco años los compromisos de cada país');

SELECT nombre, primer_apellido, contrasena, fecha_nacimiento FROM alumnos;
SELECT id_alumno, opinion FROM comentarios;
