
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const adminText = document.querySelector('.admin-text');
    const toggleBtn = document.querySelector('.toggle-btn i');

    sidebar.classList.toggle('collapsed');
    if (sidebar.classList.contains('collapsed')) {
        adminText.style.display = 'none'; // Hide admin text
        toggleBtn.classList.replace('fa-angle-double-left', 'fa-angle-double-right');
    } else {
        adminText.style.display = 'inline'; // Show admin text
        toggleBtn.classList.replace('fa-angle-double-right', 'fa-angle-double-left');
    }
}
