const socket = new WebSocket('ws://localhost:8765');

socket.addEventListener('open', function (event) {
    console.log('Connected to WS Server');
});

socket.addEventListener('message', function (event) {
    console.log('Message from WS Server: ', event.data);
    const response = document.getElementById('response');
    const p = document.createElement('p');
    p.innerHTML = interpreteMD(event.data);
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

function interpreteMD(message) {
    // Find all the emojis, the title and the bold, italic and underline text and replace them
    // with the HTML tags
    const emojis = message.match(/:([a-z]+):/g);
    const title = message.match(/# (.+)/);
    const title2 = message.match(/## (.+)/);
    const title3 = message.match(/### (.+)/);
    const bold = message.match(/\*\*(.+)\*\*/g);
    const italic = message.match(/_(.+)_/g);
    const underline = message.match(/__(.+)__/g);
    if (emojis) {
        for (let i = 0; i < emojis.length; i++) {
            message = message.replace(emojis[i], getEmojiByName(emojis[i].replace(/:/g, '')));
        }
    }
    if (title) {
        message = message.replace(title[0], '<h1>' + title[1] + '</h1>');
    }
    if (title2) {
        message = message.replace(title2[0], '<h2>' + title2[1] + '</h2>');
    }
    if (title3) {
        message = message.replace(title3[0], '<h3>' + title3[1] + '</h3>');
    }
    if (bold) {
        for (let i = 0; i < bold.length; i++) {
            message = message.replace(bold[i], '<b>' + bold[i].replace(/\*\*/g, '') + '</b>');
        }
    }
    if (italic) {
        for (let i = 0; i < italic.length; i++) {
            message = message.replace(italic[i], '<i>' + italic[i].replace(/_/g, '') + '</i>');
        }
    }
    if (underline) {
        for (let i = 0; i < underline.length; i++) {
            message = message.replace(underline[i], '<u>' + underline[i].replace(/__/g, '') + '</u>');
        }
    }
    return message;
}

function getEmojiByName(name) {
    switch (name) {
        case 'smile' || 'smiley':
            return '😀';
        case 'grin':
            return '😁';
        case 'joy':
            return '😂';
        case 'rofl':
            return '🤣';
        case 'sweat_smile':
            return '😅';
        case 'laughing':
            return '😆';
        case 'wink' || ';)':
            return '😉';
        case 'blush':
            return '😊';
        case 'yum':
            return '😋';
        case 'sunglasses':
            return '😎';
        case 'heart_eyes':
            return '😍';
        case 'kissing_heart':
            return '😘';
        case 'kissing':
            return '😗';
        case 'kissing_smiling_eyes':
            return '😙';
        case 'kissing_closed_eyes':
            return '😚';
        default:
            return '';
    }
}