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
    }
}

document.getElementById('toggleSwitch').addEventListener('change', async function () {
    console.log('Toggle switch changed')
    const fishIcon = document.querySelector('.fish-icon');
    console.log('Fish Icon:', fishIcon); // Log the fishIcon
    if (this.checked) {
        console.log('Toggle switch is checked')
        console.log('Checked status:', this.checked); // Log the checked status
        fishIcon.classList.add('shake');
        const data = await sendRequest('/start');

        console.log(data);

    } else {
        console.log('Toggle switch is not checked')
        console.log('Checked status:', this.checked); // Log the checked status
        const data = await sendRequest('/stop');
        console.log(data);
        fishIcon.classList.remove('shake');
    }
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
        });
}