// === Scroll Header Animation Script ===
// This script listens for page scrolls and toggles a 'scrolled' class on <body>
// When added, the CSS animation in style.css shrinks and darkens the header.

(function() {
  // Helper function to check scroll position
  const handleScroll = () => {
    const header = document.querySelector('.header');
    if (!header) return;

    // If the user scrolls down more than 20px, shrink the header
    if (window.scrollY > 20) {
      document.body.classList.add('scrolled');
    } else {
      document.body.classList.remove('scrolled');
    }
  };

  // Add event listeners for scroll and page load
  window.addEventListener('scroll', handleScroll);
  document.addEventListener('DOMContentLoaded', handleScroll);

  // Optional: smooth show on first load
  window.addEventListener('load', () => {
    const header = document.querySelector('.header');
    if (header) {
      header.style.transition = 'all 0.3s ease';
    }
  });
})();
