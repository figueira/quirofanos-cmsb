// Mostrar modal de formulario de duracion de intervencion quirurgica
var mostrarModalFormularioDuracionIntervencionQuirurgica = function() {
    $("#solicitar-quirofano").modal();
};

// Mostrar errores del atributo horas del formulario de duracion de intervencion quirurgica
var mostrarErroresDuracionHoras = function() {
    $("#duracion-horas").parent("div").addClass("has-error");
    $("#duracion-form-group").addClass("has-feedback");
    $("#duracion-horas-error-feedback-icon").removeClass("hidden");
    $("#duracion-horas-error-help").removeClass("hidden");
};

// Mostrar errores del atributo minutos del formulario de duracion de intervencion quirurgica
var mostrarErroresDuracionMinutos = function() {
    $("#duracion-minutos").parent("div").addClass("has-error");
    $("#duracion-form-group").addClass("has-feedback");
    $("#duracion-minutos-error-feedback-icon").removeClass("hidden");
    $("#duracion-minutos-error-help").removeClass("hidden");
};

// Mostrar aviso sobre seleccionar turno de intervencion segun duracion seleccionada
var mostrarAvisoSeleccionarTurnoIntervencion = function() {
    $("#duracion-intervencion-aviso").removeClass("hidden");
    $("#btn-solicitar-quirofano").html("Cambiar Duración");
};

// Mostrar numero habitacion paciente
var mostrarNumeroHabitacionPaciente = function(id_reservacion) {
  $("#habitacion-" + id_reservacion).removeClass("hidden")
};

// Mostrar campos expediente paciente
var mostrarCamposExpedientePaciente = function(id_reservacion) {
  $("#area-ingreso-numero-expediente-" + id_reservacion).removeClass("hidden")
};

// Mostrar compania aseguradora paciente
var mostrarCompaniaAseguradoraPaciente = function(id_reservacion) {
  $("#seguros-" + id_reservacion).removeClass("hidden")
};

// Mostrar razon riesgo
var mostrarRazonRiesgo = function(id_reservacion) {
  $("#razon-riesgo-" + id_reservacion).removeClass("hidden");
};

// Mostrar datos de quirofano en formulario
var mostrarInfoQuirofano = function(id_reservacion) {
  $("#datos-quirofano-" + id_reservacion).removeClass("hidden");
  $("#datos-paciente-" + id_reservacion).addClass("hidden");
  $("#titulo-detalles-solicitud-" + id_reservacion).html("<strong>Detalles de Solicitud - Quirófano</strong>");
};

// Mostrar datos de paciente en formulario
var mostrarInfoPaciente = function(id_reservacion) {
  $("#datos-paciente-" + id_reservacion).removeClass("hidden");
  $("#datos-quirofano-" + id_reservacion).addClass("hidden");
  $("#titulo-detalles-solicitud-" + id_reservacion).html("<strong>Detalles de Solicitud - Paciente</strong>");
};

$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");

  // Mostrar modal de cambio de horario de intervencion
  $(".btn-cambiar-horario-intervencion").click(function() {
    $("#id-intervencion-cambiar-horario").val($(this).val());
    $(this).closest(".modal").modal("hide");
    $("#solicitar-quirofano").modal();
  });
});
