$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");

	// Cambio de estado de operacion
	$(".btn-cambio-estado").click(function() {
		$('#id-intervencion').val($(this).val());
	});

	$(".btn-estado").click(function() {
		$('#estado-intervencion').val($(this).val());
		$('#formulario-cambio-estado-intervencion').submit();
	});

});
