import tkinter as tk
from tkinter import filedialog
from transformers import pipeline
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Initialize Hugging Face pipeline for image-to-text
image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Function to generate Instagram caption using OpenAI API
def generate_caption(description):
    prompt = f"Generate an Instagram caption for this image: '{description}'"
    response = openai.Completion.create(
        engine="text-davinci",  # You can replace this with another available model
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        stop=["\n"]
    )
    return response.choices[0].text.strip()


# Function to handle image selection and processing
def process_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Get image description
        description = image_to_text(file_path)[0]['generated_text']
        # Generate Instagram caption
        caption = generate_caption(description)
        # Update GUI with caption
        caption_label.config(text=caption)


# GUI setup
root = tk.Tk()
root.title("Image Caption Generator")

# Button to select image
select_button = tk.Button(root, text="Select Image", command=process_image)
select_button.pack(pady=10)

# Label to display generated caption
caption_label = tk.Label(root, text="Generated caption will appear here", wraplength=400)
caption_label.pack(pady=10)

root.mainloop()
