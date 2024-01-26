async function sendRequest(url = '', method = 'POST') {
    try {
        const response = await fetch(url, {
            method: method,
            cache: 'no-cache'
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.text();
        console.log('Server response:', data);
        return data;
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        alert('There was a problem with the request. Please try again later.');
    }
}

document.querySelector('button[name="start"]').addEventListener('click', async function (event) {
    event.preventDefault();
    const data = await sendRequest('/start');
    console.log(data);
});

document.querySelector('button[name="stop"]').addEventListener('click', async function(event) {
    event.preventDefault();
    const data = await sendRequest('/stop');
    console.log(data);
});

function closeWindow() {
    fetch('/close')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Handle the response here
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            alert('There was a problem with the request. Please try again later.');
        });
}

document.querySelector('button[name="close"]').addEventListener('click', closeWindow);

document.addEventListener('DOMContentLoaded', function () {
    let url = document.location;
    let route = "/flaskwebgui-keep-server-alive";
    let interval_request = 3 * 1000; //sec
    function keep_alive_server() {
        sendRequest(url + route, 'GET')
            .then(data => console.log(data));
    }

    setInterval(keep_alive_server, interval_request);
});