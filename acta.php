

<!DOCTYPE html><html lang="en">
<meta charset="utf-8" />
<link href="css/bootstrap.css" rel="stylesheet" />
</pre>
<div class="container">
<div class="row"></div>
 <!-- /row --></div>
<pre>
 
 <!-- /container -->

<link href="css/bootstrap.css" rel="stylesheet">


</pre>
<div class="col-lg-12">
	<div class="col-xs-6">
		<h1><a href=" "><img alt="" src="img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-6 text-right">
		<h2>Acta de Salida de Almacen</h2>
		<h4><small>Acta #001</small></h4>
		<h4><small>Fecha: <?php echo date("d/m/Y h:s"); ?></small></h4>
	</div>
</div>

<div class="col-lg-12">
	<div class="row">
		<div class="col-xs-5">
			<div class="panel panel-default">
				<div class="panel-heading">
					<h4>Solicitado Por : </h4>
				</div>
				<div class="panel-body">Dirección detalles más detalles
				</div>
			</div>
		</div>

		<div class="col-xs-5 col-xs-offset-2 text-right">
			<div class="panel panel-default">
				<div class="panel-heading">
					<h4>Para : Nombre del Cliente</h4>
				</div>
				<div class="panel-body">Dirección
				detalles
				más detalles</div>
			</div>
		</div>
	</div>
</div>

<!-- / fin de sección de datos del Cliente  -->
<div class="col-lg-12">
<table class="table table-bordered">
	<thead>
		<tr>
		<th>
			<h5>Material</h5>
		</th>
		<th>
			<h5>Texto Breve</h5>
		</th>
		<th>
			<h5>Cantidad</h5>
		</th>
		<th>
			<h5>Estado</h5>
		</th>
		<th>
			<h5>Origen</h5>
		</th>
		</tr>
	</thead>

	<tbody>
		<tr>
		<td>Artículo</td>
		<td><a href="#"> Título de su artículo aquí </a></td>
		<td class="text-right">-</td>
		<td class="text-right">200.00 €</td>
		<td class="text-right">200.00 €</td>
		</tr>
		<tr>
	</tbody>
</table>

	<div class="box">
		<h5>Observaciones</h5>
	      <div id="div-1" class="textarea">
	         <textarea id="wysihtml5" class="form-control" rows="5"></textarea>
	        <div class="form-actions">
	         <br><input type="submit" value="Submit" class="btn btn-primary"></br>
	      	</div>
	      </div>
	</div>
</div>