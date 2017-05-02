<?php
	error_reporting(0);

	require('php/conexion.php');
	
	$Material=$_GET['Material'];
	$sql="SELECT * FROM `tbl_Materiales` WHERE `Material`LIKE '$Material'";
		
	$resultado=$con->query($sql);
	$row=$resultado->fetch_assoc();
	mysqli_close($con); 
?>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<head>
		<title>Buscar / Editar Material</title>
		<link rel="stylesheet" type="text/css" href="../css/bootstrap.css">
		<?php include "php/navbar.php"; ?>
	</head>

<body>
	<div class="col-lg-12">

		<div class="col-xs-6">
			<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>

		</div>

		<div class="col-xs-6 text-right">
			<h2>Editar Material</h2>
		</div>
	</div>
</div>


<form class="form-inline col-lg-12" form action="EditaMaterial.php" method="get">
	<label class="col-md-4 control-label"></label>  
	<input id="Material" name="Material" class="form-control input-md" required="" type="text" autocomplete="off"></input>
	<input type="submit" Value="Buscar" class="btn-primary">
</form>

<form class="form-horizontal" form action="php/EditarMaterial.php" method="POST">

		<!--Material-->
		<div class="form-group">

		  <label class="col-md-4 control-label">Material</label>  
		  <div class="col-md-4">
		  <input id="Material" name="Material" placeholder="" class="form-control input-md" required="" type="text" value="<?php echo $row['Material']; ?>" readonly></input>
		    
		  </div>
		</div>

		<!--Descripcion-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Descripcion</label>  
		  <div class="col-md-4">
		  <input id="Descripcion" name="Descripcion" placeholder="Descripcion Material" class="form-control input-md" required="" type="text" value="<?php echo $row['Descripcion']; ?>">  
		    
		  </div>
		</div>

		
		<!--Ubicacion-->
		<div class="form-group">
		   <label class="col-md-4 control-label">Ubicacion</label>  
		  <div class="col-md-4">               
		    <input id="Ubicacion" name="Ubicacion" placeholder="Ubicacion" class="form-control input-md" required="" type="text"value="<?php echo $row['Ubicacion']; ?>">
		  </div>
		</div>

		<!--Categoria-->
		<div class="form-group">
		 <label class="col-md-4 control-label">Categoria</label>  
		  <div class="col-md-4">                
		   		    
		    <select id="Categoria" name="Categoria" placeholder="Categoria" class="form-control input-md" required="" type="text">
		      <option selected><?php echo $row['Categoria']; ?></option>
		        <?php include "../values/Categorias.php"; ?>
		     </select>     
		  </div>
		</div>

		<!--Partnumber-->
		<div class="form-group">
		  <label class="col-md-4 control-label">Partnumber</label>  
		  <div class="col-md-4">                
		    <input id="Partnumber" name="Partnumber" placeholder="Partnumber" class="form-control input-md" required="" type="text" value="<?php echo $row['Partnumber']; ?>">
		  </div>
		</div>



		<!--Proveedor-->
		<div class="form-group">
		 <label class="col-md-4 control-label">Proveedor</label>  
		  <div class="col-md-4">                
		    <input id="Proveedor" name="Proveedor" placeholder="Proveedor" class="form-control input-md" required="" type="text" value="<?php echo $row['Proveedor']; ?>">
		  </div>
		</div>

		<!--Ultima Modificacion-->
		<div class="form-group">
		 <label class="col-md-4 control-label">Modificado el</label>  
		  <div class="col-md-4">                
		    <div class='input-group date' id='datetimepicker3'>
                    <input type='text' class="form-control" value="<?php echo date("d/m/Y h:i:s"); ?>" readonly />
                    <span class="input-group-addon">
                        <span class="glyphicon glyphicon-time"></span>
                    </span>
                </div>
		  </div>

		</div>



		<!-- Boton Editar Material -->
		<div class="form-group">
		  <label class="col-md-4 control-label" for="Editar"></label>
		  <div class="col-md-8">
		    <button id="Editar" name="Editar" class="btn btn-primary">Editar</button>
		  </div>
		</div>
</form>


<!-- / fin de Formulario -->

</div>


</body>
</html>



