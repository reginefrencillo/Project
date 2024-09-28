// Function to toggle the sidebar
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var content = document.querySelector('.content');
    var farmerText = document.querySelector('.farmer-text');
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
    farmerText.classList.toggle('d-none');
}
