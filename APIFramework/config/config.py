import os
from dotenv import load_dotenv

load_dotenv()
token_todo = os.getenv("TOKEN")
token_clickup = os.getenv("TOKEN_CLICKUP")

URL = {    
    "URL_TODO": "https://api.todoist.com/rest/v2/",
    "URL_CLICKUP": "https://api.clickup.com/api/v2/"
}

HEADERS = {
    "HEADERS_TODO": {
        "Authorization": f"Bearer {token_todo}"
    },
    "HEADERS_CLICKUP": {
        "Authorization": f"{token_clickup}",
        "Content-Type": "application/json",
    }
}
abs_path = os.path.abspath(__file__ + "../../../")
TIMEOUT = 10
