// Creacion de peticiones AJAX que van a interactuar con el listado de usuarios del proyecto vivero.
//Esta peticion es la mas sencilla NO se utiliza ningun framwork como angular, react

function listadoUsuarios(){
    //El simbolo $ refleja una instancia de JQUERY

    $.ajax({
        url: "/usuarios/listadoUsuarios/",
        type: "get", 
        dataType: "json",
        success: function(response){
            console.log(response);
        },

    });
}

$(document).ready(function(){
    listadoUsuarios();

});