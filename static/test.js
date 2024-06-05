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
