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
};

// Mostrar datos de paciente en formulario
var mostrarInfoPaciente = function(id_reservacion) {
  $("#datos-paciente-" + id_reservacion).removeClass("hidden");
  $("#datos-quirofano-" + id_reservacion).addClass("hidden");
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
var inicializarNacionalidadCedulaPaciente = function(id_reservacion) {
  $("#cedula-paciente-nacionalidad-texto-" + id_reservacion).html($("#cedula-paciente-nacionalidad-input-" + id_reservacion).val());
  if ($("#cedula-paciente-nacionalidad-input-" + id_reservacion).val() == "E-") {
    $("#cedula-paciente-nacionalidad-cambiar-" + id_reservacion).html("V-");
  }
};

// Cambiar nacionalidad de cedula paciente
var cambiarNacionalidadCedulaPaciente = function(id_reservacion) {
  if ($("#cedula-paciente-nacionalidad-cambiar-" + id_reservacion).html() == "E-") {
    $("#cedula-paciente-nacionalidad-cambiar-" + id_reservacion).html("V-");
    $("#cedula-paciente-nacionalidad-texto-" + id_reservacion).html("E-");
    $("#cedula-paciente-nacionalidad-input-" + id_reservacion).val("E-");
  }else {
    $(this).html("E-");
    $("#cedula-paciente-nacionalidad-texto-" + id_reservacion).html("V-");
    $("#cedula-paciente-nacionalidad-input-" + id_reservacion).val("V-");
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

// Mostrar errores paciente con expediente
var mostrarErroresPacienteConExpediente = function() {
  $("#area-ingreso-numero-expediente-form-group").addClass("has-error")
  $("#area-ingreso-numero-expediente").removeClass("hidden");
  $("#paciente-con-expediente-error-help").removeClass("hidden");
}

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

// Mostrar errores compania aseguradora paciente
var mostrarErroresCompaniaAseguradoraPaciente = function() {
  $("#seguros").removeClass("hidden");
  $("#compania-aseguradora-paciente").parent("div").addClass("has-error");
  $("#compania-aseguradora-paciente-error-help").removeClass("hidden");
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

// Mostrar errores honorarios cirujano principal
var mostrarErroresHonorariosCirujanoPrincipal = function() {
  $("#honorarios-cirujano-principal").parent("div").parent("div").addClass("has-error");
  $("#honorarios-cirujano-principal-error-help").removeClass("hidden");
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

// Mostrar errores honorarios tercer ayudante
var mostrarErroresHonorariosTercerAyudante = function() {
  $("#honorarios-tercer-ayudante").parent("div").parent("div").addClass("has-error");
  $("#honorarios-tercer-ayudante-error-help").removeClass("hidden");
};


var seleccionarPestana = function(estado){  
  if (estado == 'pendientes'){
    // $('#li-en-espera').addClass('active');
    // $('#li-aprobadas').removeClass('active');
    // $('#li-rechazadas').removeClass('active');
    $("#contenido-pendientes").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'aprobadas'){
    // $('#li-aprobadas').addClass('active');
    // $('#li-en-espera').removeClass('active');
    // $('#li-rechazadas').removeClass('active');
    $("#contenido-aprobadas").removeClass('hidden');
    $("#contenido-pendientes").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'rechazadas'){
    // $('#li-rechazadas').addClass('active');
    // $('#li-en-espera').removeClass('active');
    // $('#li-aprobadas').removeClass('active');
    $("#contenido-rechazadas").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
    $("#contenido-pendientes").addClass('hidden');
  };  
};

// Opciones de paginacion
var options = {
    currentPage: 1,
    totalPages: 10,
    size:"normal",
    alignment:"left",
    useBootstrapTooltip:true,
    numberOfPages:5,
    tooltipTitles: function (type, page, current) {
        switch (type) {
            case "first":
            return "Primera Página";
            case "prev":
            return "Anterior";
            case "next":
            return "Siguiente";
            case "last":
            return "Última Página";
            case "page":
            return "Ir a Página "+page;
        }
    },
    pageUrl: function(type, page, current){
        return "?page="+page;
    }
};

var inicializarPaginacion = function(pagActual, pagTotales, estado){
    options.currentPage = pagActual;
    options.totalPages = pagTotales;
    if ( estado == 'pendientes'){
        $('#paginacion-pendientes').bootstrapPaginator(options);
    } else if ( estado == 'aprobadas' ){
        $('#paginacion-aprobadas').bootstrapPaginator(options);
    } else if ( estado == 'rechazadas' ){
        $('#paginacion-rechazadas').bootstrapPaginator(options);
    }

};

var seleccionarPestana = function(estado){
    if (estado == 'pendientes'){
        $('#tab-pendientes').addClass('active');
        $('#tab-aprobadas').removeClass('active');
        $('#tab-rechazadas').removeClass('active');
        $("#paginacion-pendientes").removeClass('hidden');
        $("#paginacion-aprobadas").addClass('hidden');
        $("#paginacion-rechazadas").addClass('hidden');
        $("#contenido-pendientes").removeClass('hidden');
        $("#contenido-aprobadas").addClass('hidden');
        $("#contenido-rechazadas").addClass('hidden');
    } else if (estado == 'aprobadas'){
        $('#tab-aprobadas').addClass('active');
        $('#tab-pendientes').removeClass('active');
        $('#tab-rechazadas').removeClass('active');
        $("#paginacion-aprobadas").removeClass('hidden');
        $("#paginacion-rechazadas").addClass('hidden');
        $("#contenido-aprobadas").removeClass('hidden');
        $("#contenido-pendientes").addClass('hidden');
        $("#contenido-rechazadas").addClass('hidden');
    } else if (estado == 'rechazadas'){
        $('#tab-rechazadas').addClass('active');
        $('#tab-pendientes').removeClass('active');
        $('#tab-aprobadas').removeClass('active');
        $("#paginacion-rechazadas").removeClass('hidden');
        $("#paginacion-aprobadas").addClass('hidden');
        $("#paginacion-pendientes").addClass('hidden');
        $("#contenido-rechazadas").removeClass('hidden');
        $("#contenido-aprobadas").addClass('hidden');
        $("#contenido-pendientes").addClass('hidden');
    };
};

$(document).ready(function() {
  // Seleccionar seccion en menu de navegacion
  $(".navegacion").removeClass("active");
  $("#seccion-mis-solicitudes").addClass("active");

  // Desplegar Solicitudes En Espera
  // $("#li-aprobadas").click(function() {
  //   $("#en-espera").addClass("hidden");
  //   $("#rechazadas").addClass("hidden");
  //   $("#aprobadas").removeClass("hidden");

  //   $("#li-aprobadas").addClass("active");
  //   $("#li-en-espera").removeClass("active");
  //   $("#li-rechazadas").removeClass("active");
  // });

  // $("#li-en-espera").click(function() {
  //   $("#aprobadas").addClass("hidden");
  //   $("#rechazadas").addClass("hidden");
  //   $("#en-espera").removeClass("hidden");

  //   $("#li-en-espera").addClass("active");
  //   $("#li-aprobadas").removeClass("active");
  //   $("#li-rechazadas").removeClass("active");
  // });

  // $("#li-rechazadas").click(function() {
  //   $("#aprobadas").addClass("hidden");
  //   $("#en-espera").addClass("hidden");
  //   $("#rechazadas").removeClass("hidden");

  //   $("#li-rechazadas").addClass("active");
  //   $("#li-aprobadas").removeClass("active");
  //   $("#li-en-espera").removeClass("active");
  // });

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
  var forma_pago = $("input[name=solicitud_quirofano-tipo_pago_paciente]");
  forma_pago.change(function(){
    seguro = $("input[name=solicitud_quirofano-tipo_pago_paciente]:checked");
    if (seguro.val() == "S")
      $("#seguros").removeClass("hidden");
    else {
      $("#seguros").addClass("hidden");
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

  // Mostrar o no mostrar numero de expediente paciente
  var expediente = $("input[name=solicitud_quirofano-paciente_con_expediente]");
  expediente.change(function(){
    $("#area-ingreso-numero-expediente").toggleClass("hidden");
    if ($("#area-ingreso-numero-expediente").hasClass("hidden")) {
      $("#numero-expediente-paciente").val("")
    }
  });
});
