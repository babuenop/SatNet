<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
  <head>
    <title>Inventario Memorias</title>
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.css">
    <?php include "php/navbar.php"; ?>
  </head>

<body>

<div class="container">

  <form class="well form-horizontal" action=" " method="post" id="contact_form">
    <fieldset>

      <!-- Form Name -->
      <legend>Formulario de Creacion de Memorias</legend>
    
      <!-- Text input-->

       <!-- Text input-->

      <div class="form-group">
        <label class="col-md-4 control-label">Proveedor</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-list-alt"></i></span>
            <select name="Proveedor" placeholder="Proveedor" class="form-control" type="text">
            <?php include "../values/Proveedores.php"; ?>
            </select>
          </div>
        </div>
      </div>

       <!-- Text input-->
      <div class="form-group">
        <label class="col-md-4 control-label">Tipo</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-list-alt"></i></span>
            <select name="Tipo" placeholder="Tipo" class="form-control" type="text">
            <?php include "../values/TipoMemorias.php"; ?>
            </select>
          </div>
        </div>
      </div>

      <div class="form-group">
        <label class="col-md-4 control-label">Descripcion</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon glyphicon-erase"></i></span>
            <input name="Descripcion" placeholder="Descripcion" class="form-control" type="text" onKeyUp="this.value=this.value.toUpperCase();" autocomplete="off">
          </div>
        </div>
      </div>  

      <!-- Text input-->

       <!-- Text input-->
      <div class="form-group">
        <label class="col-md-4 control-label">Origen</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-list-alt"></i></span>
            <select name="Origen" placeholder="Origen" class="form-control" type="text">
            <?php include "../values/Ubicaciones.php"; ?>
            <input name="RefOrigen" placeholder="Referencia Adicional Origen" class="form-control" type="text" autocomplete="off">
            </select>
          </div>
        </div>
      </div>

      <!-- Text input-->

      <div class="form-group">
        <label class="col-md-4 control-label">Ubicacion Actual</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-list-alt"></i></span>
            <select name="UbicacionActual" placeholder="Ubicacion Actual" class="form-control" type="text">
            <?php include "../values/Ubicaciones.php"; ?>
            <input name="RefUbicacionActual" placeholder="Referencia Adicional Ubicacion" class="form-control" type="text" autocomplete="off" >
            </select>
          </div>
        </div>
      </div>

      <!-- Text input-->

      <div class="form-group">
        <label class="col-md-4 control-label">IngresadoPor</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
            <input name="IngresadoPor" placeholder="IngresadoPor" class="form-control" type="text" autocomplete="off" onKeyUp="this.value=this.value.toUpperCase();">
          </div>
        </div>
      </div> 

      <!-- Text area -->

      <div class="form-group">
        <label class="col-md-4 control-label">Observaciones</label>
        <div class="col-md-4 inputGroupContainer">
          <div class="input-group">
            <span class="input-group-addon"><i class="glyphicon glyphicon-pencil"></i></span>
            <textarea class="form-control" name="comment" placeholder="Observaciones" onKeyUp="this.value=this.value.toUpperCase();"></textarea>
          </div>
        </div>
      </div>

      <!-- Button -->
      <div class="form-group">
        <label class="col-md-4 control-label"></label>
        <div class="col-md-4">
          <button type="submit" class="btn btn-primary">Agregar <span class="glyphicon glyphicon-send"></span></button>
        </div>
      </div>

    </fieldset>
  </form>
</div>
</div>
<!-- /.container -->

</body>
</html>

