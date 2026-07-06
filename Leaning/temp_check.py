import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5"
token = os.environ.get("GITHUB_TOKEN")
print("token repr:", repr(token))
try:
    cred = AzureKeyCredential(token)
    print("credential created", cred)
    client = ChatCompletionsClient(endpoint=endpoint, credential=cred)
    print("client created")
except Exception as e:
    import traceback
    traceback.print_exc()
