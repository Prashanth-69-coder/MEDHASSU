from ..database import get_client
import uuid
from supabase import Client
from datetime import datetime

supabase: Client = get_client()

def check_schedule_conflict(user_id: str, scheduled_time: datetime):
    response = supabase.table("schedules")\
        .select("*")\
        .eq("user_id", user_id)\
        .eq("scheduled_time", scheduled_time)\
        .execute()
    return len(response.data) > 0

def create_schedule(user_id: str, interview_type: str, domain: str, scheduled_time: datetime):
    if check_schedule_conflict(user_id, scheduled_time):
        raise ValueError("Schedule conflict for this time.")

    schedule_id = str(uuid.uuid4())
    schedule_data = {
        "id": schedule_id,
        "user_id": user_id,
        "interview_type": interview_type,
        "domain": domain,
        "scheduled_time": scheduled_time,
        "status": "Scheduled"
    }
    response = supabase.table("schedules").insert(schedule_data).execute()
    if response.error:
        raise Exception("Failed to create schedule.")
    return schedule_data
