document.getElementById('registerForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const response = await fetch('/accounts/register/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    });

    if (response.ok) {
        alert('Registration successful!');
    } else {
        alert('Something went wrong. Please try again later.');
    }
});
