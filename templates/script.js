const chatForm = document.getElementById("chat-form");
const chatHistory = document.getElementById("chat-history");
const userInput = document.getElementById("user-input");

chatForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent form submission
  const userText = userInput.value;

  // Send user input to the Python backend using AJAX
  fetch("/", {
    method: "POST",
    body: JSON.stringify({ user_input: userText }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle successful response
      chatHistory.innerHTML += `<p>You: ${userText}</p>`;
      chatHistory.innerHTML += `<p>Cybersecurity Chatbot: ${data}</p>`;
      userInput.value = ""; // Clear input field
      scrollToBottom(); // Scroll to the bottom of chat history
    })
    .catch((error) => {
      // Handle error response
      console.error("Error:", error);
      // Display a user-friendly error message in the chat history
      chatHistory.innerHTML += `<p class="error">Oops, something went wrong. Please try again.</p>`;
    });
});

function scrollToBottom() {
  chatHistory.scrollTop = chatHistory.scrollHeight;
}
