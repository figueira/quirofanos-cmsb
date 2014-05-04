// Mostrar modal de agregar procedimiento quirurgico
var mostrarModalAgregarProcedimientoQuirurgico = function() {
	$("#accion-formulario").val("procedimiento_quirurgico")
	$("#agregar-procedimiento-quirurgico-modal").modal();
};

// Mostrar errores nombre paciente
var mostrarErroresNombrePaciente = function() {
	$("#nombre-paciente").parent("div").addClass("has-error");
	$("#nombre-apellido-paciente-form-group").addClass("has-feedback");
	$("#nombre-paciente-error-feedback-icon").removeClass("hidden");
	$("#nombre-paciente-error-help").removeClass("hidden");
};

// Mostrar errores apellido paciente
var mostrarErroresApellidoPaciente = function() {
	$("#apellido-paciente").parent("div").addClass("has-error");
	$("#nombre-apellido-paciente-form-group").addClass("has-feedback");
	$("#apellido-paciente-error-feedback-icon").removeClass("hidden");
	$("#apellido-paciente-error-help").removeClass("hidden");
};

// Inicializar nacionalidad de cedula paciente
var inicializarNacionalidadCedulaPaciente = function() {
	$("#cedula-paciente-nacionalidad-texto").html($("#cedula-paciente-nacionalidad-input").val());
	if ($("#cedula-paciente-nacionalidad-input").val() == "E-") {
		$("#cedula-paciente-nacionalidad-cambiar").html("V-");
	}
};

// Mostrar errores asociados a la nacionalidad de cedula paciente
var mostrarErroresNacionalidadCedulaPaciente = function() {
	$("#cedula-paciente").parent("div").parent("div").addClass("has-error");
	$("#cedula-genero-paciente-form-group").addClass("has-feedback");
	$("#cedula-paciente-error-feedback-icon").removeClass("hidden").css("z-index", "2");
	$("#cedula-paciente-nacionalidad-error-help").removeClass("hidden");
};

// Mostrar errores asociados a la cedula paciente
var mostrarErroresCedulaPaciente = function() {
	$("#cedula-paciente").parent("div").parent("div").addClass("has-error");
	$("#cedula-genero-paciente-form-group").addClass("has-feedback");
	$("#cedula-paciente-error-feedback-icon").removeClass("hidden").css("z-index", "2");
	$("#cedula-paciente-error-help").removeClass("hidden");
};

// Mostrar errores genero paciente
var mostrarErroresGeneroPaciente = function() {
	$("#radios-genero-paciente").addClass("has-error");
	$("#cedula-genero-paciente-form-group").addClass("has-feedback");
	$("#genero-paciente-error-feedback-icon").removeClass("hidden");
	$("#genero-paciente-error-help").removeClass("hidden");
};

// Mostrar errores fecha de nacimiento paciente
var mostrarErroresFechaNacimientoPaciente = function() {
	$("#fecha-nacimiento-paciente").parent("div").addClass("has-error");
	$("#fecha-nacimiento-telefono-paciente-form-group").addClass("has-feedback");
	$("#fecha-nacimiento-paciente-error-feedback-icon").removeClass("hidden");
	$("#fecha-nacimiento-paciente-error-help").removeClass("hidden");
};

// Mostrar errores codigo telefono paciente
var mostrarErroresCodigoTelefonoPaciente = function() {
	$("#codigo-telefono-paciente").parent("div").addClass("has-error");
	$("#fecha-nacimiento-telefono-paciente-form-group").addClass("has-feedback");
	$("#codigo-telefono-paciente-error-feedback-icon").removeClass("hidden");
	$("#codigo-telefono-paciente-error-help").removeClass("hidden");
};

