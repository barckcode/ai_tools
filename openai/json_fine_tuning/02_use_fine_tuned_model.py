from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

completion = client.chat.completions.create(
    # replace with the corresponding model
    model="ft:gpt-3.5-turbo-0125:organization::id",
    messages=[
        {"role": "system", "content": "You are an expert assistant in tourism data for the community of Madrid"},
        {"role": "user", "content": "\u00bfCu\u00e1l es el Tasa de variaci\u00f3n anual para la comunidad aut\u00f3noma Madrid, Comunidad de en la fecha 2016-01-01?"}
    ]
)
print(completion.choices[0].message)
