from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from db import Base

class Annotation(Base):
    __tablename__ = "annotations"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    predicted_label = Column(String)
    confidence = Column(Float)
    entropy = Column(Float)
    needs_review = Column(Boolean)
    human_corrected_label = Column(String, nullable=True)
    extra_info = Column(JSON, nullable=True)