
// Toggle password visibility
const togglePassword = document.getElementById('togglePassword');
const passwordField = document.querySelector('input[name="password"]');

togglePassword.addEventListener('click', function () {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

const togglePassword2 = document.getElementById('togglePassword2');
const passwordField2 = document.querySelector('input[name="password2"]');

togglePassword2.addEventListener('click', function () {
    const type = passwordField2.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField2.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});
