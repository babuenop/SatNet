<?php  

require_once('lib/pdf/mpdf.php');

$mpdf= new mpdf('c','A4-L');
$mpdf -> writeHTML('<div>Hola</div>');
$mpdf ->output('reporte.pdf', 'I');

?>
