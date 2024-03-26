document.getElementById("myForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the default form submission

  // Get the value of the input field
  var message = document.getElementById("inputText").value;

  // Send a POST request to the Flask app
  fetch("/process_message", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: message })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("response").innerText = data.message;
  })
  .catch(error => {
    console.error("Error:", error);
  });
});
