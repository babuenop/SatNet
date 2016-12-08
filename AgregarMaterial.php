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
					<h4>Datos Generales Origen</h4>
				</div>
				<div class="panel-body">
				Realizado por:	<?php echo $row['Realizado Por'] ?><br>
				Aprobado por:	<?php echo $row['Realizado Por'] ?><br>
				</div>
			</div>
		</div>

		<div class="col-xs-5 col-xs-offset-2">
			<div class="panel panel-default">
				<div class="panel-heading">
					<h4>Datos Generales Destino</h4>
				</div>
				<div class="panel-body">
				Entregado a:	<?php echo $row['Realizado Por'] ?><br>
				Recibido por:	<?php echo $row['Realizado Por'] ?><br>
				</div>
			</div>
		</div>
	</div>
</div>

<!-- / fin de sección de datos Generales  -->
<div class="col-lg-12">
<!-- / Formulario  -->
<form class="form-horizontal" form action="php/AgregarMaterial.php" method="POST">

		<!-- Form Name -->

		<!--Material-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Material</label>  
		  <div class="col-md-4">
		  <input id="Material" name="Material" placeholder="No Material" class="form-control input-md" required="" type="text" value="" ></input>
		    
		  </div>
		</div>

		<!--Descripcion-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Descripcion</label>  
		  <div class="col-md-4">
		  <input id="Descripcion" name="Descripcion" placeholder="Descripcion Material" class="form-control input-md" required="" type="text">
		    
		  </div>
		</div>

		<!--Proveedor-->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Proveedor">Proveedor</label>
		  <div class="col-md-4">                     
		    <input id="Proveedor" name="Proveedor" placeholder="Proveedor" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!--Estado-->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Proveedor">Proveedor</label>
		  <div class="col-md-4">                     
		    <input id="Proveedor" name="Proveedor" placeholder="Proveedor" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!--Cantidad-->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Cantidad">Cantidad</label>
		  <div class="col-md-4">                     
		    <input id="Cantidad" name="Cantidad" placeholder="Cantidad" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!--Ingresado Por-->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="IngresadoPor">Ingresado Por</label>
		  <div class="col-md-4">                     
		    <input id="IngresadoPor" name="IngresadoPor" placeholder="IngresadoPor" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!-- Boton Agregar Material -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Agregar"></label>
		  <div class="col-md-8">
		    <button id="Agregar" name="Agregar" class="btn btn-primary">Agregar</button>
		  </div>
		</div>
		</form>
<!-- / fin de Formulario -->

</div>