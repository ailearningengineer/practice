import os
from pathlib import Path

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4o"


def load_env():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]

        os.environ.setdefault(key, value)


load_env()
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise RuntimeError("GITHUB_TOKEN is not set in .env or your environment.")

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(""),
        UserMessage("What is the capital of France?"),
    ],
    model=model,
)

print(response.choices[0].message.content)

