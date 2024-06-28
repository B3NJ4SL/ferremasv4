
$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWith(parametro)) {
        return true;
    }
    
    return false;

}, "Debe terminar por duocuc.cl")


$("#formulario_contacto").validate({
    rules: {
        nombre: {
            required: true,
            minlength:6,
            maxlength:30
        },
        email: {
            required: true,
            email: true,
            terminaPor: "duocuc.cl"
        },
        mensaje: {
            required: true,
            minlength: 5,
            maxlength: 200
        }

    }
})



$("#guardar").click(function() {
    if($("#formulario_contacto").valid() == false){
        return;
    }
    let nombre = $("#nombre").val()
    let email = $("#email").val()
    let tipoSolicitud = $("#tipo_solicitud").val()
    let mensaje = $("#mensaje").val()
    let avisos = $("#avisos").is(":checked")

    
})