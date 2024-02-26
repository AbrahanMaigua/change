let intervalo;
let contador;
let totalSeconds = 0;
const MAX_SECONDS = 86400; // 24 horas en segundos
const counterElement = document.getElementById('counter');
const sendLinkElement = document.getElementById('sendLink');

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
    const hours   = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    counterElement.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

function sendcheking() {
    const timeT =  document.getElementById("counter")
    let tiempoInicial = timeT.textContent;
    let totalSeconds = obtenerSegundos(tiempoInicial);

    const hours   = pad(Math.floor(totalSeconds / 3600));
    const minutes = pad(Math.floor((totalSeconds % 3600) / 60));
    const seconds = pad(totalSeconds % 60);
    if (`${seconds}` != '00' || `${minutes}` != '00' || `${hours}` != '00' ) {
        window.location.href = `cheking?hours=${hours}&min=${minutes}&seg=${seconds}`

    } else {
        timeT.classList.add('red');
        console.log(timeT.className)

    }
}

function pad(num) {
    return num.toString().padStart(2, '0');
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

function actualizarContador() {
    let tiempoFormateado = formatearTiempo(contador);

    contador--; // Decrementar el contador
    document.getElementById("counter").textContent = tiempoFormateado; // Actualizar el valor mostrado en el contador

    // Si el contador llega a cero, detenerlo
    if (contador === 0) {
        clearInterval(intervalo); // Detener el contador
        window.location.href = '/'
        
    }
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

function resetCounter(){
    document.getElementById("counter").textContent ='00:00:00';
    textoInicial = document.getElementById("counter").textContent;
    caracteres = textoInicial.split('');
    contador_t = caracteres.length -1;

}
const timeT =  document.getElementById("counter")
let textoInicial = timeT.textContent;
let caracteres   = textoInicial.split('');
let contador_t = caracteres.length -1;

function addNumber(num) {
   

    if (contador_t != -1 && caracteres[contador_t] != ':'  ) {
        caracteres[contador_t] = num.toString();
        contador_t--;
    } else  {
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

function pix(total){
    window.location.href = `pix/${total}`

}

