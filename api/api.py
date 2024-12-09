from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import openai

# Inicializar FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clave de API de OpenAI
openai.api_key = "TU_API_KEY_DE_OPENAI"

@app.post("/generate-blog")
async def generate_blog(
    topic: str = Form(...),
    tone: str = Form(...),
    language: str = Form(...)
):
    try:
        # Crear el prompt para la generación del blog
        prompt = f"""
        Escribe un artículo de blog basado en el siguiente tema: {topic}.
        Tono: {tone}.
        Idioma: {language}.
        Artículo:
        """

        # Llamar a la API de OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
        )

        article = response["choices"][0]["text"].strip()
        return {"article": article}
    except Exception as e:
        return {"error": str(e)}

