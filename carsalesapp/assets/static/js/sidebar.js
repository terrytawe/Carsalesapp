const sidebar = document.getElementById("sidebar");

function toggleSideBar() {
  sidebar.classList.toggle("show");
}

function toggleMenu(button) {
  button.nextElementSibling.classList.toggle("show");
  button.classList.toggle("rotate");
}

function toggleSubMenu(button) {
  button.nextElementSibling.classList.toggle("show");
  button.classList.toggle("rotate");
}
