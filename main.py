from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from openai import OpenAI

# Create FastAPI app
app = FastAPI()

# Load environment variables
load_dotenv()

# Define the request model
class TextRequest(BaseModel):
    input_text: str = Field(default="Mi aplicación es una Web estática", min_length=5, max_length=100)

# Initialize OpenAI client with key
client = OpenAI(api_key=os.getenv("OPENAPI_API_KEY"))

# Define the function to process the request
def generate_response(input_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": "Te llamas MeLiMA (Asistente Mercado Libre Modelado de Amenazas). Debes recibir una descripción de la aplicación web del usuario y devolver solo un JSON con la lista de las 3 principales amenazas potenciales de seguridad con dos campos: descripción breve y sugerencia general de mitigacion. Por favor, sigue el formato de salida esperado como en este ejemplo: [{'descripción': 'Exposición de Información Personal', 'mitigación': 'Implementar un mecanismo de autenticación y autorización robusto para proteger la información personal de los usuarios.'}]. Utiliza para ellos como base el OWASP Top Ten y el CWE/SANS Top 25."                
            },            
            {
                "role": "assistant", 
                "content": "Hola, soy MeLiMA, un asistente de modelado de amenazas. Puedo ayudarte a identificar amenazas de seguridad en tus aplicaciones y sistemas. Describe tu aplicación y te ayudaré a identificar amenazas de seguridad."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        max_tokens=180,
        temperature=0.6
    )

    return response.choices[0].message.content.strip()

# Define the root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de MeLiMA, asistente de Me rcado Li bre para M odelado de A menazas. Te ayudo a identificar amenazas de seguridad en tus aplicaciones y sistemas. Descríbeme tu aplicación y te entregaré un listado de amenazas con sugerencias de mitigación.",
        "endpoints": {
            "chat": "/chat - POST para enviar la descripción de tu aplicación y recibir un listado de amenazas"
        }
    }
    
# Define the chat endpoint
@app.post("/chat")
async def chat_completion(request: TextRequest):
    try:
        response = generate_response(request.input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))