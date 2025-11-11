document.addEventListener("DOMContentLoaded", function () {
  console.log("Chatbot JS loaded ✅");

  const sendBtn = document.getElementById("send-btn");
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  function appendMessage(sender, message, type) {
    const msg = document.createElement("div");
    msg.classList.add("message");
    msg.classList.add(type === "user" ? "user-message" : "bot-message");
    msg.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("You", message, "user");
    userInput.value = "";

    fetch("/get_response", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Server response:", data);
        appendMessage("ChatBot", data.reply, "bot");
      })
      .catch((error) => {
        console.error("Error:", error);
        appendMessage("Bot", "⚠️ Server not responding. Try again later.", "bot");
      });
  }

  sendBtn.addEventListener("click", sendMessage);
  userInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendMessage();
  });
});
