from models.usuarios import obtener_admin

uid = "2RW3HWcWR9SeV9om3igPuQRg8BQ2"  # Usa un UID válido de un admin en tu BD
admin = obtener_admin(uid)

print("Admin obtenido:", admin)
