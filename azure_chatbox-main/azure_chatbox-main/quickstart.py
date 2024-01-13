import os
from openai import AzureOpenAI
   
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2023-12-01-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

response = client.chat.completions.create(
    model="GPT35TURBO16K",
    messages = [{"role":"system", "content":"you are an English assistant and you can only respond in english"},
                {"role": "assistant", "content": "Hello, I'm your English assistant. How can I help you?"},]
)
print(response.choices[0].message.content)