let intervalo;
let contador;
let totalSeconds = 0;
const MAX_SECONDS = 86400; // 24 horas en segundos
const counterElement = document.getElementById('counter');
const sendLinkElement = document.getElementById('sendLink');

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
    sendLinkElement.href = `otra_pagina.html?hours=${hours}&minutes=${minutes}&seconds=${seconds}`;
}

function updateCounter() {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    counterElement.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

function pad(num) {
    return num.toString().padStart(2, '0');
}

// Obtener el tiempo inicial desde el HTML
window.onload = function() {
    let tiempoInicial = document.getElementById("counter").textContent;
    contador = obtenerSegundos(tiempoInicial);
};

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
        window.location.href = '/page.html'
        
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

let textoInicial = document.getElementById("counter").textContent;
    let caracteres = textoInicial.split('');
    let contador_t = caracteres.length -1;
    function resetCounter(){
        document.getElementById("counter").textContent ='00:00:00';
        textoInicial = document.getElementById("counter").textContent;
        caracteres = textoInicial.split('');
        contador_t = caracteres.length -1;

    }

    function addNumber(num) {
        console.log(num)

        if (contador_t != -1 && caracteres[contador_t] != ':'  ) {
            caracteres[contador_t] = num.toString();
            contador_t--;
        } else  {
            contador_t--;
            addNumber(num)
        }
        // Actualizamos solo los caracteres modificados en el texto mostrado
        document.getElementById("counter").textContent = caracteres.join('');
    }

   
    