from backend.database import Base, engine
from backend import models  # ВАЖНО: чтобы модели зарегистрировались

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
