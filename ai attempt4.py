import openai

# Initialize the OpenAI API client
openai.api_key = 'sk-proj-PrOIhEbSrN3k0ZoSp4pUT3BlbkFJq6AE6gX5PhYBauCcIfTR'

# Generate a caption for the image description using GPT-3
def generate_caption(image_description):
    prompt = f"Generate a caption for the image: {image_description}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Example usage
image_description = "A beautiful landscape with mountains and a lake"
caption = generate_caption(image_description)
print("Generated Caption:", caption)
