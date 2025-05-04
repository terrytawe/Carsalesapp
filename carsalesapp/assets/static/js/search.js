/**
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 * Parameter Building
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 */
function buildQueryParams(form, sortSelect = null) {
  const formData = new URLSearchParams();
  const elements = form.querySelectorAll("input, select");

  elements.forEach((el) => {
    if (el.name && !el.disabled) {
      if (el.type === "checkbox") {
        if (el.checked) formData.append(el.name, el.value);
      } else if (el.value.trim() !== "") {
        formData.append(el.name, el.value);
      }
    }
  });

  if (sortSelect && sortSelect.value.trim() !== "") {
    formData.set("sort", sortSelect.value);
  }

  return formData.toString();
}

/**
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 * Search Function
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 */
function performSearch(queryString) {
  const searchUrl = `/search-results/?${queryString}`;
  const newUrl = `/browse/?${queryString}`;
  window.history.replaceState(null, "", newUrl);

  fetch(searchUrl, {
    method: "GET",
    headers: { "X-Requested-With": "XMLHttpRequest" },
    credentials: "same-origin",
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("results-container").innerHTML = data.html;
    })
    .catch((err) => {
      console.error("AJAX search error:", err);
    });
}

/**
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 * Event handling
 * ────────────────────────────────────────────────────────────────────────────────────────────────
 */

//  Search Button
document.getElementById("btn-search").addEventListener("click", function (event) {
  if (event) event.preventDefault();
  const form = document.getElementById("form-search");
  const sortSelect = document.getElementById("sort-select");
  const queryString = buildQueryParams(form, sortSelect);
  performSearch(queryString);
});

// Sort Button
document.getElementById("sort-select").addEventListener("change", function () {
  const currentUrl = new URL(window.location.href);
  const params = currentUrl.searchParams;
  const sortValue = this.value;

  if (sortValue) params.set("sort", sortValue);
  else params.delete("sort");

  performSearch(params.toString());
});

document.getElementById("btn-clear").addEventListener("click", function () {
  const form = document.getElementById("form-search");
  const sortSelect = document.getElementById("sort-select");

  form.reset();
  form.querySelectorAll("input[type=checkbox]").forEach((cb) => (cb.checked = false));
  if (sortSelect) sortSelect.value = "";

  const queryString = buildQueryParams(form, sortSelect);
  performSearch(queryString);
});
