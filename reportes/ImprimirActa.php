<?php
require_once ('../lib/pdf/mpdf.php');


	require('../php/conexion.php');
	
	$IdActa=$_GET['IdActa'];

	$sql="SELECT * FROM `tbl_actas` WHERE IdActa=$IdActa";
	
	$resultado=$con->query($sql);
	$row=$resultado->fetch_assoc();
	
	$query = "SELECT * FROM tbl_actasDetalle WHERE IdActa=$IdActa";
  	$resultado1=$con->query($query);
  	$query = mysqli_query ($con, $query) or die ("Fallo en la consulta". mysqli_error ($con));
 	$nfilas = mysqli_num_rows ($query);


	mysqli_close($con); 
	
$html = '
<div class="col-lg-12">
<div class="row">
	<div class="col-xs-2">
		<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-8 text-right">
		<h3><small>Acta Entrega de Repuestos';
		foreach ($resultado as $resultado){
			$html.= ''.$resultado['IdActa'].'';
$html .='</small></h3>
		<h4><small>Fecha ';
		
			$html.= ''.$resultado['Fecha de Entrega'].'';

$html .='</small></h4>
	</div>
</div>

<div class="row">
	<div class="col-xs-5">
		<div class="" >
			<div class="panel-default">
				<div class="col-xs-5">
				<h5><small><b>Origen</b></small></h5>
				</div>
			</div>
			<div >
				<div class="col-md-6">
				<h5><small>	';
				$html.= ''.$resultado['Origen'].'';
	
				$html.='</small></h5>
				<h5><small>	Remite: ';
				$html.= ''.$resultado['Realizado Por'].'';
		
				$html.='</small></h5>
				</div>
			</div>			
		</div>
</div>

	<div class="col-xs-5 text-Left">
			<div class="" >
			<div class="panel-default">
				<div class="col-xs-5">
				<h5><small><b>Destino</b></small></h5>
				</div>
			</div>
			<div >
				<div class="col-md-6">
				<h5><small>	';
				$html.= ''.$resultado['Destino'].''; 
		$html.='</small></h5>
				<h5><small>	Recibe: 
				';
				$html.= ''.$resultado['Recibido Por'].'';
		}; 
		$html.='</small></h5>
				</div>
			</div>			
		</div>
	</div>

</div>


<!-- / fin de sección de datos del Cliente  -->
<br>

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
			<h6>Proveedor</h6>
		</th>
		<th>
			<h6>Estado</h6>
		</th>
		<th>
			<h6>Cantidad</h6>
		</th>
		<th>
			<h6>Revisado por </h6>
		</th>
		</tr>';



 if ($nfilas > 0){
 	$html.='';
 	for ($i=0; $i<$nfilas; $i++){
          $resultado1 = mysqli_fetch_array ($query);
        $html.='  
			<tbody>
				<tr>
				<td><h6><small> '.$resultado1['Codigo'] .' </small><h6></td>
				<td><h6><small> '. $resultado1['Descripcion'] .' </small><h6></a></td>
				<td><h6><small> '. $resultado1['Proveedor'] .' </small><h6></td>
				<td><h6><small> '. $resultado1['Estado'] .' </small><h6></td>
				<td><h6><small><center> '. $resultado1['Cantidad'] .' </small><h6></td>
				<td><h6><small> '. $resultado1['Revisado Por'] .' </small><h6></td>
				
			</tbody>';
	}}
	$html.='</table>

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

