// Mostrar busqueda de medico por cedula
var mostrarBusquedaCedulaMedico = function() {
  $('#solicitar-cuenta-medico').trigger('click');
};

// Mostrar busqueda de departamento por nombre
var mostrarBusquedaNombreDepartamento = function() {
  $('#solicitar-cuenta-departamento').trigger('click');
};

// Mostrar formulario de solicitud de registro medico
var mostrarFormularioSolicitudMedico = function() {
  $("#body-solicitar-cuenta").addClass("hidden");
  $("#formulario-solicitud-departamento").addClass("hidden");
  $("#formulario-solicitud-medico").removeClass("hidden");
  $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Médico");
};

// Mostrar formulario de solicitud de registro departamento
var mostrarFormularioSolicitudDepartamento = function() {
  $("#body-solicitar-cuenta").addClass("hidden");
  $("#formulario-solicitud-departamento").removeClass("hidden");
  $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Departamento");
};

// Inicializar nacionalidad de busqueda cedula medico
var inicializarNacionalidadCedulaMedico = function() {
  $("#busqueda-cedula-medico-nacionalidad-texto").html($("#busqueda-cedula-medico-nacionalidad-input").val());
  if ($("#busqueda-cedula-medico-nacionalidad-input").val() == "E-") {
    $("#busqueda-cedula-medico-nacionalidad-cambiar").html("V-");
  }
};

// Mostrar errores asociados a la nacionalidad de busqueda cedula medico
var mostrarErroresNacionalidadCedulaMedico = function() {
  $("#busqueda-cedula-medico").parent("div").parent("div").addClass("has-error");
  $("#busqueda-cedula-medico-form-group").addClass("has-feedback");
  $("#busqueda-cedula-medico-error-feedback-icon").removeClass("hidden").css("z-index", "2");
  $("#busqueda-cedula-medico-nacionalidad-error-help").removeClass("hidden");
};

// Mostrar errores asociados a la cedula de busqueda medico
var mostrarErroresCedulaMedico = function() {
  $("#busqueda-cedula-medico").parent("div").parent("div").addClass("has-error");
  $("#busqueda-cedula-medico-form-group").addClass("has-feedback");
  $("#busqueda-cedula-medico-error-feedback-icon").removeClass("hidden").css("z-index", "2");
  $("#busqueda-cedula-medico-error-help").removeClass("hidden");
};

// Mostrar errores asociados al nombre de busqueda departamento
var mostrarErroresNombreDepartamento = function() {
  $("#busqueda-nombre-departamento").parent("div").addClass("has-error");
  $("#busqueda-nombre-departamento-error-help").removeClass("hidden");
};

// Mostrar errores asociados al nombre de usuario de solicitud de registro medico
var mostrarErroresUsuarioMedico = function() {
  $("#nombre-usuario-medico").parent("div").addClass("has-error");
  $("#email-nombre-usuario-medico-form-group").addClass("has-feedback");
  $("#nombre-usuario-medico-error-feedback-icon").removeClass("hidden");
  $("#nombre-usuario-medico-error-help").removeClass("hidden");
};

// Mostrar errores asociados al nombre de usuario de solicitud de registro departamento
var mostrarErroresUsuarioDepartamento = function() {
  $("#nombre-usuario-departamento").parent("div").addClass("has-error");
  $("#email-nombre-usuario-departamento-form-group").addClass("has-feedback");
  $("#nombre-usuario-departamento-error-feedback-icon").removeClass("hidden");
  $("#nombre-usuario-departamento-error-help").removeClass("hidden");
};

$(document).ready(function() {
  // Desplegar formulario de solicitud de cuenta medico
  $("#solicitar-cuenta-medico").click(function() {
    $("#body-solicitar-cuenta").addClass("hidden");
    $("#formulario-busqueda-medico").removeClass("hidden");
    $("#formulario-solicitud-departamento").addClass("hidden");
    $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Médico");
  });

  // Desplegar formulario de solicitud de cuenta departamento
  $("#solicitar-cuenta-departamento").click(function() {
    $("#body-solicitar-cuenta").addClass("hidden");
    $("#formulario-busqueda-departamento").removeClass("hidden");
    $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Departamento");
  });

  // Volver a seleccion de tipo de solicitud de cuenta
  $(".volver-solicitar-cuenta").click(function() {
    $("#formulario-busqueda-medico").addClass("hidden");
    $("#formulario-solicitud-medico").addClass("hidden");
    $("#formulario-busqueda-departamento").addClass("hidden");
    $("#formulario-solicitud-departamento").addClass("hidden");
    $("#body-solicitar-cuenta").removeClass("hidden");
    $("#titulo-solicitar-cuenta").html("Solicitar Cuenta");
  });

  // Popover de solicitar cuenta medico
  $('#solicitar-cuenta-medico').popover({
    placement: "bottom",
    trigger: "hover",
    title: "Médico",
    content: "Cuenta para personal médico y quirúrgico."
  });

  // Popover de solicitar cuenta departamento
  $('#solicitar-cuenta-departamento').popover({
    placement: "bottom",
    trigger: "hover",
    title: "Departamento Clínico",
    content: "Cuenta para departamentos que requieren información del plan quirúrgico."
  })

  // Cambiar nacionalidad de cedula medico
  $("#busqueda-cedula-medico-nacionalidad-cambiar").click(function() {
    if ($(this).html() == "E-") {
      $(this).html("V-");
      $("#busqueda-cedula-medico-nacionalidad-texto").html("E-");
      $("#busqueda-cedula-medico-nacionalidad-input").val("E-");
    }else {
      $(this).html("E-");
      $("#busqueda-cedula-medico-nacionalidad-texto").html("V-");
      $("#busqueda-cedula-medico-nacionalidad-input").val("V-");
    }
  });
});
