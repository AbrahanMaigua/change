let intervalo;
let contador;
let isactivecronometro = false;

let totalSeconds = 0;
const MAX_SECONDS = 86400; // 24 horas en segundos
const counterElement = document.getElementById('counter');
const sendLinkElement = document.getElementById('sendLink');

const timeT = document.getElementById("counter");
if (timeT != ''){
    let textoInicial = timeT.textContent;

    let caracteres = textoInicial.split('');
    let contador_t = caracteres.length - 1;


}


console.log(counterElement)
console.log(counterElement)

function incrementTime(secondsToAdd) {
    totalSeconds += secondsToAdd;
    if (totalSeconds > MAX_SECONDS) {
        totalSeconds = MAX_SECONDS;
    }
    updateCounter();
    updateSendLink();
}

function resetTime() {
    totalSeconds = 0;
    updateCounter();
    updateSendLink();
}

function updateSendLink() {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    sendLinkElement.href = `cheking?hours=${hours}&min=${minutes}&seg=${seconds}`;
}

function updateCounter() {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    counterElement.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

function sendcheking() {
    const timeT = document.getElementById("counter")
    let tiempoInicial = timeT.textContent;
    let totalSeconds = obtenerSegundos(tiempoInicial);

    const hours = pad(Math.floor(totalSeconds / 3600));
    const minutes = pad(Math.floor((totalSeconds % 3600) / 60));
    const seconds = pad(totalSeconds % 60);
    if (`${seconds}` != '00' || `${minutes}` != '00' || `${hours}` != '00') {
        window.location.href = `cheking?hours=${hours}&min=${minutes}&seg=${seconds}`

    } else {
        timeT.classList.add('red');
        console.log(timeT.className)

    }
}

function pad(num) {
    return num.toString().padStart(2, '0');
}

// Función para actualizar el contador
function actualizarContador() {
    let tiempoFormateado = formatearTiempo(contador);

    contador--; // Decrementar el contador
    // document.getElementById("counter").textContent = tiempoFormateado; // Actualizar el valor mostrado en el contador

    // Si el contador llega a cero, detenerlo
    if (contador === 0) {
        clearInterval(intervalo); // Detener el contador
        if (isactivecronometro === true) {
            const eventSource = new EventSource('/complete');

            eventSource.onmessage = function(event) {
                newData.textContent = 'Server Time: ' + event.data;

            }
            window.location.href = '/';
        }
        setInterval(contador, 1000);

    }
}


function toggleContador() {
    // Si el contador está corriendo, detenerlo
    if (intervalo) {
        clearInterval(intervalo);
        intervalo = null;
        return;
    }

    // Si el contador está detenido, iniciarlo
    intervalo = setInterval(actualizarContador, 1000);
}

// Función para convertir el tiempo en formato HH:MM:SS a segundos
function obtenerSegundos(tiempo) {
    let partesTiempo = tiempo.split(":");
    let horas = parseInt(partesTiempo[0]);
    let minutos = parseInt(partesTiempo[1]);
    let segundos = parseInt(partesTiempo[2]);
    return horas * 3600 + minutos * 60 + segundos;
}

// Función para formatear los segundos en formato HH:MM:SS
function formatearTiempo(segundos) {
    let horas = Math.floor(segundos / 3600);
    let minutos = Math.floor((segundos % 3600) / 60);
    let segundosRestantes = segundos % 60;


    return `${pad(horas)}:${pad(minutos)}:${pad(segundosRestantes)}`;
}

function resetCounter() {
    document.getElementById("counter").textContent = '00:00:00';
    textoInicial = document.getElementById("counter").textContent;
    caracteres = textoInicial.split('');
    contador_t = caracteres.length - 1;

}


function addNumber(num) {


    if (contador_t != -1 && caracteres[contador_t] != ':') {
        caracteres[contador_t] = num.toString();
        contador_t--;
    } else {
        contador_t--;
        addNumber(num)
    }
    // Actualizamos solo los caracteres modificados en el texto mostrado
    let Seg = obtenerSegundos(caracteres.join(''))
    if (Seg > MAX_SECONDS) {
        Seg = MAX_SECONDS;
    }
    timeT.textContent = formatearTiempo(Seg);
    timeT.classList.remove('red')
}

function pix(total, pedido_id) {
    window.location.href = `pix/${pedido_id}`

}

function actualizarCronometro() {
    const counterElement = document.getElementById('counter');
    let totalseg = obtenerSegundos(counterElement.textContent); // Obtener el contenido del elemento
    let tiempoRestante = totalseg;

    // Si el tiempo restante es 0, detener el cronómetro
    if (tiempoRestante === 0) {
        clearInterval(intervalo);
        window.location.href = '/';


    } else {
        tiempoRestante--; // Decrementar el tiempo restante
        counterElement.textContent = formatearTiempo(tiempoRestante); // Actualizar el valor mostrado en el contador

    }
}

function iniciarCronometro() {
    console.log("Cronómetro iniciado");
    actualizarCronometro(); // Llamar a la función una vez para que comience inmediatamente
    return setInterval(actualizarCronometro, 900);
}

function startButton() {
    // Cuando se hace clic en el botón, se inicia el cronómetro
    if (isactivecronometro === false) {
        isactivecronometro = true
        document.getElementById('startButton').remove()
        document.getElementById('back').remove()

        var intervalo = iniciarCronometro();


    };
};


var queryString = window.location.search;
console.log(queryString)
if (queryString.includes("startauto")) {
    // Llama a la función si estás en la página deseada y el parámetro existe
    startButton();
    const eventSource = new EventSource('/complete');
}
