var toggleDetallesProcedimiento = function(elemento) {
    $(elemento).next(".procedimiento-quirurgico-detalle").toggleClass("hidden");
    var icono = $($(elemento).children(".glyphicon")[0]);
    if (icono.hasClass("glyphicon-plus-sign")) {
        icono.removeClass("glyphicon-plus-sign");
        icono.addClass("glyphicon-minus-sign");
    }else {
        icono.removeClass("glyphicon-minus-sign");
        icono.addClass("glyphicon-plus-sign");
    }
};

$(document).ready(function() {
    // Loading en posts
    $(".btn-loading").click(function () {
        $(this).button('loading');
    });
});
