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
        $("#paginacion-pendientes").addClass('hidden');
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
    $("#seccion-solicitudes-quirofanos").addClass("active");

});
