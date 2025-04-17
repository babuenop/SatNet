<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<head>
		<title>Crear Material</title>
		<link rel="stylesheet" type="text/css" href="../css/bootstrap.css">
		<?php include "php/navbar.php"; ?>
	</head>

<body>
	<div class="col-lg-12">

		<div class="col-xs-6">
			<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>

		</div>

		<div class="col-xs-6 text-right">
			<h2>Crear Material</h2>
		</div>
	</div>
</div>

<form class="form-horizontal" form action="php/CrearMaterial.php" method="POST">


		<!--Material-->
		<div class="form-group">

		  <label class="col-md-4 control-label">Material</label>  
		  <div class="col-md-4">
		  <input id="Material" name="Material" placeholder="No. Material" class="form-control input-md" required="" type="text" value=""></input>
		    
		  </div>
		</div>

		<!--Descripcion-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Descripcion</label>  
		  <div class="col-md-4">
		  <input id="Descripcion" name="Descripcion" placeholder="Descripcion Material" class="form-control input-md" required="" type="text" value="">  
		    
		  </div>
		</div>

		
		<!--Ubicacion-->
		<div class="form-group">
		   <label class="col-md-4 control-label">Ubicacion</label>  
		  <div class="col-md-4">               
		    <input id="Ubicacion" name="Ubicacion" placeholder="Ubicacion" class="form-control input-md" required="" type="text" value="">
		  </div>
		</div>

		<!--Categoria-->
		<div class="form-group">
		 <label class="col-md-4 control-label">Categoria</label>  
		  <div class="col-md-4">                
		    <select id="Categoria" name="Categoria" placeholder="Categoria" class="form-control input-md" required="" type="text" value="">
		     <?php include "../values/Categorias.php"; ?>
		     </select>


		  </div>
		</div>


		<!--Partnumber-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Partnumber</label>  
		  <div class="col-md-4">                
		    <input id="Partnumber" name="Partnumber" placeholder="Partnumber" class="form-control input-md" required="" type="text" value="">
		  </div>
		</div>

		<!--Categoria-->
		<div class="form-group">
		 <label class="col-md-4 control-label">Proveedor</label>  
		  <div class="col-md-4">                
		    <input id="Proveedor" name="Proveedor" placeholder="Proveedor" class="form-control input-md" required="" type="text" value="">
		  </div>
		</div>

		<!-- Boton Crear Material -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Crear"></label>
		  <div class="col-md-8">
		    <button id="Crear" name="Crear" class="btn btn-primary">Crear</button>
		  </div>
		</div>

</form>
<!-- / fin de Formulario -->

</div>


</body>
</html>



