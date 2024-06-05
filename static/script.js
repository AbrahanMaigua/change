let intervalo;
let isactivecronometro = false;

let totalSeconds = 0;
const MAX_SECONDS = 86400; // 24 horas en segundos
const counterElement = document.getElementById('counter');
const sendLinkElement = document.getElementById('sendLink');

console.log(counterElement)
console.log(counterElement)

const timeT      =  document.getElementById("counter")
let textoInicial = timeT.textContent;
let caracteres   = textoInicial.split('');
// Declarar la variable globalmente
let contador_t;

// Asignar su valor en el lugar adecuado, por ejemplo, dentro de una función de inicialización
function inicializarContador(caracteres) {
    contador_t = caracteres.length - 2;
}

// Llamar a la función de inicialización con el array 'caracteres'
inicializarContador(caracteres);


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
    if (`${seconds}` != '00' || `${minutes}` != '00' || `${hours}` != '00') {
          sendLinkElement.href = `cheking?hours=${hours}&min=${minutes}&seg=${seconds}`;


    } else {
        counterElement.classList.add('red');
        console.log(counterElement.className)
    }
}

function updateCounter() {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    counterElement.textContent = `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
}

function sendcheking() {
    const timeT       = document.getElementById("counter")
    let tiempoInicial = timeT.textContent;
    let totalSeconds  = obtenerSegundos(tiempoInicial);

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
    console.log(isactivecronometro)
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
    let horas        = parseInt(partesTiempo[0]);
    let minutos      = parseInt(partesTiempo[1]);
    let segundos     = parseInt(partesTiempo[2]);
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
    contador_t = caracteres.length -1;
}


let currentTimeInSeconds = 0;

function incrementTimeBy(number) {
    // Convert the number into hours, minutes, and seconds
    let hours = Math.floor(number / 3600);
    let minutes = Math.floor((number % 3600) / 60);
    let seconds = number % 60;

    // Convert the old current time to hours, minutes, and seconds
    let currentHours = Math.floor(currentTimeInSeconds / 3600);
    let currentMinutes = Math.floor((currentTimeInSeconds % 3600) / 60);
    let currentSeconds = currentTimeInSeconds % 60;

    // Add the new values
    currentSeconds += seconds;
    if (currentSeconds >= 60) {
        currentMinutes += Math.floor(currentSeconds / 60);
        currentSeconds = currentSeconds % 60;
    }

    currentMinutes += minutes;
    if (currentMinutes >= 60) {
        currentHours += Math.floor(currentMinutes / 60);
        currentMinutes = currentMinutes % 60;
    }

    currentHours += hours;
    if (currentHours >= 24) {
        currentHours = currentHours % 24;
    }

    // Update the current time in seconds
    currentTimeInSeconds = (currentHours * 3600) + (currentMinutes * 60) + currentSeconds;

    // Format the time as 00:00:00
    let formattedHours = String(currentHours).padStart(2, '0');
    let formattedMinutes = String(currentMinutes).padStart(2, '0');
    let formattedSeconds = String(currentSeconds).padStart(2, '0');

    // Update the timer element
    document.getElementById('counter').textContent = `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}




function addNumber(num) {
    console.log('Ejecutando addNumber con contador_t:', contador_t, 'y num:', num);

    while (contador_t >= 0) {
        if (caracteres[contador_t] !== ':') {
            let temp = caracteres[contador_t]; // Guardamos el valor actual en una variable temporal
            caracteres[contador_t] = String(num) // Colocamos el nuevo número en la posición actual
            contador_t--; // Movemos el contador una posición hacia atrás
            num = temp; // Actualizamos num para la siguiente iteración
        } else {
            contador_t--; // Si estamos en ':' o al inicio de la cadena, solo movemos el contador
        }
    }
    // Actualizamos solo los caracteres modificados en el texto mostrado
    let Seg = obtenerSegundos(caracteres.join(''));
    if (Seg > MAX_SECONDS) {
        Seg = MAX_SECONDS;
    }

    let timeT = document.getElementsByClassName('timeT');
    console.log(timeT.textContent)
    timeT.textContent = formatearTiempo(Seg);
    //timeT.classList.remove('red');
}

function pix(total, pedido_id) {
    window.location.href = `pix/${pedido_id}`
}

function completeStatusCarga() {
    const eventSource = new EventSource('/complete');
        eventSource.onmessage = function(event) {
            console.log(event.data)
        };
};

function actualizarCronometro() {
    const counterElement = document.getElementById('counter');
    let totalseg         = obtenerSegundos(counterElement.textContent); // Obtener el contenido del elemento
    let tiempoRestante   = totalseg;

    // Función para convertir el tiempo en formato HH:MM:SS a segundos
    function obtenerSegundos(tiempo) {
        let partesTiempo = tiempo.split(":");
        let horas        = parseInt(partesTiempo[0]);
        let minutos      = parseInt(partesTiempo[1]);
        let segundos     = parseInt(partesTiempo[2]);
        return horas * 3600 + minutos * 60 + segundos;
    }
   
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
    completeStatusCarga()
    return setInterval(actualizarCronometro, 900);
}
function startcronometro() {
    // Cuando se hace clic en el botón, se inicia el cronómetro
    if (isactivecronometro === false) {
        isactivecronometro = true
        iniciarCronometro();

        document.getElementById('startButton').remove()
        document.getElementById('back').remove()
        document.getElementById('intruciones').remove()
        

       


    }
};

// uso en caso de fallas de eletricidad
var queryString = window.location.search;

// Verifica si la cadena de consulta contiene el parámetro deseado 
if (queryString.includes("startauto")) {
    // Llama a la función si estás en la página deseada y el parámetro existe
    startcronometro();
}
