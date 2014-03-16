$(document).ready(function() {
	// Ir a formulario de paciente
	$("#ver-info-paciente").click(function() {
		$("#formulario-solicitud-quirofano").addClass("hidden");
		$("#formulario-solicitud-paciente").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Paciente");
	});

	// Volver a formulario de quirofano
	$("#volver-info-quirofano").click(function() {
		$("#formulario-solicitud-paciente").addClass("hidden");
		$("#formulario-solicitud-quirofano").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Quirófano");
	});

	// Ir a formulario de honorarios
	$("#ver-info-honorarios").click(function() {
		$("#formulario-solicitud-paciente").addClass("hidden");
		$("#formulario-solicitud-honorarios").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Participantes");
	});

	// Volver a formulario de paciente
	$("#volver-info-paciente").click(function() {
		$("#formulario-solicitud-honorarios").addClass("hidden");
		$("#formulario-solicitud-paciente").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Paciente");
	});

	// Mostrar o no mostrar razon de riesgo
	var nivel = $("input[name=riesgo]");
	nivel.change(function(){
		nivel_seleccionado = $("input[name=riesgo]:checked");
		if (nivel_seleccionado.val() == "malo")
			$("#razon-riesgo").removeClass("hidden");
		else {								
			$("#razon-riesgo-input").val("");
			$("#razon-riesgo").addClass("hidden");			
		}
	});

	// Mostrar o no mostrar aseguradoras
	var forma_pago = $("input[name=forma-pago]");
	forma_pago.change(function(){
		seguro = $("input[name=forma-pago]:checked");
		if (seguro.val() == "seguro")
			$("#seguros").removeClass("hidden");
		else {										
			$("#seguros").addClass("hidden");			
		}
	});

	// Mostrar o no mostrar habitacion de paciente
	var hospitalizado = $("input[name=paciente-hospitalizado]");
	hospitalizado.change(function(){
		$("#habitacion").toggleClass("hidden");
	});

	// Mostrar o no mostrar carnet impres de paciente
	var impres = $("input[name=paciente-impres]");
	impres.change(function(){
		$("input[name=carnet-impres]").val("");
		$("#carnet-impres").toggleClass("hidden");
	});

	// Mostrar o no mostrar numero inscripcion paciente
	var paciente_medico = $("input[name=paciente-medico]");
	paciente_medico.change(function(){
		$("input[name=numero-inscripcion-medico]").val("");
		$("#numero-inscripcion-medico").toggleClass("hidden");
	});

	// Mostrar o no mostrar paciente pariente de medico
	var paciente_pariente_medico = $("input[name=paciente-pariente-medico]");
	paciente_pariente_medico.change(function(){
		$(".input-medico-pariente").val("");
		$("#medico-pariente").toggleClass("hidden");
	});
});