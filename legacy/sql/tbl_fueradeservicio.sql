-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-01-2017 a las 12:33:23
-- Versión del servidor: 10.1.13-MariaDB
-- Versión de PHP: 7.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `satnet`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_fueradeservicio`
--

CREATE TABLE `tbl_fueradeservicio` (
  `IdRegistro` int(11) NOT NULL,
  `Casino` varchar(35) NOT NULL,
  `Maquina` varchar(35) NOT NULL,
  `Modelo` varchar(35) NOT NULL,
  `Fabricante` varchar(35) NOT NULL,
  `EnServicio` varchar(2) NOT NULL,
  `Desde` date NOT NULL,
  `Solicitud` int(11) NOT NULL,
  `Motivo` varchar(255) NOT NULL,
  `Acciones` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_fueradeservicio`
--
ALTER TABLE `tbl_fueradeservicio`
  ADD PRIMARY KEY (`IdRegistro`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_fueradeservicio`
--
ALTER TABLE `tbl_fueradeservicio`
  MODIFY `IdRegistro` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
