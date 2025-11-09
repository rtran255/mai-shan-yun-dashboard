// assets/script.js
document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("toggle-header");
  const header = document.getElementById("top-header");
  const sidebar = document.querySelector(".sidebar");

  if (btn && header) {
    btn.addEventListener("click", () => {
      header.classList.toggle("collapsed");
      if (sidebar) sidebar.classList.toggle("collapsed");
    });
  }

  function updateNavActive() {
    const radios = document.querySelectorAll(".nav-container input[type='radio']");
    radios.forEach((r) => {
      const id = r.id;
      const label = document.querySelector(`label[for='${id}']`);
      if (!label) return;
      if (r.checked) label.classList.add("active");
      else label.classList.remove("active");
      label.addEventListener("click", () => {
        radios.forEach((rr) => {
          const lbl = document.querySelector(`label[for='${rr.id}']`);
          if (lbl) lbl.classList.remove("active");
        });
        label.classList.add("active");
      });
    });
  }

  updateNavActive();
  setInterval(updateNavActive, 600);
});
