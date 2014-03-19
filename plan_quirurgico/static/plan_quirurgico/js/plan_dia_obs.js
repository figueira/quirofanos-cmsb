$(document).ready(function() {
	// Seleccionar seccion en menu de navegacion
	$(".navegacion").removeClass("active");
	$("#seccion-plan-quirurgico").addClass("active");

	// Cambio de estado de operacion
	$(".btn-estado-operacion").click(function() {
		if ($(this).attr("id") != "btn-en-habitacion") {
			if (!$(".select-en-habitacion").hasClass("hidden")) {
				$(".select-en-habitacion").addClass("hidden");
			}
		}else {
			$(".select-en-habitacion").removeClass("hidden");
		}
		$(".btn-estado-operacion").removeClass("btn").removeClass("btn-danger").removeClass("btn-warning").removeClass("btn-success").removeClass("btn-default");
		var botones = $(this).parent().children();
		$(botones[0]).addClass("btn").addClass("btn-danger").removeAttr("disabled");
		$(botones[1]).addClass("btn").addClass("btn-warning").removeAttr("disabled");
		$(botones[2]).addClass("btn").addClass("btn-success").removeAttr("disabled");
		$(botones[3]).addClass("btn").addClass("btn-success").removeAttr("disabled");
		$(this).removeClass("btn").removeClass("btn-danger").removeClass("btn-warning").removeClass("btn-success").removeClass("btn-default");
		$(this).addClass("btn").addClass("btn-default").attr("disabled", "disabled");
	});
});