// Esconde menu de navegacion
var esconderMenuNavegacion = function() {
    $("#menu-navegacion").addClass("hidden");
}

// Actualziar hora actual
var actualizarHora = function() {
    Dajaxice.plan_quirurgico.obtener_hora_actual(function(data) {
        $(".hora-actual").html(data.hora_actual);
    });
}

$(document).ready(function() {
    esconderMenuNavegacion();
    $("html").mousemove(function() {
        if ($("#menu-navegacion").hasClass("hidden")) {
            $("#menu-navegacion").removeClass("hidden");
            setTimeout(esconderMenuNavegacion, 5000);
        }
    })

    // Intervalo de un segundo para actualizar hora actual
    setInterval(actualizarHora, 1000);
});
