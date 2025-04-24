const sidebar = document.getElementById("sidebar");

function toggleSideBar() {
  sidebar.classList.toggle("show");
}

function toggleMenu(button) {
  button.nextElementSibling.classList.toggle("show");
  button.classList.toggle("rotate");
}

function toggleSubMenu(button) {
  //button.nextElementSibling.classList.toggle("show");
  //button.classList.toggle("rotate");

  const subMenu = button.nextElementSibling;
  const isOpen = subMenu.classList.contains("show");

  document.querySelectorAll(".sub-menu").forEach((menu) => menu.classList.remove("show"));
  document.querySelectorAll(".dropdown-btn").forEach((btn) => btn.classList.remove("rotate"));

  if (!isOpen) {
    subMenu.classList.add("show");
    button.classList.add("rotate");

    localStorage.setItem("activeSidebarMenu", button.dataset.id);
  } else {
    localStorage.removeItem("activeSidebarMenu");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  // Restore the active menu from localStorage
  const activeMenu = localStorage.getItem("activeSidebarMenu");
  if (activeMenu) {
    const submenu = document.querySelector(`.sub-menu[data-parent="${activeMenu}"]`);
    const button = document.querySelector(`.dropdown-btn[data-id="${activeMenu}"]`);
    if (submenu) submenu.classList.add("show");
    if (button) button.classList.add("rotate");
  }

  // Add click handlers to submenu <a> links
  document.querySelectorAll(".sub-menu a").forEach((link) => {
    link.addEventListener("click", function () {
      const parentUl = link.closest(".sub-menu");
      if (parentUl) {
        const menuId = parentUl.dataset.parent;
        localStorage.setItem("activeSidebarMenu", menuId);
      }
    });
  });

  // Optional: highlight active link
  const currentPath = window.location.pathname;
  document.querySelectorAll(".sub-menu a").forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    }
  });
});
