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

@app.get("/test")
def test_proxy():
    return {"message": "FastAPI is working on Vercel!"}


@app.get("/sleeper/picks/{draft_id}")
def get_draft_picks(draft_id: str):
    url = f"https://api.sleeper.app/v1/draft/{draft_id}/picks"
    try:
        response = requests.get(url, timeout=10)  # timeout helps avoid hanging
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {
            "error": "HTTPError",
            "message": str(http_err),
            "url": url
        }
    except requests.exceptions.RequestException as req_err:
        return {
            "error": "RequestException",
            "message": str(req_err),
            "url": url
        }
    except Exception as e:
        return {
            "error": "UnhandledException",
            "message": str(e),
            "url": url
        }