function submitAllFormsAJAX(event) {
  if (event) event.preventDefault();
  const forms = ["form-category", "form-pricing", "form-features"];
  const formData = new URLSearchParams();

  forms.forEach((id) => {
    const form = document.getElementById(id);
    if (!form) return;

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
  });

  const queryString = formData.toString();
  fetch(`/search-results/?${queryString}`, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
    credentials: "same-origin",
    body: null,
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
}
