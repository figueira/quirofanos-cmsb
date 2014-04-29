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

$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");
});
