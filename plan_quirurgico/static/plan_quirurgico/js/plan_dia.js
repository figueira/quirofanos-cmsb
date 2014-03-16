$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");
	
	// Mostrar instrucciones al usuario para seleccionar bloque de horas para solicitar quirofano
	$('#aceptar-duracion').click(function(){
		$('#btn-solicitar-quirofano').remove();
		$('#duracion-operacion').removeClass("hidden");
	});
});