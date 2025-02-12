# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from sqlalchemy.types import Enum as SQLAlchemyEnum

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # or use an Enum if desired
    other_details = Column(Text, nullable=True)

    # Relationship definitions (update foreign key references accordingly)
    created_assignments = relationship(
        "Assignment",
        foreign_keys="[Assignment.student_id]",
        back_populates="student"
    )
    assigned_assignments = relationship(
        "Assignment",
        foreign_keys="[Assignment.faculty_id]",
        back_populates="faculty"
    )

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    # Note: Update the foreign key references to match the column name in the users table.
    student_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    faculty_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    submission_date = Column(DateTime, default=datetime.utcnow)
    feedback = Column(Text, nullable=True)

    student = relationship("User", foreign_keys=[student_id], back_populates="created_assignments")
    faculty = relationship("User", foreign_keys=[faculty_id], back_populates="assigned_assignments")
