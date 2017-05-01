<?PHP

if(array_key_exists('Editar',$_POST))
{			
	
		if ($_REQUEST['Material'] != "" 
		&& $_REQUEST['Descripcion'] != ""  
		&& $_REQUEST['Ubicacion'] != "" 
		&& $_REQUEST['Partnumber'] != ""
		&& $_REQUEST['Proveedor'] != ""
		) 
	{
			
		$Material = $_POST['Material'];
		$Descripcion = $_POST['Descripcion'];
		$Ubicacion = $_POST['Ubicacion'];
		$Partnumber = $_POST['Partnumber'];
		$Proveedor = $_POST['Proveedor'];

		include ('conexion.php');

		print $Material;

		$sql = "UPDATE `tbl_materiales` SET `Material` = '$Material', `Descripcion` = '$Descripcion', `Ubicacion` = '$Ubicacion', `Partnumber` = '$Partnumber', `Proveedor` = '$Proveedor' WHERE `tbl_materiales`.`Material` LIKE '$Material';";

		mysqli_query($con, $sql);
		mysqli_close($con); 
	
		print "<script>window.location='../EditaMaterial.php';</script>";
	}
	else
	{
		print "<script>alert(\"Debe completar todos los datoSs\")";
	}
}

?>