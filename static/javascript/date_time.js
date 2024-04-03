function addZero(num) {
    return (num < 10 ? '0' : '') + num;
}

function updateDateTime() {
    const now = new Date();
    const formattedDate = `${addZero(now.getDate())}.${addZero(now.getMonth() + 1)}.${now.getFullYear()}`;
    const formattedTime = `${addZero(now.getHours())}:${addZero(now.getMinutes())}`;
    document.getElementById('contener-top-date').textContent = `${formattedDate}`;
    document.getElementById('contener-top-time').textContent = `${formattedTime}`;
}

setInterval(updateDateTime, 1000);
updateDateTime();