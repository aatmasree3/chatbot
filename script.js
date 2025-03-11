function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    fetch("http://127.0.0.1:5000/chat", {  // Ensure it matches Flask URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += `<p>User: ${userInput}</p><p>Bot: ${data.response}</p>`;
        document.getElementById("user-input").value = ""; // Clear input
    });
}
