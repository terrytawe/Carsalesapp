const tabItems = document.querySelectorAll(".search-group-item");

tabItems.forEach((tab) => {
  tab.addEventListener("click", function (e) {
    e.preventDefault();

    // Remove 'active' class from all tabs and panes
    tabItems.forEach((t) => t.classList.remove("active"));

    // Add 'active' to clicked tab
    this.classList.add("active");

    // Show the matching tab pane
    const target = this.getAttribute("data-tab");
    document.getElementById(target).classList.add("active");
  });
});

function toggleMenu(button) {
  button.nextElementSibling.classList.toggle("show");
  button.classList.toggle("rotate");
}
