# 🧩 F7 – Traceability Notification API

## 📘 Overview
This API ensures that **every notification** is linked to a valid entity —  
`Candidate`, `Requirement`, `Vendor`, `Lead`, or `Case`.  
Messages without an entity link are automatically corrected to maintain full traceability.

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate

2️⃣ Install Requirements
pip install -r requirements.txt

3️⃣ Run the FastAPI App
uvicorn app.main:app --reload

🌐 Swagger URL

Open:
👉 http://127.0.0.1:8000/docs

You’ll see the Traceability API (F7) section.

🧪 Example Request (POST /f7/notifications)
{
  "entity_type": "Case",
  "entity_id": 123,
  "message": "New email received"
}

✅ Expected Response
{
  "status": "success",
  "data": {
    "entity_type": "Case",
    "entity_id": 123,
    "message": "New email received on Case 123",
    "timestamp": "2025-10-07T12:45:00"
  }
}

📁 Output Storage

All notifications are stored in:

data/notifications.json

✅ Swagger Test Success

Once Swagger shows:

"status": "success"


✅ Your F7 Traceability API is successfully running.
