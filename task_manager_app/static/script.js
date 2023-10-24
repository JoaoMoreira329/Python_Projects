function toggleNightMode() {
    const body = document.body;
    const table = document.getElementById('Table');
    const isNightMode = body.classList.contains('night-mode');

    body.classList.toggle('night-mode');
    table.classList.toggle('night-mode');

    localStorage.setItem('nightMode', !isNightMode);
}

document.addEventListener('DOMContentLoaded', function () {
    const isNightMode = localStorage.getItem('nightMode');
    const body = document.body;
    const table = document.getElementById('Table');

    if (isNightMode === 'true') {
        body.classList.add('night-mode');
        table.classList.add('night-mode');
    }
});
