console.log('bora viu!!')

function actualizarCronometro() {
    const counterElement = document.getElementById('counter');
    
    // Función para convertir el tiempo en formato HH:MM:SS a segundos
    function obtenerSegundos(tiempo) {
        let partesTiempo = tiempo.split(":");
        let horas = parseInt(partesTiempo[0]);
        let minutos = parseInt(partesTiempo[1]);
        let segundos = parseInt(partesTiempo[2]);
        return horas * 3600 + minutos * 60 + segundos;
    }
    
    let totalseg = obtenerSegundos(counterElement.textContent); // Obtener el contenido del elemento
    let tiempoRestante = totalseg;

    // Si el tiempo restante es 0, detener el cronómetro
    if (tiempoRestante === 0) {
        clearInterval(intervalo);
    } else {
        tiempoRestante--; // Decrementar el tiempo restante
    }
}

function iniciarCronometro() {
    console.log("Cronómetro iniciado");
    actualizarCronometro(); // Llamar a la función una vez para que comience inmediatamente
    return setInterval(actualizarCronometro, 1000);
}

document.getElementById('startButton').addEventListener('click', function() {
    // Cuando se hace clic en el botón, se inicia el cronómetro
    var intervalo = iniciarCronometro();
});
