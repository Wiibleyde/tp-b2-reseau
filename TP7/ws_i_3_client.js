const socket = new WebSocket('ws://localhost:8765');

socket.addEventListener('open', function (event) {
    console.log('Connected to WS Server');
});

socket.addEventListener('message', function (event) {
    console.log('Message from WS Server: ', event.data);
    const response = document.getElementById('response');
    const p = document.createElement('p');
    p.innerHTML = event.data;
    response.appendChild(p);
    response.scrollTop = response.scrollHeight;
});

document.getElementById('send').addEventListener('click', function () {
    const message = document.getElementById('message').value;
    const username = document.getElementById('username').value;
    if (message === '' || username === '') {
        return;
    }
    document.getElementById('message').value = '';
    socket.send(username + ': ' + message);
});

document.getElementById('message').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) {
        const message = document.getElementById('message').value;
        const username = document.getElementById('username').value;
        if (message === '' || username === '') {
            return;
        }
        document.getElementById('message').value = '';
        socket.send(username + ': ' + message);
    }
});