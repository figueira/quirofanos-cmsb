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

var inicializarPaginacion = function(pagActual, pagTotales, periodo){
    options.currentPage = pagActual;
    options.totalPages = pagTotales;
    if ( periodo == 'semana-actual'){
        $('#paginacion-semana-actual').bootstrapPaginator(options);
    } else if ( periodo == 'mes-actual' ){
        $('#paginacion-mes-actual').bootstrapPaginator(options);
    } else if ( periodo == 'ano-actual' ){
        $('#paginacion-ano-actual').bootstrapPaginator(options);
    }

};

var seleccionarPestana = function(periodo){
    if (periodo == 'semana_actual'){
        $('#tab-semana-actual').addClass('active');
        $('#tab-mes-actual').removeClass('active');
        $('#tab-ano-actual').removeClass('active');
        $("#paginacion-semana-actual").removeClass('hidden');
        $("#paginacion-mes-actual").addClass('hidden');
        $("#paginacion-ano-actual").addClass('hidden');
        $("#contenido-semana-actual").removeClass('hidden');
        $("#contenido-mes-actual").addClass('hidden');
        $("#contenido-ano-actual").addClass('hidden');
    } else if (periodo == 'mes_actual'){
        $('#tab-mes-actual').addClass('active');
        $('#tab-semana-actual').removeClass('active');
        $('#tab-ano-actual').removeClass('active');
        $("#paginacion-mes-actual").removeClass('hidden');
        $("#paginacion-semana-actual").addClass('hidden');
        $("#paginacion-ano-actual").addClass('hidden');
        $("#contenido-mes-actual").removeClass('hidden');
        $("#contenido-semana-actual").addClass('hidden');
        $("#contenido-ano-actual").addClass('hidden');
    } else if (periodo == 'ano_actual'){
        $('#tab-ano-actual').addClass('active');
        $('#tab-semana-actual').removeClass('active');
        $('#tab-mes-actual').removeClass('active');
        $("#paginacion-ano-actual").removeClass('hidden');
        $("#paginacion-mes-actual").addClass('hidden');
        $("#paginacion-semana-actual").addClass('hidden');
        $("#contenido-ano-actual").removeClass('hidden');
        $("#contenido-mes-actual").addClass('hidden');
        $("#contenido-semana-actual").addClass('hidden');
    };
};

$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-proximas-operaciones").addClass("active");
});
