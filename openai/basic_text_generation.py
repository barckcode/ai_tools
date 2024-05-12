from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


system_prompt = "Eres un experto en historia"
user_prompt = "¿En qué año se descubrió América?"


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)

print(completion.choices[0].message)
