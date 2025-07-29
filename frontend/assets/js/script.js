// script.js

// Toggle do menu mobile
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
    });
  }

  // Marca link ativo conforme a página
  const navItems = document.querySelectorAll('.nav-links a');
  navItems.forEach(link => {
    if (link.href === window.location.href) {
      link.classList.add('active');
    }
  });
});
