document.getElementById('query-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const query = document.getElementById('query').value;
    const responseElement = document.getElementById('response');

    try {
        const response = await fetch('http://127.0.0.1:8000/api/ask_bot/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        responseElement.textContent = data.answer;
    } catch (error) {
        responseElement.textContent = 'Error: ' + error.message;
    }
});