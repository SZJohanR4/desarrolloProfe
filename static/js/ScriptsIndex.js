$(document).ready(function(){
	$('#contenedor, #formLogin').hide();
	$('#botonIngresar').click(function () {
        $('#contenedor, #formLogin').fadeIn(1000);
    });
    $('#contenedor').click(function () {
        $('#contenedor, #formLogin').fadeOut(1000);
    });

    if ($('#advertencia').show()) {
    	$('#advertencia').fadeOut(2000);
    }
   /* $('#cerrar').click(function(){
    	$('#advertencia').fadeOut(1000);
    });*/
});