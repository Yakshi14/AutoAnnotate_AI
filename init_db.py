from db import engine, Base
from models import Annotation

Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")