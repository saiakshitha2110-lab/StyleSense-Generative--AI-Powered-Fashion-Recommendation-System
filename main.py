from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from engine import FashionEngine
from typing import List, Optional
import uvicorn

app = FastAPI(title="StyleSense Pro API")

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = FashionEngine()

class PreferenceSchema(BaseModel):
    gender: str
    age: str
    occasion: str
    style: str
    budget: str

@app.get("/")
def read_root():
    return {"message": "Welcome to StyleSense Pro API"}

@app.post("/recommendations")
def get_recommendations(prefs: PreferenceSchema):
    try:
        # Pydantic V2 uses model_dump(), V1 uses dict()
        # Using model_dump() with a fallback for maximum compatibility
        data = prefs.model_dump() if hasattr(prefs, 'model_dump') else prefs.dict()
        results = engine.get_recommendations(data)
        return {"recommendations": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/trends")
def get_trends():
    try:
        trends = engine.get_trend_insights()
        return {"trends": trends}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
