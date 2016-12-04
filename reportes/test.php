<?php
require_once ('../lib/pdf/mpdf.php');

$html = '

<div class="row">
	<div class="col-xs-2">
		<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-8 text-right">
		<h3><small>Canasta de Compras</small></h3>
		<h4><small>Fecha: </small></h4>
	</div>
</div>

<div class="row">
	<div class="col-xs-5">
		<div class="panel panel-default" >
			<div >
				<h5><small>	Solicitado Por : </small></h5>
				<h5><small>	Solicitado Por : </small></h5>
			</div>			
		</div>
</div>
	<div class="col-xs-5 text-Left">
		<div class="panel panel-default">
			<div>
				<h5><small>Para : Nombre del Cliente<small></h5>
				<h5><small>Para : Nombre del Cliente<small></h5>
			</div>
		</div>
	</div>
</div>


<!-- / fin de sección de datos del Cliente  -->


<table class="table table-bordered">
	<thead>
		<tr>
		<th>
			<h6>Material</h6>
		</th>
		<th>
			<h6>Texto Breve</h6>
		</th>
		<th>
			<h6>Cantidad</h6>
		</th>
		<th>
			<h6>Estado</h6>
		</th>
		<th>
			<h6>Origen</h6>
		</th>
		</tr>
	</thead>

	<tbody>
		<tr>
		<td><h6>Artículo</h6></td>
		<td><h6>Esta es la descripcion del articulo </h6></td>
		<td><h6>Artículo</h6></td>
		<td><h6>Artículo</h6></td>
		<td><h6>Artículo</h6></td>
		</tr>
		<tr>
	</tbody>
</table>

<h6>Observaciones</h6>
	<div class="panel panel-default">
	   	<h5><small><small></h5>   
	    </div>
    </div>

	
'
;

$mpdf=new mPDF('A4');
$css = file_get_contents('../css/bootstrap.css');
$mpdf->WriteHTML($css, 1);
$mpdf->WriteHTML($html);
$mpdf->Output('reporte.pdf','I');
?>

