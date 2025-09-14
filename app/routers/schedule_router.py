from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from ..services import schedule_service

router = APIRouter()

class ScheduleRequest(BaseModel):
    user_id: str
    interview_type: str
    domain: str
    scheduled_time: datetime

@router.post("/schedule")
async def create_schedule(schedule: ScheduleRequest):
    try:
        schedule_data = schedule_service.create_schedule(
            schedule.user_id,
            schedule.interview_type,
            schedule.domain,
            schedule.scheduled_time,
        )
        return {"message": "Interview scheduled successfully", "schedule_id": schedule_data["id"]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
