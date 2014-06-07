$(document).ready(function() {
	// Ir a detalles de paciente
	$("#ver-info-paciente").click(function() {
		$("#formulario-solicitud-quirofano").addClass("hidden");
		$("#formulario-solicitud-paciente").removeClass("hidden");
		$("#titulo-detalles-operacion").html("Detalles de Operación - Paciente");
	});

	// Volver a detalles de quirofano
	$("#volver-info-quirofano").click(function() {
		$("#formulario-solicitud-paciente").addClass("hidden");
		$("#formulario-solicitud-quirofano").removeClass("hidden");
		$("#titulo-detalles-operacion").html("Detalles de Operación - Quirófano");
	});

	// Ir a detalles de honorarios
	$("#ver-info-honorarios").click(function() {
		$("#formulario-solicitud-paciente").addClass("hidden");
		$("#formulario-solicitud-honorarios").removeClass("hidden");
		$("#titulo-detalles-operacion").html("Detalles de Operación - Participantes");
	});

	// Volver a detalles de paciente
	$("#volver-info-paciente").click(function() {
		$("#formulario-solicitud-honorarios").addClass("hidden");
		$("#formulario-solicitud-paciente").removeClass("hidden");
		$("#titulo-detalles-operacion").html("Detalles de Operación - Paciente");
	});
});