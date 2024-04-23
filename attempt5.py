import os
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="http://localhost:9001",  # only local hosting supported
    api_key=os.environ["ROBOFLOW_API_KEY"]
)

result = CLIENT.prompt_cogvlm(
    visual_prompt="./grad.jpg",
    text_prompt="Generate a caption for this image.",
)
print(result)