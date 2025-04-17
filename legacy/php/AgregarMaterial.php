<?PHP

if(array_key_exists('Agregar',$_POST))
{			
	
	if ($_REQUEST['Material'] != "" 
		&& $_REQUEST['Descripcion'] != ""  
		&& $_REQUEST['Proveedor'] != "" 
		&& $_REQUEST['Estado'] != ""
		&& $_REQUEST['Cantidad'] != ""
		&& $_REQUEST['IngresadoPor'] != ""
		) 
	{
			
		$IdActa=$_POST['IdActa'];
		$Material = $_POST['Material'];
		$Descripcion = $_POST['Descripcion'];
		$Proveedor = $_POST['Proveedor'];
		$Estado = $_POST['Estado'];
		$Cantidad = $_POST['Cantidad'];
		$IngresadoPor = $_POST['IngresadoPor'];
		
		include ('conexion.php');

		$sql = "INSERT INTO `tbl_actasdetalle` (`IdActa`, `Codigo`, `Descripcion`, `Proveedor`, `Estado`, `Cantidad`, `Revisado Por`) VALUES ('$IdActa', '$Material', '$Descripcion', '$Proveedor', '$Estado', '$Cantidad', '$IngresadoPor')";

		mysqli_query($con, $sql);
		mysqli_close($con); 
	
		print "<script>window.location='../EditarActa.php';</script>";
	}
	else
	{
		print "<script>alert(\"Debe completar todos los datoSs\")";
	}
}

?>