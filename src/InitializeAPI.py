from fastapi import FastAPI, HTTPException
import uvicorn
import nest_asyncio
import torch
from threading import Thread
from BuildModel import MoodClassification

nest_asyncio.apply()
app = FastAPI()

mood_classifier = MoodClassification('config.yaml')
@app.get('/')
def read_root():
  return {
          "Name": "Mood Analysis System",
          "Model": "facebook/bart-large-mnli"
         }

@app.get('/health')
def health():
    # Kiểm tra xem model đã được khởi tạo chưa
    model_status = "ready" if mood_classifier is not None else "loading"

    # Kiểm tra thiết bị phần cứng đang sử dụng
    device = "cuda (GPU)" if torch.cuda.is_available() else "cpu"
    # Tính thời gian server đã chạy (Uptime)


    return {
        "status": "healthy",
        "details": {
            "model_name": "facebook/bart-large-mnli",
            "model_status": model_status,
            "device": device,
            "memory_usage": "stable"
        }
    }

@app.post('/CLImood')
def post_mood(message: str):
  if not message or len(message.strip()) == 0:
        raise HTTPException(status_code=400, detail="Message không được để trống")
  try:
    mood = mood_classifier(message)
    return {
        "status": "ok",
        "data": {
            "mood": mood
        }
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Chạy server trong thread riêng
thread = Thread(target=run_server, daemon=True)
thread.start()
print("Server started on http://0.0.0.0:8000")