<?PHP

if(array_key_exists('Crear',$_POST))
{			
	
	if ($_REQUEST['Fecha'] != "" && $_REQUEST['Origen'] != ""  && $_REQUEST['RealizadoPor'] != ""
		 && $_REQUEST['Destino'] != "" && $_REQUEST['Recibe'] != ""  && $_REQUEST['Observaciones'] != "") 
	{
			
		$Fecha = $_POST['Fecha'];
		$Origen = $_POST['Origen'];
		$RealizadoPor = $_POST['RealizadoPor'];
		$Destino = $_POST['Destino'];
		$Recibe = $_POST['Recibe'];
		$Observaciones = $_POST['Observaciones'];
		
		include ('conexion.php');

		$sql="INSERT INTO `tbl_actas` (`IdActa`, `Realizado Por`, `Origen`, `Fecha de Entrega`, `Destino`, `Enviado por`, `Aprobado por`, `Comentarios`, `Recibido Por`) VALUES (NULL, '$RealizadoPor', '$Origen', '$Fecha', '$Destino', NULL, NULL, '$Observaciones', '$Recibe');";

		mysqli_query($con, $sql);
		mysqli_close($con); 
	
		print "<script>alert(\"Acta creada correctamente.\");window.location='../EditarActa.php';</script>";
	}
	else
	{
		print "<script>alert(\"Debe completar todos los datoSs\")";
	}
}

?>