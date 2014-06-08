// Mostrar numero habitacion paciente
var mostrarNumeroHabitacionPaciente = function(id_reservacion) {
  $("#habitacion-" + id_reservacion).removeClass("hidden")
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
  $("#opciones-gestion-solicitud").removeClass("hidden");
};

// Mostrar datos de paciente en formulario
var mostrarInfoPaciente = function(id_reservacion) {
  $("#datos-paciente-" + id_reservacion).removeClass("hidden");
  $("#datos-quirofano-" + id_reservacion).addClass("hidden");
  $("#titulo-detalles-solicitud-" + id_reservacion).html("<strong>Detalles de Solicitud - Paciente</strong>");
  $("#opciones-gestion-solicitud").addClass("hidden");
};
