from langflow.load import run_flow_from_json
from dotenv import load_dotenv

TWEAKS = {
    "TextInput-XjIKI": {
        "input_value": "question"
    },
    "TextInput-176Ns": {
        "input_value": "answer"
    },
}

result = run_flow_from_json("flow.json",input_value="message", fallback_to_env_vars=True, tweaks=TWEAKS)