"""Model availability checking for atlas-foundry-144"""

import httpx
import asyncio
from typing import Dict, List, Optional

# Model configuration with endpoints
MODEL_CONFIGS = {
    "deepseek-v4.1-flash": {
        "name": "DeepSeek V4.1 Flash",
        "provider": "deepseek",
        "free": True,
        "check_url": "https://api.deepseek.com/v1/models",
        "description": "Free tier with no usage cap"
    },
    "kimi-k3": {
        "name": "Kimi K3",
        "provider": "kimi",
        "free": True,
        "check_url": "https://api.kimi.ai/v1/models",
        "description": "Free tier with no usage cap"
    },
    "glm-5.3-flash": {
        "name": "GLM 5.3 Flash",
        "provider": "z.ai",
        "free": True,
        "check_url": "https://open.bigmodel.cn/api/v1/models",
        "description": "Free tier inference"
    }
}


async def check_model_availability(model_id: str, timeout: float = 5.0) -> Optional[Dict]:
    """Check if a model is currently available."""
    if model_id not in MODEL_CONFIGS:
        return None
    
    config = MODEL_CONFIGS[model_id]
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(config["check_url"])
            if resp.status_code == 200:
                return {"available": True, "config": config}
    except Exception:
        pass
    return {"available": False, "config": config}


async def get_available_models() -> Dict[str, Dict]:
    """Get all models with their availability status."""
    results = {}
    async with httpx.AsyncClient() as client:
        tasks = []
        for model_id in MODEL_CONFIGS:
            tasks.append(check_model_availability(model_id))
        results_dict = await asyncio.gather(*tasks)
        
    for model_id, result in zip(MODEL_CONFIGS.keys(), results_dict):
        results[model_id] = result
    
    return results


def get_model_info(model_id: str) -> Optional[Dict]:
    """Get model configuration info."""
    return MODEL_CONFIGS.get(model_id)
