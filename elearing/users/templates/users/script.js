// script.js
document.getElementById('login-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get input values
    const miNumber = document.getElementById('mi-number').value.trim();
    const password = document.getElementById('password').value.trim();

    // Simple validation
    if (!miNumber || !password) {
        alert('Please fill in all fields.');
        return;
    }

    // Simulate login (replace with actual API call in a real application)
    console.log('MI Number:', miNumber);
    console.log('Password:', password);

    // Redirect to dashboard or show success message
    alert('Login successful! Redirecting to dashboard...');
    // window.location.href = '/dashboard'; // Redirect to dashboard
});