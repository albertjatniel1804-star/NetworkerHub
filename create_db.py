from app.database.connection import create_tables
from app.models.user import User

create_tables()

print("Base de datos creada correctamente.")
