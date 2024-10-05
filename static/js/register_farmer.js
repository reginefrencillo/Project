const togglePassword = document.querySelector('#togglePassword');
const passwordField = document.querySelector('#id_password');  // Select the password input field

togglePassword.addEventListener('click', function (e) {
    // Toggle the type attribute
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);

    // Toggle the eye / eye-slash icon
    this.classList.toggle('fa-eye-slash');
});
