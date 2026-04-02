from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
  return {"Name": "mood analysis system",
          "Model": "facebook/bart-large-mnli"
         }

@app.get('/health')
def health():
  return {"status": "ok"}