$(document).ready(function(){
	$('#contenedor, #contenedorAgregarEstudiantes').hide();
	$('#crearProyecto').hide();
	$('#botonAgregarEstudiantes').click(function () {
        $('#contenedor, #contenedorAgregarEstudiantes').fadeIn(1000);
    });
    $('#contenedor').click(function () {
        $('#contenedor, #contenedorAgregarEstudiantes').fadeOut(1000);
    });
    $('#botonAgregar').click(function () {
        $('#contenedor, #contenedorAgregarEstudiantes').fadeOut(1000);
        $('#crearProyecto').show();
        $('#botonAgregarEstudiantes').hide();
    });
});