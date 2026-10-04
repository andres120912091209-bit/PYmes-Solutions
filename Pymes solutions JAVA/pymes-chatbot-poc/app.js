const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// Base de conocimiento de Pymes Solutions (datos de prueba)
const knowledgeBase = [
    {
        keywords: ["horario", "hora", "abren", "cierran"],
        answer: "Nuestro horario de atención es de lunes a viernes de 8:00 a.m. a 6:00 p.m."
    },
    {
        keywords: ["producto", "productos", "catálogo", "catalogo"],
        answer: "En Pymes Solutions puedes consultar productos desde el módulo de Productos. ¿Deseas información de alguna categoría?"
    },
    {
        keywords: ["precio", "costo", "valor"],
        answer: "Los precios dependen del producto. Puedes revisarlos en el listado de productos del sistema."
    },
    {
        keywords: ["cliente", "registrar", "registro"],
        answer: "Para registrar un cliente debes ingresar nombre, email, teléfono y empresa en el módulo de Clientes."
    },
    {
        keywords: ["contacto", "teléfono", "telefono", "correo", "email"],
        answer: "Puedes contactarnos al correo soporte@pymessolutions.com o al teléfono 300 123 4567."
    },
    {
        keywords: ["pedido", "orden", "compra"],
        answer: "Actualmente puedes gestionar clientes y productos. El módulo de pedidos puede integrarse en una siguiente fase."
    },
    {
        keywords: ["hola", "buenos", "buenas"],
        answer: "¡Hola! Soy el asistente virtual de Pymes Solutions. ¿En qué puedo ayudarte?"
    },
    {
        keywords: ["gracias", "ok", "listo"],
        answer: "¡Con gusto! Si necesitas algo más, aquí estoy."
    }
];

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add("message", sender);
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function getBotAnswer(message) {
    const text = message.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    for (const item of knowledgeBase) {
        if (item.keywords.some(k => text.includes(k))) {
            return item.answer;
        }
    }

    return "No estoy seguro de esa consulta. Puedes reformularla o escribir a soporte@pymessolutions.com para ayuda personalizada.";
}

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";

    setTimeout(() => {
        const answer = getBotAnswer(message);
        addMessage(answer, "bot");
    }, 400);
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

// Mensaje inicial
addMessage("¡Hola! Soy el asistente de Pymes Solutions. Pregúntame por horarios, productos, clientes o contacto.", "bot");