import web
import random
from models.phishing_model import PhishingMessage, PhishingExamples, PhishingQuestion

class PhishingController:
    def GET_info(self):
        """Retorna información básica sobre phishing (Flowice lo manejará después)."""
        return "Explicación breve de qué es el phishing..."

    def GET_examples(self):
        """Retorna ejemplos de phishing en formato JSON."""
        tipos = {"email": "Email Phishing", "scam": "Scam Phishing", "sms": "SMS Phishing", "web": "Web Phishing"}
        ejemplos = {tipo: f"Ejemplo de {desc}" for tipo, desc in tipos.items()}
        return web.jsondumps(PhishingExamples(**ejemplos).__dict__)

    def GET_generate_question(self):
        """Genera una pregunta con 3 opciones, donde solo una es phishing."""
        opciones = ["A", "B", "C"]
        respuesta_correcta = random.choice(opciones)

        tipos = ["email", "scam", "sms", "web"]
        ejemplos = [f"Mensaje {i}" for i in range(3)]

        return web.jsondumps(PhishingQuestion(
            opcionA=ejemplos[0], opcionB=ejemplos[1], opcionC=ejemplos[2], respuesta_correcta=respuesta_correcta
        ).__dict__)
