document.getElementById("btn-search").addEventListener("click", function (event) {
  if (event) event.preventDefault();

  const form = document.getElementById("form-category");
  const formData = new URLSearchParams();

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

  const queryString = formData.toString();
  fetch(`/ajax/search/?${queryString}`, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    credentials: "same-origin",
  })
    .then((response) => response.text())
    .then((html) => {
      const parser = new DOMParser();
      const newDoc = parser.parseFromString(html, "text/html");
      const newResults = newDoc.getElementById("results-container");
      document.getElementById("results-container").innerHTML = newResults.innerHTML;
    })
    .catch((err) => {
      console.error("AJAX search error:", err);
    });
});
