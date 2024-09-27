function toggleTooltip(element) {
    var tooltip = element.querySelector('.tooltip');
    if (tooltip) {
        tooltip.style.display = tooltip.style.display === 'none' ? 'block' : 'none';
    }
}

// Get the header element
const header = document.querySelector('header');

// Function to check scroll position
function checkScroll() {
    // Check if we are past the first page (100vh)
    if (window.scrollY > window.innerHeight) {
        // Add background color to the header
        header.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
        header.style.transition = 'background-color 0.3s';
    } else {
        // Remove background color when on the first page
        header.style.backgroundColor = 'transparent';
    }
}

// Event listener to monitor scroll events
window.addEventListener('scroll', checkScroll);