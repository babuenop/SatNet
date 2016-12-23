<?php
require_once ('../lib/pdf/mpdf.php');


	require('../php/conexion.php');
	
	$IdActa='133';
	$Codigo=$_GET['busqueda'];

	$sql="SELECT * FROM `tbl_materiales` WHERE `Material` LIKE '$Codigo'";
	$sql1="SELECT * FROM `tbl_actas` WHERE `IdActa`=$IdActa";
	
	$resultado=$con->query($sql);
	$row=$resultado->fetch_assoc();
	$resultado1=$con->query($sql1);
	$row1=$resultado1->fetch_assoc();
	mysqli_close($con); 
	
$html = '

<div class="row">
	<div class="col-xs-2">
		<h1><a href=" "><img alt="" src="../img/logo.jpg" width="140" height="40" /></a></h1>
	</div>

	<div class="col-xs-8 text-right">
		<h3><small>Acta Entrega de Repuestos ';
		foreach ($resultado1 as $resultado1){
			$html.= ''.$resultado1['IdActa'].'';
$html .='</small></h3>
		<h4><small>Fecha ';
		
			$html.= ''.$resultado1['Fecha de Entrega'].'';

$html .='</small></h4>
	</div>
</div>

<div class="row">
	<div class="col-xs-5">
		<div class="panel panel-default" >
			<div class="panel-default">
				<div class="col-xs-5">
				<h5><small><b>Origen</b></small></h5>
				</div>
			</div>
			<div >
				<div class="col-md-6">
				<h5><small>	';
				$html.= ''.$resultado1['Origen'].'';
	
				$html.='</small></h5>
				<h5><small>	Remite: ';
				$html.= ''.$resultado1['Realizado Por'].'';
		
				$html.='</small></h5>
				</div>
			</div>			
		</div>
</div>

	<div class="col-xs-5 text-Left">
			<div class="panel panel-default" >
			<div class="panel-default">
				<div class="col-xs-5">
				<h5><small><b>Destino</b></small></h5>
				</div>
			</div>
			<div >
				<div class="col-md-6">
				<h5><small>	';
				$html.= ''.$resultado1['Destino'].''; 
		$html.='</small></h5>
				<h5><small>	Recibe: 
				';
				$html.= ''.$resultado1['Recibido Por'].'';
		}; 
		$html.='</small></h5>
				</div>
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
	</thead><tbody>
	';
		foreach ($resultado as $resultado){
			$html.= ''.$resultado['Codigo'].'';
			}
$html .='</tbody>
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

