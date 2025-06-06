from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from db import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    attendance = Column(Float)
    assignment_score = Column(Float)
    exam_score = Column(Float)
    risk_prediction = Column(String(20))
    prediction_date = Column(DateTime, default=datetime.utcnow)
