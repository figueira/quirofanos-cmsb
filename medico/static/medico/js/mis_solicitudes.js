var seleccionarPestana = function(estado){
  if (estado == 'pendientes'){
    $('#li-en-espera').addClass('active');
    $('#li-aprobadas').removeClass('active');
    $('#li-rechazadas').removeClass('active');
    $("#contenido-pendientes").removeClass('hidden');
    $("#contenido-aprobadas").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'aprobadas'){
    $('#li-aprobadas').addClass('active');
    $('#li-en-espera').removeClass('active');
    $('#li-rechazadas').removeClass('active');
    $("#contenido-aprobadas").removeClass('hidden');
    $("#contenido-pendientes").addClass('hidden');
    $("#contenido-rechazadas").addClass('hidden');
  } else if (estado == 'rechazadas'){
    $('#li-rechazadas').addClass('active');
    $('#li-en-espera').removeClass('active');
    $('#li-aprobadas').removeClass('active');
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
  $("#li-aprobadas").click(function() {
    $("#en-espera").addClass("hidden");
    $("#rechazadas").addClass("hidden");
    $("#aprobadas").removeClass("hidden");

    $("#li-aprobadas").addClass("active");
    $("#li-en-espera").removeClass("active");
    $("#li-rechazadas").removeClass("active");
  });

  $("#li-en-espera").click(function() {
    $("#aprobadas").addClass("hidden");
    $("#rechazadas").addClass("hidden");
    $("#en-espera").removeClass("hidden");

    $("#li-en-espera").addClass("active");
    $("#li-aprobadas").removeClass("active");
    $("#li-rechazadas").removeClass("active");
  });

  $("#li-rechazadas").click(function() {
    $("#aprobadas").addClass("hidden");
    $("#en-espera").addClass("hidden");
    $("#rechazadas").removeClass("hidden");

    $("#li-rechazadas").addClass("active");
    $("#li-aprobadas").removeClass("active");
    $("#li-en-espera").removeClass("active");
  });
});
