<?PHP

if(array_key_exists('Crear',$_POST))
{			
	
	if ($_REQUEST['Material'] != "" 
		&& $_REQUEST['Descripcion'] != ""  
		&& $_REQUEST['Ubicacion'] != "" 
		&& $_REQUEST['Categoria'] != ""
		&& $_REQUEST['Partnumber'] != ""
		&& $_REQUEST['Proveedor'] != ""
		) 
	{
			
		$Material=$_POST['Material'];
		$Descripcion = $_POST['Descripcion'];
		$Ubicacion = $_POST['Ubicacion'];
		$Categoria = $_POST['Categoria'];
		$Partnumber = $_POST['Partnumber'];
		$Proveedor = $_POST['Proveedor'];
		
		include ('conexion.php');

		
		$sql = "INSERT INTO `tbl_materiales` (`Material`, `Descripcion`, `Ubicacion`, `Partnumber`, `Proveedor`, `Categoria`) VALUES ('$Material', '$Descripcion', '$Ubicacion', '$Partnumber', '$Proveedor', '$Categoria');";

		mysqli_query($con, $sql);
		mysqli_close($con); 
	
		print "<script>window.location='../EditaMaterial.php?Material=$Material';</script>";
	}
	else
	{
		print "<script>alert(\"Debe completar todos los datoSs\")";
	}
}

?>