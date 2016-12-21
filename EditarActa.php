<?php
	require('php/conexion.php');
	$sql="SELECT * FROM `tbl_actas` ORDER BY `IdActa` DESC limit 1";
	$resultado=$con->query($sql);
	$row=$resultado->fetch_assoc();
	$IdActa=$row['IdActa'];
	mysqli_close($con); 
?>

<!DOCTYPE html><html lang="en">
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="css/bootstrap.css" rel="stylesheet" />
<?php include "php/navbar.php" ?>
<div class="container">
<div class="row"></div>
 <!-- /row -->
 </div>

 <!-- /container -->
<!--Encabezado del Acta-->
<div class="col-lg-12">
	<div class="col-xs-6">
		<h1><a href=" "><img alt="" src="img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-6 text-right">
		<h2>Acta Entrega de Repuestos</h2>
		<h4>Acta No. <?php echo $IdActa; ?><br></h4>
		<h4><?php echo $row['Fecha de Entrega']; ?><br></h4>
		<h4><small></small></h4>
	</div>
</div>


<!--Datos Generales-->
<div class="col-lg-12">
	<div class="row">
		<div class="col-xs-5">
			<div class="panel panel-default">
				<div class="panel-heading">
					<h4>Origen</h4>
				</div>
				<div class="panel-body">
				<b><?php echo $row['Origen'] ?></b><br>
				Remite:	<?php echo $row['Realizado Por'] ?><br>
				</div>
			</div>
		</div>

		<div class="col-xs-5 col-xs-offset-2">
			<div class="panel panel-default">
				<div class="panel-heading">
					<h4>Destino</h4>
				</div>
				<div class="panel-body">
				<b><?php echo $row['Destino'] ?></b><br>
				Recibe:	<?php echo $row['Recibido Por'] ?><br>
				</div>
			</div>
		</div>
	</div>
</div>

<!-- / fin de sección de datos Generales  -->
<div class="col-lg-12">
<!-- / Tabla  -->
<form class="form-inline" form action="agregarmaterial.php" method="get">
	<input type="hidden" class="form-control input-md" id="IdActa" name="IdActa" value="<?php echo $IdActa; ?>">
	<input type="text" name="busqueda" class="form-control input-md" required="">
	<input type="submit" Value="Buscar" class="btn-primary">
</form>
<?php 
  include "php/conexion.php"; 


  $query = "SELECT * FROM tbl_actasDetalle WHERE IdActa=$IdActa";
  $resultado=$con->query($query);
  $query = mysqli_query ($con, $query) or die ("Fallo en la consulta". mysqli_error ($con));
  $nfilas = mysqli_num_rows ($query);

  if ($nfilas > 0){
		print "<table class=table table-bordered>
				<thead>
					<tr>
					<th>Codigo</th>
					<th>Descripcion</h5></th>
					<th>Proveedor</h5></th>
					<th>Estado</h5></th>
					<th>Cantidad</h5></th>
					<th>Revisado Por</th>
					<th>Editar</th>
					<th>Borrar</th>
					</tr>
				</thead>";
 	for ($i=0; $i<$nfilas; $i++){
          $resultado = mysqli_fetch_array ($query);
        print "  
			<tbody>
				<tr>
				<td>".$resultado['Codigo'] ."</td>
				<td>". $resultado['Descripcion'] ."</a></td>
				<td>". $resultado['Proveedor'] ."</td>
				<td>". $resultado['Estado'] ."</td>
				<td>". $resultado['Cantidad'] ."</td>
				<td>". $resultado['Revisado Por'] ."</td>
				<td><a href=editar.php?IdActa=".$IdActa."&Codigo=".$resultado['Codigo'] ."><img src=img/edit.png width=25 height=25 /></a>
				<td><a href=php/BorrarMaterial.php?IdActa=".$IdActa."&Codigo=".$resultado['Codigo'] ."><img src=img/del.png width=25 height=25 /></a>
				
			</tbody>";
	}
	print"</table>";
}?>

<!-- / fin de tabla  -->
<br>

 <a href="reportes/imprimiracta.php"><img src=img/print.png width=40 height=40 />
	

</div>