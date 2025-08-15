from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sleeper/picks/{draft_id}")
def get_draft_picks(draft_id: str):
    try:
        url = f"https://api.sleeper.app/v1/draft/{draft_id}/picks"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {
            "error": str(e),
            "url": url,
            "note": "This is a debug message from the server."
        }