from openai import OpenAI
import os
import json
import tempfile

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Min 10 examples
data = [
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Dato base",
        "time": "2015-10-01",
        "value": 562247
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación anual",
        "time": "2015-10-01",
        "value": 19
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Acumulado en lo que va de año",
        "time": "2015-10-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación acumulada",
        "time": "2015-10-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Dato base",
        "time": "2015-11-01",
        "value": 371205
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación anual",
        "time": "2015-11-01",
        "value": 14.04
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Acumulado en lo que va de año",
        "time": "2015-11-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación acumulada",
        "time": "2015-11-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Dato base",
        "time": "2015-12-01",
        "value": 332461
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación anual",
        "time": "2015-12-01",
        "value": 7.94
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Acumulado en lo que va de año",
        "time": "2015-12-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación acumulada",
        "time": "2015-12-01",
        "value": None
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Dato base",
        "time": "2016-01-01",
        "value": 397420
    },
    {
        "autonomous_community": "Madrid, Comunidad de",
        "data_type": "Tasa de variación anual",
        "time": "2016-01-01",
        "value": 14.05
    }
]

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.jsonl') as temp:
    for item in data:
        # Crear mensajes para simular una conversación
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"¿Cuál es el {item['data_type']} para la comunidad autónoma {item['autonomous_community']} en la fecha {item['time']}?"},
            {"role": "assistant", "content": f"El {item['data_type']} para la comunidad autónoma {item['autonomous_community']} en la fecha {item['time']} es {item['value'] if item['value'] is not None else 0}."}
        ]
        conversation = {"messages": messages}
        temp.write(json.dumps(conversation) + '\n')

client.files.create(
    file=open(temp.name, "rb"),
    purpose="fine-tune"
)

os.remove(temp.name)

print('File uploaded to: https://platform.openai.com/storage/files')
