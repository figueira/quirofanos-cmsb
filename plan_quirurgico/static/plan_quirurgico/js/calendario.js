$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");

    // Hacer que celdas del calendario se comporten como links
    $(".calendario-dia").click(function() {
        window.document.location = $(this).attr("href");
    });
});
