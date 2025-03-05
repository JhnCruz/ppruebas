import os

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 8080

# Clave API para Flowice (Integrada por otra persona)
FLOWICE_API_KEY = os.getenv("FLOWICE_API_KEY", "clave_por_definir")
