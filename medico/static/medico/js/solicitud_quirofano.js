// Mostrar numero habitacion paciente
var mostrarNumeroHabitacionPaciente = function() {
	$("#habitacion").removeClass("hidden")
};

// Mostrar razon riesgo
var mostrarRazonRiesgo = function() {
	$("#razon-riesgo").removeClass("hidden");
};

// Mostrar datos de quirofano en formulario
var mostrarInfoQuirofano = function() {
	$("#ver-info-quirofano").trigger("click");
};

// Mostrar modal de agregar procedimiento quirurgico
var mostrarModalAgregarProcedimientoQuirurgico = function() {
	mostrarInfoQuirofano();
	$("#accion-formulario").val("procedimiento_quirurgico");
	$("#agregar-procedimiento-quirurgico-modal").modal();
};

// Mostrar errores medico solicitante
var mostrarErroresMedicoSolicitante = function() {
	$("#medico-solicitante").parent("div").addClass("has-error");
	$("#medico-solicitante-error-help").removeClass("hidden");
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

// Mostrar errores paciente hospitalizado
var mostrarErroresPacienteHospitalizado = function() {
	$("#numero-habitacion-paciente-form-group").addClass("has-error");
	$("#habitacion").removeClass("hidden");
	$("#paciente-hospitalizado-error-help").removeClass("hidden");
};

// Mostrar errores numero habitacion paciente
var mostrarErroresNumeroHabitacionPaciente = function() {
	$("#habitacion").removeClass("hidden");
	$("#numero-habitacion-paciente").parent("div").addClass("has-error");
	$("#numero-habitacion-paciente-form-group").addClass("has-feedback");
	$("#numero-habitacion-paciente-error-feedback-icon").removeClass("hidden");
	$("#numero-habitacion-paciente-error-help").removeClass("hidden");
};

// Mostrar errores preferencia anestesica
var mostrarErroresPreferenciaAnestesica = function() {
	$("#radios-preferencia-anestesica").addClass("has-error");
	$("#preferencia-anestesica-form-group").addClass("has-feedback");
	$("#preferencia-anestesica-error-feedback-icon").removeClass("hidden");
	$("#preferencia-anestesica-error-help").removeClass("hidden");
};

// Mostrar errores observaciones
var mostrarErroresObservaciones = function() {
	$("#observaciones").parent("div").addClass("has-error");
	$("#observaciones-form-group").addClass("has-feedback");
	$("#observaciones-error-feedback-icon").removeClass("hidden");
	$("#observaciones-error-help").removeClass("hidden");
};

// Mostrar errores riesgo
var mostrarErroresRiesgo = function() {
	$("#radios-riesgo").addClass("has-error");
	$("#riesgo-form-group").addClass("has-feedback");
	$("#riesgo-error-feedback-icon").removeClass("hidden");
	$("#riesgo-error-help").removeClass("hidden");
};

// Mostrar errores razon riesgo
var mostrarErroresRazonRiesgo = function() {
	$("#razon-riesgo-input").parent("div").addClass("has-error");
	$("#razon-riesgo").addClass("has-feedback");
	$("#razon-riesgo-error-feedback-icon").removeClass("hidden");
	$("#razon-riesgo-error-help").removeClass("hidden");
};

// Mostrar errores dias hospitalizacion
var mostrarErroresDiasHospitalizacion = function() {
	$("#dias-hospitalizacion").parent("div").addClass("has-error");
	$("#dias-hospitalizacion-form-group").addClass("has-feedback");
	$("#dias-hospitalizacion-error-feedback-icon").removeClass("hidden");
	$("#dias-hospitalizacion-error-help").removeClass("hidden");
};

// Mostrar errores equipos especiales requeridos
var mostrarErroresEquiposEspecialesRequeridos = function() {
	$("#checkboxes-equipos-especiales-requeridos").addClass("has-error");
	$("#equipos-especiales-requeridos-form-group").addClass("has-feedback");
	$("#equipos-especiales-requeridos-error-feedback-icon").removeClass("hidden");
	$("#equipos-especiales-requeridos-error-help").removeClass("hidden");
};

// Mostrar errores materiales quirurgicos requeridos
var mostrarErroresMaterialesQuirurgicosRequeridos = function() {
	$("#checkboxes-materiales-quirurgicos-requeridos").addClass("has-error");
	$("#materiales-quirurgicos-requeridos-form-group").addClass("has-feedback");
	$("#materiales-quirurgicos-requeridos-error-feedback-icon").removeClass("hidden");
	$("#materiales-quirurgicos-requeridos-error-help").removeClass("hidden");
};

// Mostrar errores otros materiales quirurgicos
var mostrarErroresOtrosMaterialesQuirurgicos = function() {
	$("#otros-materiales-quirurgicos").parent("div").addClass("has-error");
	$("#otros-materiales-quirurgicos-form-group").addClass("has-feedback");
	$("#otros-materiales-quirurgicos-error-feedback-icon").removeClass("hidden");
	$("#otros-materiales-quirurgicos-error-help").removeClass("hidden");
};

// Mostrar errores honorarios cirujano principal
var mostrarErroresCirujanoPrincipal = function() {
	$("#cirujano-principal").parent("div").addClass("has-error");
	$("#cirujano-principal-error-help").removeClass("hidden");
};

// Mostrar errores anestesiologo
var mostrarErroresAnestesiologo = function() {
	$("#anestesiologo").parent("div").addClass("has-error");
	$("#anestesiologo-error-help").removeClass("hidden");
};

// Mostrar errores primer ayudante
var mostrarErroresPrimerAyudante = function() {
	$("#primer-ayudante").parent("div").addClass("has-error");
	$("#primer-ayudante-error-help").removeClass("hidden");
};

// Mostrar errores segundo ayudante
var mostrarErroresSegundoAyudante = function() {
	$("#segundo-ayudante").parent("div").addClass("has-error");
	$("#segundo-ayudante-error-help").removeClass("hidden");
};

// Mostrar errores tercer ayudante
var mostrarErroresTercerAyudante = function() {
	$("#tercer-ayudante").parent("div").addClass("has-error");
	$("#tercer-ayudante-error-help").removeClass("hidden");
};

// Mostrar errores nombre procedimiento
var mostrarErroresNombreProcedimiento = function() {
	$("#nombre-procedimiento").parent("div").addClass("has-error");
	$("#nombre-procedimiento-form-group").addClass("has-feedback");
	$("#nombre-procedimiento-error-feedback-icon").removeClass("hidden")
	$("#nombre-procedimiento-error-help").removeClass("hidden")
};

var sistemasCorporales;
var sistemaCorporalActual;
var organoCorporalActual;

// Mostrar las opciones del select de sistemas corporales
var mostrarOpcionesSistemasCorporales = function() {
	$.each(sistemasCorporales, function(indice, valor) {
		$("#sistemas-corporales").append("<option value=\"" + valor.id + "\">" + valor.nombre + "</option>");
	});
};

// Mostrar las opciones del select de organos corporales segun el sistema corporal seleccionado
var mostrarOpcionesOrganosCorporales = function(id_sistema_corporal) {
	var sistemaCorporal = $.grep(sistemasCorporales, function(valor, indice) {
		return valor.id == id_sistema_corporal
	});
	sistemaCorporalActual = sistemaCorporal[0]
	$("#organos-corporales").html("");
	$.each(sistemaCorporalActual.organos_corporales, function(indice, valor) {
		$("#organos-corporales").append("<option value=\"" + valor.id + "\">" + valor.nombre + "</option>");
	});
	mostrarOpcionesTiposProcedimientos(sistemaCorporalActual.organos_corporales[0].id);
	$("#id-organo-corporal").val(sistemaCorporalActual.organos_corporales[0].id);
	$("#id-tipo-procedimiento-quirurgico").val(sistemaCorporalActual.organos_corporales[0].tipos_procedimientos_permitidos[0].id);
};

// Mostrar las opciones de tipos de procedimientos permitidos segun el organo corporal seleccionado
var mostrarOpcionesTiposProcedimientos = function(id_organo_corporal) {
	var organoCorporal = $.grep(sistemaCorporalActual.organos_corporales, function(valor, indice) {
		return valor.id == id_organo_corporal
	});
	organoCorporalActual = organoCorporal[0]
	$("#tipos-procedimientos").html("");
	$.each(organoCorporalActual.tipos_procedimientos_permitidos, function(indice, valor) {
		$("#tipos-procedimientos").append("<option value=\"" + valor.id + "\">" + valor.nombre + "</option>");
	});
	$("#id-tipo-procedimiento-quirurgico").val(organoCorporalActual.tipos_procedimientos_permitidos[0].id);
};

// Seleccionar organo corporal que fue seleccionado anteriormente
var seleccionarSistemaCorporal = function(id_sistema_corporal_actual, id_organo_corporal, id_tipo_procedimiento) {
	var sistemaCorporal = $.grep(sistemasCorporales, function(valor, indice) {
		return valor.id == id_sistema_corporal_actual
	});
	sistemaCorporalActual = sistemaCorporal[0]
	$("#sistemas-corporales>option[value=" + id_sistema_corporal_actual + "]").attr("selected", "selected");
	mostrarOpcionesOrganosCorporales(id_sistema_corporal_actual);
	$("#organos-corporales>option[value=" + id_organo_corporal + "]").attr("selected", "selected");
	mostrarOpcionesTiposProcedimientos(id_organo_corporal);
	$("#tipos-procedimientos>option[value=" + id_tipo_procedimiento + "]").attr("selected", "selected");
}

$(document).ready(function() {
	// Ir a formulario de paciente
	$("#ver-info-paciente").click(function() {
		$("#datos-quirofano").addClass("hidden");
		$("#datos-paciente").removeClass("hidden");
		$("#titulo-detalles-solicitud").html("Detalles de Solicitud - Paciente");
	});

	// Ir a formulario de quirofano
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

	// Mostrar o no mostrar habitacion de paciente
	var hospitalizado = $("input[name=solicitud_quirofano-paciente_hospitalizado]");
	hospitalizado.change(function(){
		$("#habitacion").toggleClass("hidden");
		if ($("#habitacion").hasClass("hidden")) {
			$("#numero-habitacion-paciente").val("");
		}
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

	// Actualizar select de organos corporales cuando cambia el sistema corporal
	$("#sistemas-corporales").change(function() {
		idSistemaCorporal = $("#sistemas-corporales>option:selected").val();
		mostrarOpcionesOrganosCorporales(idSistemaCorporal);
	});

	// Actualizar select de tipos procedimientos cuando cambia el organo corporal. Ademas de actualizar el valor escondido del id-organo-corporal seleccionado.
	$("#organos-corporales").change(function() {
		idOrganoCorporal = $("#organos-corporales>option:selected").val();
		$("#id-organo-corporal").val(idOrganoCorporal)
		mostrarOpcionesTiposProcedimientos(idOrganoCorporal);
	});

	// Actualizar el valor escondido del id-tipo-procedimiento-quirurgico seleccionado.
	$("#tipos-procedimientos").change(function() {
		idTipoProcedimiento = $("#tipos-procedimientos>option:selected").val();
		$("#id-tipo-procedimiento-quirurgico").val(idTipoProcedimiento);
	});

	// Eliminar procedimiento quirurgico
	$(".eliminar-procedimiento-quirurgico").click(function() {
		$("#accion-formulario").val("eliminar_procedimiento_quirurgico");
		$("#id-procedimiento-quirurgico").val($(this).prev("input").val());
		$("#formulario-solicitud-quirofano").submit();
	});
});
