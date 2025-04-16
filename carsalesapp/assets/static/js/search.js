function submitAllFormsAJAX() {
  const forms = ["form1", "form2", "form3", "form4"];
  const formData = new FormData();

  forms.forEach((formId) => {
    const form = document.getElementById(formId);
    const elements = form.querySelectorAll("input, select, textarea");

    elements.forEach((el) => {
      if (el.name && !el.disabled) {
        formData.append(el.name, el.value);
      }
    });
  });

  // Add CSRF token
  const csrfToken = document.getElementById("csrf").value;

  fetch("{% url 'process_form' %}", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken,
    },
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("responseBox").innerText = data;
    })
    .catch((error) => {
      document.getElementById("responseBox").innerText = "Error submitting forms!";
      console.error("Submission error:", error);
    });
}
