//pajina 1
function mostrarValores(){
    
    let nombre = "Camilo"
    let edad = 19;
    let esEstudiante = true;
    document.write("Nombre: ", nombre, "<br>");
    document.write("Edad: ", edad, "<br>");
    document.write("¿Es Estudainte?: ", esEstudiante, "<br><br>");

    //cambio de valores
    

    nombre = "Andrés"
    edad = 22;
    esEstudiante = false;
    document.write("<b>Nombre Cambiado<b>: ", nombre, "<br>");
    document.write("<b>Edad Cambiada<b>: ", edad, "<br>");
    document.write("¿Es Estudainte?: ", esEstudiante, "<br>");

}

function OperacionesMatematicas(){

    let a = 15;
    let b = 26;
    let suma = a + b;
    let resta = a - b;
    let multiplicacion = a * b;
    let division = a / b;
    document.write("La suma de ", a, " y ", b , " es: ", suma, "<br>");
    document.write("La resta de ", a, " y ", b , " es: ", resta, "<br>");
    document.write("La multiplicacion  de ", a, " y ", b , " es: ", multiplicacion, "<br>");
    document.write("La division de ", a, " y ", b , " es: ", division, "<br><br>");
    let igual = a == b;
    let diferente = a != b;
    let mayorque = a > b;
    let menorque = a < b;
    let mayorigual = a >= b;
    let menorigual = a <= b;
    document.write("Es igual ", a, " que ", b , ": ", igual, "<br>");
    document.write("Es diferente ", a, " que ", b , ": ", diferente, "<br>");
    document.write("Es mayor ", a, " que ", b , ": ", mayorque, "<br>");
    document.write("Es menor ", a, " que ", b , ": ", menorque, "<br>");
    document.write("Es mayor o igual ", a, " que ", b , ": ", mayorigual, "<br>");
    document.write("Es menor o igual ", a, " que ", b , ": ", menorigual, "<br>");


}

function PuedeConducir(){
    let esMayorDeEdad = true;
    let tieneLicencia = false;
    let PuedeConducir = esMayorDeEdad && tieneLicencia;
    document.write("hola camilo Bienvenido al curso de programacion basica?: ", " puede conducir: ", PuedeConducir);

}

