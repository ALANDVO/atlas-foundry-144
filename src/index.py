from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
import uvicorn
import httpx
import os
import asyncio

app = FastAPI(
    title="atlas-foundry-144",
    description="Free AI/ML model access - DeepSeek V4.1 Flash, Kimi K3 and other frontier models",
    version="0.1.0"
)

# Available models configuration
AVAILABLE_MODELS = {
    "deepseek-v4.1-flash": {
        "name": "DeepSeek V4.1 Flash",
        "provider": "deepseek",
        "free": True,
        "endpoint": "https://api.deepseek.com/v1",
        "description": "Free tier with no usage cap"
    },
    "kimi-k3": {
        "name": "Kimi K3",
        "provider": "kimi",
        "free": True,
        "endpoint": "https://api.kimi.ai/v1",
        "description": "Free tier with no usage cap"
    },
    "glm-5.3-flash": {
        "name": "GLM 5.3 Flash",
        "provider": "z.ai",
        "free": True,
        "endpoint": "https://open.bigmodel.cn/api/v1",
        "description": "Free tier inference"
    }
}

@app.get("/")
async def root():
    return {"message": "atlas-foundry-144 - Free AI/ML model access", "status": "online"}

@app.get("/models")
async def list_models():
    """List available free AI/ML models."""
    return {"models": AVAILABLE_MODELS, "count": len(AVAILABLE_MODELS)}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/v1/{model_id}")
async def get_model_info(model_id: str):
    """Get model information by model ID."""
    if model_id not in AVAILABLE_MODELS:
        raise HTTPException(status_code=404, detail=f"Model {model_id} not found")
    
    model_info = AVAILABLE_MODELS[model_id]
    return {
        "provider": model_info["provider"],
        "model": model_info["name"],
        "free": model_info["free"],
        "endpoint": model_info["endpoint"],
        "description": model_info["description"]
    }

@app.post("/v1/{model_id}/chat")
async def chat_with_model(model_id: str):
    """Chat with a specific model."""
    if model_id not in AVAILABLE_MODELS:
        raise HTTPException(status_code=404, detail=f"Model {model_id} not found")
    
    model_info = AVAILABLE_MODELS[model_id]
    return {
        "provider": model_info["provider"],
        "model": model_info["name"],
        "message": f"Free access to {model_info['name']} - {model_info['description']}",
        "free": True
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
