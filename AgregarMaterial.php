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
<form class="form-inline" form action="php/AgregarMaterial.php" method="POST">

		<!-- Form Name -->

		<!--IdActa-->
		<div class="form-group">
			<input type="hidden" class="form-control input-md" id="IdActa" name="IdActa" value="<?php echo $IdActa; ?>">
		</div>	

		<!--Material-->
		<div class="form-group">
		  <label class="col">Material</label>  
		  <div class="col">
		  <input id="Material" name="Material" placeholder="No Material" class="form-control input-md" required="" type="text" value="" ></input>

		    
		  </div>
		</div>

		<!--Descripcion-->
		<div class="form-group">
		  <label class="col">Descripcion</label>  
		  <div class="col">
		  <input id="Descripcion" name="Descripcion" placeholder="Descripcion Material" class="form-control input-md" required="" type="text">
		    
		  </div>
		</div>

		<!--Proveedor-->
		<div class="form-group">
		  <label class="col" for="Proveedor">Proveedor</label>
		  <div class="col">                     
		    <input id="Proveedor" name="Proveedor" placeholder="Proveedor" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!--Estado-->
		<div class="form-group">
		  <label class="col" for="Proveedor">Estado</label>
		  <div class="col">                     
		    <input id="Estado" name="Estado" placeholder="Estado" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!--Cantidad-->
		<div class="form-group">
		  <label class="col" for="Cantidad">Cantidad</label>
		  <div class="col">                     
		    <input id="Cantidad" name="Cantidad" placeholder="Cantidad" class="form-control input-md" required="" type="number">
		  </div>
		</div>

		<!--Ingresado Por-->
		<div class="form-group">
		  <label class="col" for="IngresadoPor">Ingresado Por</label>
		  <div class="col">                     
		    <input id="IngresadoPor" name="IngresadoPor" placeholder="IngresadoPor" class="form-control input-md" required="" type="text">
		  </div>
		</div>

		<!-- Boton Agregar Material -->
		<div class="form-group">
		  <label class="col" for="Agregar"></label>
		  <div class="col">
		    <button id="Agregar" name="Agregar" class="btn btn-primary">Agregar</button>
		  </div>
		</div>
		</form>
<!-- / fin de Formulario -->

</div>