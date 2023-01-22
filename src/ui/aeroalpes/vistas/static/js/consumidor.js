window.addEventListener("DOMContentLoaded", () => {
    const messages = document.getElementById("respuestas").createElement("ul");
    document.body.appendChild(messages);
    
    const websocket = new WebSocket("wss://5678-misw4406-tutorial5cqrse-kcm2jfgj6c3.ws-eu83.gitpod.io");
    websocket.onmessage = ({ data }) => {
      const message = document.createElement("li");
      const content = document.createTextNode(data);
      message.appendChild(content);
      messages.appendChild(message);
    };
  });