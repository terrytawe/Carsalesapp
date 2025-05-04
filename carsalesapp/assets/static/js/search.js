document.getElementById("btn-search").addEventListener("click", function (event) {
  if (event) event.preventDefault();

  const form = document.getElementById("form-search");
  const formData = new URLSearchParams();
  const sortValue = document.getElementById("sort-select").value;

  const elements = form.querySelectorAll("input, select");
  elements.forEach((el) => {
    if (el.name && !el.disabled) {
      if (el.type === "checkbox") {
        if (el.checked) formData.append(el.name, el.value);
      } else {
        formData.append(el.name, el.value);
      }
    }
  });

  if (sortValue) formData.append("sort", sortValue);

  const queryString = formData.toString();
  fetch(`/search-results/?${queryString}`, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    credentials: "same-origin",
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("results-container").innerHTML = data.html;
    })
    .catch((err) => {
      console.error("AJAX search error:", err);
    });
});

document.getElementById("sort-select").addEventListener("change", function () {
  document.getElementById("btn-search").click();
});
