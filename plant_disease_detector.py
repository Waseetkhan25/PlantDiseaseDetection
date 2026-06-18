import tensorflow as tf
import numpy as np
from PIL import Image
import os

# ---------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------

MODEL_PATH = "trained_model.keras"  # Must be in the same folder as this script

disease_classes = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust',
    'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# ---------------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------------

print("=" * 50)
print("   🌿 Plant Disease Detector")
print("=" * 50)
print("\n⏳ Loading AI model, please wait...")

if not os.path.exists(MODEL_PATH):
    print(f"\n❌ ERROR: '{MODEL_PATH}' not found!")
    print("   Download it from: https://github.com/MuhammadAreeb21/Plant-Disease-Project-AI")
    print("   Place it in the same folder as this script.")
    exit()

model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded successfully!\n")

# ---------------------------------------------------------------
# PREDICTION FUNCTION
# ---------------------------------------------------------------

def predict_disease(image_path):
    if not os.path.exists(image_path):
        print(f"❌ Image file not found: {image_path}")
        return

    image = Image.open(image_path)

    # Convert to RGB if needed (handles PNG with transparency, grayscale, etc.)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Resize to model's expected input size
    target_size = model.input_shape[1:3]  # e.g. (128, 128)
    image = image.resize(target_size)

    # Prepare array for model
    image_array = np.array(image).astype(np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    # Predict
    prediction = model.predict(image_array, verbose=0)
    predicted_index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100
    predicted_class = disease_classes[predicted_index]

    # Format output nicely
    parts = predicted_class.split("___")
    plant = parts[0].replace("_", " ")
    disease = parts[1].replace("_", " ") if len(parts) > 1 else "Unknown"

    print("-" * 50)
    print(f"🌱 Plant   : {plant}")
    print(f"🦠 Disease : {disease}")
    print(f"📊 Confidence: {confidence:.2f}%")

    if "healthy" in disease.lower():
        print("🟢 Status  : HEALTHY - No disease detected!")
    else:
        print("🔴 Status  : DISEASED - Treatment may be needed.")
    print("-" * 50)

# ---------------------------------------------------------------
# MAIN LOOP - Keep asking user for images
# ---------------------------------------------------------------

while True:
    print("\nEnter the path to your leaf image (or type 'exit' to quit):")
    user_input = input(">>> ").strip().strip('"').strip("'")

    if user_input.lower() == 'exit':
        print("\n👋 Goodbye!")
        break

    if user_input == "":
        print("⚠️  Please enter a valid path.")
        continue

    predict_disease(user_input)
