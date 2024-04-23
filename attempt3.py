import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.applications.efficientnet import preprocess_input
from keras.models import load_model

# Load your trained model
model = load_model('your_model_path.h5')

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def generate_caption(image_path):
    img = preprocess_image(image_path)
    caption = model.predict(img)
    return caption

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img)
        panel.image = img

        # Generate caption
        caption = generate_caption(file_path)
        messagebox.showinfo("Caption", caption)

# Create main window
root = tk.Tk()
root.title("Image Captioning")

# Create panel for displaying image
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Create button to select image
btn = tk.Button(root, text="Select Image", command=select_image)
btn.pack(pady=5)

root.mainloop()
