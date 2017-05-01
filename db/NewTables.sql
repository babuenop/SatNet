CREATE TABLE `tbl_salidas` (
  `IdSalida` int(3) NOT NULL,
  `Realizado Por` varchar(34) DEFAULT NULL,
  `Origen` varchar(32) DEFAULT NULL,
  `FechaDeSalida ` varchar(10) DEFAULT NULL,
  `Destino` varchar(32) NOT NULL,
  `EnviadoPor` varchar(34) DEFAULT NULL,
  `AprobadoPor` varchar(27) DEFAULT NULL,
  `Comentarios` varchar(186) DEFAULT NULL,
  `RetiradoPor` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;