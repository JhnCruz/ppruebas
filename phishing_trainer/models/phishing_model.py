class PhishingMessage:
    def __init__(self, tipo, mensaje, es_phishing):
        self.tipo = tipo
        self.mensaje = mensaje
        self.es_phishing = es_phishing

class PhishingExamples:
    def __init__(self, email, scam, sms, web):
        self.email = email
        self.scam = scam
        self.sms = sms
        self.web = web

class PhishingQuestion:
    def __init__(self, opcionA, opcionB, opcionC, respuesta_correcta):
        self.opcionA = opcionA
        self.opcionB = opcionB
        self.opcionC = opcionC
        self.respuesta_correcta = respuesta_correcta
