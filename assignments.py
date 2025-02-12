# assignments.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Assignment, User
from schemas import AssignmentCreate, FeedbackRequest
from dependencies import get_current_user

assignments_router = APIRouter(prefix="/assignments", tags=["Assignments"])

@assignments_router.get("/")
async def get_assignments():
    return {"message": "List of assignments"}

@assignments_router.post("/submit")
def submit_assignment(
    request: AssignmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "student":
        raise HTTPException(status_code=403, detail="Only students can submit assignments")
    new_assignment = Assignment(title=request.title, student_id=current_user.id)
    db.add(new_assignment)
    db.commit()
    return {"message": "Assignment submitted successfully"}

@assignments_router.get("/review")
def review_assignments(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "faculty":
        raise HTTPException(status_code=403, detail="Only faculty can review assignments")
    assignments = db.query(Assignment).all()
    return {
        "assignments": [
            {"id": a.id, "title": a.title, "student_id": a.student_id, "feedback": a.feedback}
            for a in assignments
        ]
    }

@assignments_router.post("/feedback/{assignment_id}")
def give_feedback(
    assignment_id: int,
    request: FeedbackRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role != "faculty":
        raise HTTPException(status_code=403, detail="Only faculty can provide feedback")
    assignment = db.query(Assignment).filter(Assignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    assignment.feedback = request.feedback
    assignment.faculty_id = current_user.id
    db.commit()
    return {"message": "Feedback submitted successfully"}
