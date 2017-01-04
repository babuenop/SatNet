<?php
	require('../php/conexion.php');
	$sql="SELECT * FROM `tbl_fueradeservicio` ORDER BY `Desde`";
	$resultado=$con->query($sql);
	$row=$resultado->fetch_assoc();
	$IdActa=$row['IdRegistro'];
	mysqli_close($con); 
?>

<!DOCTYPE html><html lang="en">
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="../css/bootstrap.css" rel="stylesheet" />
<?php include "../php/navbar.php" ?>
<div class="container">
<div class="row"></div>
 <!-- /row -->
 </div>

 <!-- /container -->
<!--Encabezado del Acta-->
<div class="col-lg-12">
	<div class="col-xs-6">
		<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-6 text-right">
		<h2>Maquinas Fuera de Servicio</h2><br>
		<h4><?php echo date("d/m/Y"); ?><br></h4>
		<h4><small></small></h4> 
	</div>
</div>



<div class="col-lg-12">
<!-- / Tabla  -->
<form class="form-inline" form action="agregarmaquina.php" method="get">
	<input type="hidden" class="form-control input-md" id="IdActa" name="IdActa" value="<?php echo $IdActa; ?>">
	<input type="Number" name="busqueda" class="form-control input-md" placeholder="No Maquina"required="">
	<input type="submit" Value="Agregar" class="btn-primary">
</form>
<br>
<?php 
  include "../php/conexion.php"; 


  $query = "SELECT * FROM tbl_fueradeservicio ORDER BY `Desde` ";
  $resultado=$con->query($query);
  $query = mysqli_query ($con, $query) or die ("Fallo en la consulta". mysqli_error ($con));
  $nfilas = mysqli_num_rows ($query);

  if ($nfilas > 0){
		print "<table class=table table-bordered>
				<thead>
					<tr>
					<th>Casino</th>
					<th>Maquina</th>
					<th>Modelo</th>
					<th>Fabricante</th>
					<th>En Servicio</th>
					<th>Desde</th>
					<th># Solicitud</th>
					<th>Motivo</th>
					<th>Acciones</th>
					<th>Dias FS</th>
					</tr>
				</thead>";
 	for ($i=0; $i<$nfilas; $i++){
          $resultado = mysqli_fetch_array ($query);
        print "  
			<tbody>
				<tr>
				<td>".$resultado['Casino'] ."</td>
				<td>". $resultado['Maquina'] ."</a></td>
				<td>". $resultado['Modelo'] ."</td>
				<td>". $resultado['Fabricante'] ."</td>
				<td>". $resultado['En Servicio'] ."</td>
				<td>". $resultado['Desde'] ."</td>
				<td>". $resultado['Solicitud'] ."</td>
				<td>". $resultado['Motivo'] ."</td>
				<td>". $resultado['Acciones'] ."</td>
				<td>". $resultado['Motivo'] ."</td>
			
				
			</tbody>";
	}
	print"</table>";
}
print"
<!-- / fin de tabla  -->
<br>

 <a name=acta href=reporte.php?IdActa=$IdActa><img src=../img/print.png width=40 height=40 />
	

</div>"
?>