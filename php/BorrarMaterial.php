<?php 
	require('conexion.php');
	
	$IdActa=$_GET['IdActa'];
	$Codigo=$_GET['Codigo'];
	
	$sql="DELETE FROM `tbl_actasdetalle` WHERE `IdActa`=$IdActa and `Codigo`=$Codigo";
	
	mysqli_query($con, $sql);
	mysqli_close($con); 

	print "<script>window.location='../EditarActa.php';</script>";
?>