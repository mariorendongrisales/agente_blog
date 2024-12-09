const form = document.getElementById('blog-form');
const resultContainer = document.getElementById('result-container');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const topic = document.getElementById('topic').value;
    const tone = document.getElementById('tone').value;
    const language = document.getElementById('language').value;

    try {
        result.textContent = "Generando artículo...";
        
        const response = await fetch('/api/generate-blog', {
            method: 'POST',
            body: new URLSearchParams({
                topic: topic,
                tone: tone,
                language: language,
            }),
        });

        const data = await response.json();
        result.textContent = data.article || "Hubo un error al generar el artículo.";
    } catch (error) {
        result.textContent = "Error al conectar con el servidor.";
    }
});

