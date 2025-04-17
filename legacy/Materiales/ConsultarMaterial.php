<HTML LANG="es">
<div>
<head>
	<title>Consultar Material</title>
	
	<link rel="stylesheet" type="text/css" href="../css/bootstrap.css">
	<link rel="stylesheet" type="text/css" href="../js/jquery.dataTables.min.css">
	<?php include "php/navbar.php"; ?>
</head>
</div>
<head>
	<script type="text/javascript" language="javascript" src="../js/jquery-3.1.1.js"></script>
	<script type="text/javascript" language="javascript" src="../js/jquery-3.1.1.min.js"></script>
	<script type="text/javascript" language="javascript" src="../js/jquery.dataTables.min.js"></script>
</head>


<body>
<h1>Consultar Material</h1>
    <script type="text/javascript">
    
    $(document).ready(function(){
        $('#grid').DataTable( {
            "lengthMenu":[10,20,50,100],
            "order": [[0,"asc"]],
            "language": {
                "lengthMenu": "Mostrar _MENU_ registros por pagina",
                "zeroRecords": "No existen resultados en su busqueda",
                "info": "Mostrando pagina _PAGE_ de _PAGES_ ",
                "infoEmpty": "No hay registros disponibles",
                "infoFiltered": "(Buscado entre _MAX_ registros en total)",
                "search": "Buscar: ",
                "paginate": {
                    "first": "Primero",
                    "last": "Ultimo",
                    "next": "Siguiente",
                    "previous": "Anterior"
                },
            }
        });
        
        $("*").css("font-family", "arial").css('font-size', '12px');
    });
    </script>
    

<?PHP
$conexion = mysqli_connect ("localhost","root", "")
or die ("No se puede conectar con el servidor");

mysqli_select_db ($conexion,"satnet")
or die ("No se puede seleccionar la base de datos");

$instruccion = "CALL sp_listarmateriales(); ";
$consulta = mysqli_query ($conexion, $instruccion)
	or die ("Fallo en la consulta". mysqli_error ($conexion));
	
$nfilas = mysqli_num_rows ($consulta);

if ($nfilas > 0){
	print ("<TABLE id='grid' class='display' 'cellspacing='0'>\n");
	print ("<THEAD>");
        print ("<TR>\n");            
	      	print ("<TH>Material</TH>\n");
			print ("<TH>Descripcion</TH>\n");
			print ("<TH>Ubicacion</TH>\n");
			print ("<TH>Partnumber</TH>\n");
			print ("<TH>Proveedor</TH>\n");
			print ("<TH>Categoria</TH>\n");
			print ("<TH>Editar</TH>\n");
			// print ("<TH>Borrar</TH>\n");
		print ("</TR>\n");
        print ("</THEAD>");
        print ("<TBODY>");
	
	for ($i=0; $i<$nfilas; $i++){
		$resultado = mysqli_fetch_array ($consulta);
	print ("<TR>\n");
	print ("<TD>" . $resultado["Material"] .	"</TD>\n");
	print ("<TD>" . $resultado['Descripcion'] .	"</TD>\n");
	print ("<TD>" . $resultado['Ubicacion'] .	"</TD>\n");
	print ("<TD>" . $resultado['Partnumber'] .	"</TD>\n");
	print ("<TD>" . $resultado['Proveedor'] .	"</TD>\n");
	print ("<TD>" . $resultado['Categoria'] .	"</TD>\n");
	print ("<TD><a href=EditaMaterial.php?Material=". $resultado["Material"] ."><button type='button' class='btn btn-default'>Editar</button></a></TD>\n");
	// print ("<TD><a href=editamat.php?IdActa=". $resultado['Material'] ."><button type='button' class='btn btn-default'>Borrar</button></a></TD>\n");
	
	print ("</TR>\n");
       
	}
         print ("</TBODY>");
	print ("</TABLE>\n");
	}
	else{
		print ("No hay materiales");
	}
	mysqli_close ($conexion);
	?>
	</BODY>
	</HTML>