import replicate

input = {
    "width": 768,
    "height": 768,
    "prompt": "Imagine a soldier from a pre-Columbian society transported to the 21st century. The image should depict this soldier wearing traditional armor influenced by ancient Mesoamerican or South American cultures, yet subtly integrated with modern elements reflective of today’s technology. The soldier stands in a contemporary urban setting, showcasing a contrast between the ancient and modern worlds. This fusion should be visually striking, highlighting both the historical authenticity of the pre-Columbian armor and the futuristic adaptations made to it.",
    "refine": "expert_ensemble_refiner",
    "apply_watermark": False,
    "num_inference_steps": 25
}

output = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input=input
)
print(output)
