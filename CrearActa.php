<?php
  include "php/conexion.php";
  $query= "SELECT * FROM `tbl_actas`";
  $resultado=$con->query($query);
?>

<html>
	<head>
		<title>Crear Acta</title>
		<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
		<?php include "php/navbar.php"; ?>
	</head>
	<body>

		<div class="col-lg-12">
			<div class="col-xs-6">
				<h1><a href=" "><img alt="" src="img/logo.jpg" width="140" height="40" /></a></h1>
			</div>

			<div class="col-xs-6 text-right">
				<h2>Crear</h2>

			</div>
		</div>

		<form class="form-horizontal" form action="php/crearActa.php" method="POST">
		<fieldset>

		<!-- Form Name -->
		<legend></legend>

		<!-- Fecha-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Fecha</label>  
		  <div class="col-md-1">
		  <input id="Fecha" type="Fecha" name="Fecha" class="form-control input-md" value="<?php echo date("d/m/Y"); ?>"  disabled>
		    
		  </div>
		</div>        

		<!-- Realizado Por-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Realizado Por</label>  
		  <div class="col-md-4">
		  <input id="RealizadoPor" name="RealizadoPor" placeholder="Acta Realizada Por" class="form-control input-md" required="" type="text">
		    
		  </div>
		</div>

		<!-- Observaciones -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Observaciones">Observaciones</label>
		  <div class="col-md-4">                     
		    <textarea class="form-control" id="Observaciones" name="Observaciones" required=""></textarea>
		  </div>
		</div>

		<!-- Button -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Crear"></label>
		  <div class="col-md-8">
		    <button id="Crear" name="Crear" class="btn btn-success">Crear</button>
		  </div>
		</div>

		</fieldset>
		</form>
	</body>
</html>


