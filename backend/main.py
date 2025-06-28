from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import base64
import requests
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        base64_img = base64.b64encode(image_bytes).decode()

        payload = {
            "model": "llava",
            "prompt": "Describe this image in detail.",
            "images": [base64_img],
            "stream": True
        }

        # Stream from Ollama
        response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
        response.raise_for_status()

        # Join streamed chunks of response text
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_data = json.loads(line)
                    full_response += json_data.get("response", "")
                except json.JSONDecodeError:
                    continue  # ignore bad chunks

        return {
            "result": full_response.strip(),
            "success": True
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Ollama is not running or unreachable at localhost:11434.",
            "success": False
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }
