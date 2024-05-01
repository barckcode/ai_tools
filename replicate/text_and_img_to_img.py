import replicate

# Public IMG
image = "https://i.etsystatic.com/42678828/r/il/ff9f3f/5707804001/il_fullxfull.5707804001_cvcw.jpg";
# Local IMG Example
# import base64

# with open("./path/to/my/image.png", 'rb') as file:
#     data = base64.b64encode(file.read()).decode('utf-8')
#     image = f"data:application/octet-stream;base64,{data}"


input = {
    "width": 768,
    "height": 768,
    "prompt": "Transform this image to black and white",
    "refine": "expert_ensemble_refiner",
    "apply_watermark": False,
    "num_inference_steps": 25,
    "image": image
}

output = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input=input
)
print(output)
