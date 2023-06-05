CREATE DATABASE bd_sistema_ventas;

USE bd_sistema_ventas;

CREATE TABLE trabajadores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    sueldo DECIMAL(10, 2)
);

INSERT INTO trabajadores (nombre, sueldo) VALUES ('Juan Pérez', 400000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('María López', 300000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Pedro Rodríguez', 450000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Ana García', 380000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Luisa Martínez', 320000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Carlos Sánchez', 500000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Laura Fernández', 370000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Roberto Torres', 420000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Sofía Ramírez', 390000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Diego Herrera', 430000);
INSERT INTO trabajadores (nombre, sueldo) VALUES ('Valeria Gómez', 350000);

select * from trabajadores;
-- DROP DATABASE bd_sistema_ventas;




