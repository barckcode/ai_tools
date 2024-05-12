from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

client.fine_tuning.jobs.create(
    # replaced by the corresponding file
    training_file="file-M5u930aOSRUz7k2AVVAnZePL",
    model="gpt-3.5-turbo"
)

print('Go to Fine-tuning section: https://platform.openai.com/finetune')
