// Function to toggle the sidebar
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var content = document.querySelector('.content');
    var employeeText = document.querySelector('.employee-text'); // Select the Employee text
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
    employeeText.classList.toggle('d-none'); // Hide employee text when sidebar is collapsed
}