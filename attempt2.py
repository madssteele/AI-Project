import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import AutoProcessor, AutoModelForSeq2SeqLM

# Load model directly
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/blip-image-captioning-large")

def generate_caption(image_path):
    try:
        # Read the image file
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        # Tokenize and preprocess the image
        inputs = processor(image_bytes, return_tensors="pt", padding=True)

        # Generate caption for the provided image
        outputs = model.generate(**inputs)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        
        return caption
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the selected image
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Resize the image to fit in the GUI
        photo = ImageTk.PhotoImage(image)

        # Update the image on the GUI
        image_label.config(image=photo)
        image_label.image = photo

        # Generate caption for the selected image
        caption = generate_caption(file_path)
        if caption is not None:
            caption_label.config(text="Caption: " + caption)
        else:
            caption_label.config(text="Caption: Caption not available")

# Create the main application window
app = tk.Tk()
app.title("Image Caption Generator")

# Create widgets
image_label = tk.Label(app)
select_button = tk.Button(app, text="Select Image", command=select_image)
caption_label = tk.Label(app, text="Caption: ")

# Layout widgets
image_label.pack(pady=10)
select_button.pack(pady=5)
caption_label.pack(pady=5)

# Run the application
app.mainloop()
