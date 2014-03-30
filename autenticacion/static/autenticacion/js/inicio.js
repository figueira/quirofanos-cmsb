$(document).ready(function() {
  // Desplegar formulario de solicitud de cuenta medico
  $("#solicitar-cuenta-medico").click(function() {
    $("#body-solicitar-cuenta").addClass("hidden");
    $("#formulario-solicitud-medico").removeClass("hidden");
    $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Médico");
  });

  // Desplegar formulario de solicitud de cuenta departamento
  $("#solicitar-cuenta-departamento").click(function() {
    $("#body-solicitar-cuenta").addClass("hidden");
    $("#formulario-solicitud-departamento").removeClass("hidden");
    $("#titulo-solicitar-cuenta").html("Solicitar Cuenta - Departamento");
  });

  // Volver a seleccion de tipo de solicitud de cuenta
  $(".volver-solicitar-cuenta").click(function() {
    $("#formulario-solicitud-medico").addClass("hidden");
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
  $("#cedula-medico-nacionalidad-cambiar").click(function() {
    if ($(this).html() == "E-") {
      $(this).html("V-");
      $("#cedula-medico-nacionalidad-texto").html("E-");
      $("#cedula-medico-nacionalidad-input").val("E-");
    }else {
      $(this).html("E-");
      $("#cedula-medico-nacionalidad-texto").html("V-");
      $("#cedula-medico-nacionalidad-input").val("V-");
    }
  });
});
