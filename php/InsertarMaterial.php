<?PHP

if(array_key_exists('Crear',$_POST))
{			
	
	if ($_REQUEST['Fecha'] != "" && $_REQUEST['RealizadoPor'] != ""  && $_REQUEST['Observaciones'] != "") 
	{
			
		$Fecha = $_POST['Fecha'];
		$RealizadoPor = $_POST['RealizadoPor'];
		$Observaciones = $_POST['Observaciones'];
		
		include ('conexion.php');

		$sql="INSERT INTO `tbl_actas` (`IdActa`, `Realizado Por`, `Casino`, `Fecha de Entrega`, `Enviado por`, `Aprobado por`, `Comentarios`, `Recibido Por`) VALUES (NULL, '$RealizadoPor', NULL, '$Fecha', NULL, NULL, '$Observaciones', NULL)";

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