async function send(ip, port) {
    const message = document.getElementById('message').value;
    const ws = new WebSocket(`ws://${ip}:${port}`);
    ws.onopen = () => {
        ws.send(message);
    };
    ws.onmessage = (e) => {
        const response = document.getElementById('response');
        response.innerHTML = response.innerHTML + `<p>${e.data}</p>`;
    };
}

document.getElementById('send').addEventListener('click', () => {
    send('localhost', 8765);
});