// Toggle password visibility
document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.querySelector('input[name="password"]');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

document.getElementById('togglePassword2').addEventListener('click', function () {
    const passwordField = document.querySelector('input[name="password2"]');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});
