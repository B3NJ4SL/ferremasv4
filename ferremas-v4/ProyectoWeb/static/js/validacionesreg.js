const nombre = document.getElementById("name")
const email = document.getElementById("email")
const pass = document.getElementById("password")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")


form.addEventListener("submit", e=>{
    e.preventDefault()    
    if(nombre.value.length <6){ 
        alert("El nombre no es valido, debe tener al menos 6 caracteres como minimmo")
               
    }    
   

    
    if(pass.value.length < 8 ){
        alert("La contraseña no es valida, debe tener al menos 8 caracteres como minimmo")
       
    }
})

