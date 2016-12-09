<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
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

		<!-- Form Name -->

		<!--Fecha-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Fecha</label>  
		  <div class="col-md-4">
		  <input id="Fecha" name="Fecha" placeholder="Acta Realizada Por" class="form-control input-md" required="" type="text" value="<?php echo date("d/m/Y"); ?>" readonly></input>
		    
		  </div>
		</div>

		<!-- RealizadoPor-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Creada Por</label>  
		  <div class="col-md-4">
		  <input id="RealizadoPor" name="RealizadoPor" placeholder="Creada Por" class="form-control input-md" required="" type="text">
		    
		  </div>
		</div>

		<!-- Observaciones -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Observaciones">Observaciones</label>
		  <div class="col-md-4">                     
		    <textarea class="form-control" id="Observaciones" name="Observaciones" required=""></textarea>
		  </div>
		</div>

		<!-- Crear -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Crear"></label>
		  <div class="col-md-8">
		    <button id="Crear" name="Crear" class="btn btn-primary">Crear</button>
		  </div>
		</div>
		</form>
	</body>
</html>


