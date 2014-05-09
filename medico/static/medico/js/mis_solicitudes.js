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