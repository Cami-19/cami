function sumarNumeros(){
const entrada = document.getElementById('promedio').value;
const numeros = entrada.split(',').map(num => parseFloat(num.trim()));

    let i = 0;
    let suma = 0;
    
   
    for(i;i <=numeros.length; i++){
        if (!isNaN(numeros[i])){
            suma = suma + numeros[i];
        }
       
    }
    
    const promedio = suma/numeros.length;
    document.getElementById('salidaPromedio').innerText= `suma:  ${suma.toFixed(1)}, promedio: ${promedio.toFixed(1)}`;
    
}

function ingresarNumeros(){

let numero = parseFloat(prompt("ingrese un numero"));
let i =0;
let suma = 0;
while (numero>=0){ 
    i++;
    suma = suma + numero;
numero = parseFloat(prompt("ingrese otro numero"));
    

}
document.getElementById('salidaNumeros').innerText= `suma:  ${suma}, imgresaste ${i} numeros`;


}

function validarContrasena(){

    let contraseña = "Csil19++";
    let correcto = "";
    let intento = 0;
    do{
        correcto =prompt("ingrese contraseña");
        intento++;
    }
    while(contraseña!=correcto);

    document.getElementById("salidaContrasena").innerText= `contraseña correcta, numero de intentos ${intento}`;
    
    
}