// Mostrar errores numero telefono paciente
var mostrarErroresNumeroTelefonoPaciente = function() {
	$("#numero-telefono-paciente").parent("div").addClass("has-error");
	$("#fecha-nacimiento-telefono-paciente-form-group").addClass("has-feedback");
	$("#numero-telefono-paciente-error-feedback-icon").removeClass("hidden");
	$("#numero-telefono-paciente-error-help").removeClass("hidden");
};

// Mostrar errores diagnostico ingreso paciente
var mostrarErroresDiagnosticoIngresoPaciente = function() {
	$("#diagnostico-ingreso-paciente").parent("div").addClass("has-error");
	$("#diagnostico-ingreso-paciente-form-group").addClass("has-feedback");
	$("#diagnostico-ingreso-paciente-error-feedback-icon").removeClass("hidden");
	$("#diagnostico-ingreso-paciente-error-help").removeClass("hidden");
};

// Mostrar errores servicios operatorios paciente
var mostrarErroresServiciosOperatoriosPaciente = function() {
	$("#checkboxes-servicios-operatorios-paciente").addClass("has-error");
	$("#servicios-operatorios-paciente-form-group").addClass("has-feedback");
	$("#servicios-operatorios-paciente-error-feedback-icon").removeClass("hidden");
	$("#servicios-operatorios-paciente-error-help").removeClass("hidden");
};

// Mostrar errores numero habitacion paciente
var mostrarErroresNumeroHabitacionPaciente = function() {
	$("#habitacion").removeClass("hidden");
	$("#numero-habitacion-paciente").parent("div").addClass("has-error");
	$("#numero-habitacion-paciente-form-group").addClass("has-feedback");
	$("#numero-habitacion-paciente-error-feedback-icon").removeClass("hidden");
	$("#numero-habitacion-paciente-error-help").removeClass("hidden");
};

// Mostrar errores area ingreso paciente
var mostrarErroresAreaIngresoPaciente = function() {
	$("#area-ingreso-numero-expediente").removeClass("hidden");
	$("#area-ingreso-paciente").parent("div").addClass("has-error");
	$("#area-ingreso-numero-expediente-form-group").addClass("has-feedback");
	$("#area-ingreso-paciente-error-feedback-icon").removeClass("hidden");
	$("#area-ingreso-paciente-error-help").removeClass("hidden");
};

// Mostrar errores numero expediente paciente
var mostrarErroresNumeroExpedientePaciente = function() {
	$("#area-ingreso-numero-expediente").removeClass("hidden");
	$("#numero-expediente-paciente").parent("div").addClass("has-error");
	$("#area-ingreso-numero-expediente-form-group").addClass("has-feedback");
	$("#numero-expediente-paciente-error-feedback-icon").removeClass("hidden");
	$("#numero-expediente-paciente-error-help").removeClass("hidden");
};

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

	// Mostrar o no mostrar numero de expediente paciente
	var expediente = $("input[name=paciente-con-expediente]");
	expediente.change(function(){
		$("#area-ingreso-numero-expediente").toggleClass("hidden");
	});

	// Cambiar la accion en formulario para que demuestre que se esta agregando un procedimiento quirurgico
	$("#agregar-procedimiento-quirurgico-btn").click(function() {
		$("#accion-formulario").val("procedimiento_quirurgico")
	});

	// Cambiar la accion en formulario para que demuestre que NO se esta agregando un procedimiento quirurgico
	$("#cancelar-agregar-procedimiento-quirurgico").click(function() {
		$("#accion-formulario").val("solicitud_quirofano")
	});

	// Cambiar nacionalidad de cedula pacie te
	$("#cedula-paciente-nacionalidad-cambiar").click(function() {
		if ($(this).html() == "E-") {
			$(this).html("V-");
			$("#cedula-paciente-nacionalidad-texto").html("E-");
			$("#cedula-paciente-nacionalidad-input").val("E-");
		}else {
			$(this).html("E-");
			$("#cedula-paciente-nacionalidad-texto").html("V-");
			$("#cedula-paciente-nacionalidad-input").val("V-");
		}
	});
});
