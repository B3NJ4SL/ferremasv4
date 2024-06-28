const $txtUsuario = document.getElementById('txtUsuario')
const $txtPass = document.getElementById('txtPass')
const $formlog = document.getElementById('formlog')



(function (){
    $formlog.addEventListener('submit',function(e) {
        let nombre=String($txtUsuario.value).trim();
        if(nombre.length == 0){
            alert("El nombre de usuario no puede estar vacio!!!");
            e.preventDefault();
        }   
        
    });

})();








