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
    const fishIcon = document.querySelector('.fish-icon');
    if (this.checked) {
        fishIcon.classList.add('shake');
        const data = await sendRequest('/start');

        console.log(data);

    } else {
        const data = await sendRequest('/stop');
        console.log(data);
        fishIcon.classList.remove('shake');
    }
});

window.addEventListener('keydown', function(event) {
    // Check if the pressed key combination is Shift + Alt + F
    if (event.shiftKey && event.altKey && (event.key === 'f' || event.key === 'F')) {
        // Get the toggleSwitch element
        const toggleSwitch = document.getElementById('toggleSwitch');
        // Change the checked property to its opposite value
        toggleSwitch.checked = !toggleSwitch.checked;

        // Trigger the change event
        toggleSwitch.dispatchEvent(new Event('change'));
    }
});

// Array of sentences
const sentences = [
  "\"Oh, fishing is such a blast! Nothing says 'fun' like sitting for hours, staring at water, and pretending it's a thrilling adventure.\"",
  "\"I love how fishing combines the excitement of watching paint dry with the thrill of doing absolutely nothing for hours on end.\"",
  "\"The joy of fishing is unparalleled. Nothing like the adrenaline rush of reeling in...absolutely nothing.\"",
  "\"They say fishing is a sport, but I think it's more of a meditative practice in patience. Because who needs excitement anyway?\"",
  "\"Fishing: where the real action happens is in convincing yourself that this is a riveting way to spend your time.\"",
  "\"The excitement of fishing is like a rollercoaster ride – if the rollercoaster were on pause for several hours between each 'thrilling' moment.\"",
  "\"Nothing beats the exhilaration of hooking a seaweed monster. Truly, the stuff of legends.\"",
  "\"Fishing is like a box of chocolates, except you're stuck with the same bland flavor for hours and hours.\"",
  "\"They said fishing is a great stress reliever. Probably because stressing about catching anything takes your mind off other worries.\"",
  "\"Fishing: because who needs the rush of victory when you can have the calm satisfaction of tangled lines and lost bait?\"",
  "\"If you enjoy the thrill of suspense, try fishing. Will you catch something exciting? Probably not, but the suspense is killing you, right?\"",
  "\"The best part of fishing is when the fish get to enjoy the story of how you almost caught them but then didn't.\"",
  "\"Fishing is a wonderful bonding experience. Nothing brings people together like collectively wondering why you're sitting there in the first place.\"",
  "\"They said fishing builds character. I didn't realize they meant the character to withstand extreme levels of boredom.\"",
  "\"Fishing: where the phrase 'It's the journey, not the destination' really means 'It's the napping, not the fishing.'\"",
  "\"Spending your time fishing – because who needs productivity and meaningful activities, right?\"",
  "\"Is fishing the new extreme sport of sitting? Because sitting for hours is truly pushing the boundaries of excitement.\"",
  "\"You know what's a great use of time? Not fishing. Seriously, have you considered doing something... anything else?\""
];

const Philosophers = [
  "Arthur Schopenhauer",
  "Friedrich Nietzsche",
  "Emil Cioran",
  "Jean-Paul Sartre",
  "Albert Camus",
  "Thomas Ligotti",
  "Peter Wessel Zapffe",
  "Giacomo Leopardi",
  "Martin Heidegger",
  "Philipp Mainländer"
];

// Function to pick a random sentence
// Function to pick a random item from an array
function getRandomItem(array) {
    const index = Math.floor(Math.random() * array.length);
    return array[index];
}

// Function to display a random sentence and philosopher
function displayRandomContent() {
    const sentence = getRandomItem(sentences);
    const philosopher = getRandomItem(Philosophers);

    const wildQuotes = document.getElementById('wild-quotes');
    wildQuotes.classList.remove('fade-out');
    wildQuotes.classList.add('fade');

    document.getElementById('random-sentence').textContent = sentence;
    document.getElementById('random-philosopher').textContent = philosopher;

    setTimeout(() => {
        wildQuotes.classList.remove('fade');
        wildQuotes.classList.add('fade-out');
    }, 8000);
}

// Display random content initially
displayRandomContent();

// Update the content every 5 seconds
setInterval(displayRandomContent, 12000);
