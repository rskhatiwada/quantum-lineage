// One-click light/dark toggle, overriding Hextra's light/dark/system
// dropdown (see layouts/_partials/theme-toggle.html). setTheme() itself
// comes from the theme's untouched assets/js/head/theme.js.
(function () {
  const toggleButtons = document.querySelectorAll(".hextra-theme-toggle");

  function currentTheme() {
    return document.documentElement.classList.contains("dark") ? "dark" : "light";
  }

  function switchTheme(theme) {
    setTheme(theme);
    localStorage.setItem("color-theme", theme);
  }

  toggleButtons.forEach((btn) => {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      switchTheme(currentTheme() === "dark" ? "light" : "dark");
    });
  });
})();
