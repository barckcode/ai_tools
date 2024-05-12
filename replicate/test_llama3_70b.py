import replicate


prompt = f"What is the capital of Spain?"

# The meta/meta-llama-3-70b-instruct model can stream output as it's running.
for event in replicate.stream(
    "meta/meta-llama-3-70b-instruct",
    input={
        "top_k": 0,
        "top_p": 0.9,
        "prompt": "Como se hace una tortilla de patata?",
        "max_tokens": 512,
        "min_tokens": 0,
        "temperature": 0.6,
        "system_prompt": "You are a data analyst specialized in tourism",
        "length_penalty": 1,
        "stop_sequences": "<|end_of_text|>,<|eot_id|>",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a data analyst specialized in tourism<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15,
        "log_performance_metrics": False
    },
):
    print(str(event), end="")
