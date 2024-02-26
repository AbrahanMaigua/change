document.addEventListener("DOMContentLoaded", function() {
    var display = document.getElementById('display');
    var tiempoInicial = 3540; // 5 minutos en segundos

    // Función para actualizar el cronómetro
    function actualizarCronometro() {
        var hours   = Math.floor(tiempoInicial / 3600);
        var minutes = Math.floor((tiempoInicial % 3600) / 60);
        var seconds = tiempoInicial % 60;

        // Formatear los valores para asegurar dos dígitos
        var hoursStr   = ('0' + hours).slice(-2);
        var minutesStr = ('0' + minutes).slice(-2);
        var secondsStr = ('0' + seconds).slice(-2);

        var timeString = hoursStr + ':' + minutesStr + ':' + secondsStr;
        display.textContent = timeString;
        tiempoInicial--; // Decrementar el tiempo
        if (tiempoInicial < 0) {
            clearInterval(intervalo);
            display.textContent = 'Tiempo expirado';
            window.location.href = '/'
        }
    }

    // Actualizar el cronómetro cada segundo
    var intervalo = setInterval(actualizarCronometro, 1000);
});