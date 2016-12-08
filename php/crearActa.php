<?php
$Fecha =$_POST["Fecha"];
$CreadoPor =$_POST["RealizadoPor"];
$Observaciones =$_POST["Observaciones"];

Echo($Fecha."<br>".$CreadoPor."<br>".$Observaciones);

include ("conexion.php");

$sql = "INSERT INTO `tbl_actas` (
	`IdActa`, 
	`Realizado Por`, 
	`Casino`, 
	`Fecha de Entrega`, 
	`Enviado por`, 
	`Aprobado por`, 
	`Comentarios`, 
	`Recibido Por`) 

	VALUES (NULL, $CreadoPor, NULL, $Fecha, NULL, NULL, $Observaciones, NULL)";

	$query = $con->query($sql);
			if($query!=null){
				print "<script>window.location='../EditarActa.php';</script>";
mysqli_close($conexion);
}
?>