function validarFormulario(){
    let nombre = document.getElementById("nombre").value;
    let correo = document.getElementById("email").value;

    if(nombre == "" || correo == ""){
        alert("por favor, completa todos los campos.");
        return false;

    }
    return true;
}
function mostrarMensaje(){
    alert("Hola bienvenodo");
}