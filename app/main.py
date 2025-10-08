from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas import NotificationCreate
from app.models import Notification
from app.database import load_data, save_data

app = FastAPI(
    title="Traceability Notification API",
    description="Every notification must link to a valid entity: Candidate, Requirement, Vendor, Lead, or Case.",
    version="1.0.0"
)

# Custom error for invalid/missing JSON
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid or empty JSON body. Please provide entity_type, entity_id, and message."}
    )

@app.get("/", tags=["Root"])
def root():
    return {"message": "Traceability API is running!"}

@app.post("/notifications", tags=["Notifications"])
def create_notification(request_data: NotificationCreate):
    try:
        new_notification = Notification(
            entity_type=request_data.entity_type,
            entity_id=request_data.entity_id,
            message=request_data.message
        )
        data = load_data()
        data.append(new_notification.to_dict())
        save_data(data)
        return {"status": "success", "data": new_notification.to_dict()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/notifications", tags=["Notifications"])
def get_notifications():
    data = load_data()
    return {"count": len(data), "data": data}
