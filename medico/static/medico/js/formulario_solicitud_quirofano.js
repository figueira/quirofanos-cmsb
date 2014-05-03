$(document).ready(function() {
	// Ir a formulario de paciente
	$("#ver-info-paciente").click(function() {
		$("#datos-quirofano").addClass("hidden");
		$("#datos-paciente").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Paciente");
	});

	// Ir formulario de quirofano
	$("#ver-info-quirofano").click(function() {
		$("#datos-paciente").addClass("hidden");
		$("#datos-quirofano").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Quirófano");
	});

	// Mostrar o no mostrar razon de riesgo
	var nivel = $("input[name=solicitud_quirofano-riesgo]");
	nivel.change(function(){
		nivel_seleccionado = $("input[name=solicitud_quirofano-riesgo]:checked");
		if (nivel_seleccionado.val() == "M")
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
});
