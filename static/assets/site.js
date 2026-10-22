(() => {
  const current = location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.sidebar nav a').forEach(link => {
    const path = new URL(link.href).pathname.replace(/\/$/, '') || '/';
    if (current === path) link.setAttribute('aria-current', 'page');
  });
})();
