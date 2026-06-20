🌿 Plant Disease Detection
An AI-powered system that detects and classifies plant diseases from leaf images using deep learning. Upload an image of a plant leaf, and the model will identify the disease — helping farmers and agronomists take timely action.
---
📌 Table of Contents
Overview
Features
Demo
Tech Stack
Dataset
Model Architecture
Project Structure
Getting Started
Usage
Results
Contributing
License
---
🧠 Overview
Plant diseases are a major threat to food security worldwide. Early and accurate detection can significantly reduce crop losses. This project uses a Convolutional Neural Network (CNN) trained on thousands of leaf images to automatically classify diseases in plants such as Tomato, Potato, Pepper, Corn, Apple, and more.
---
✨ Features
🔍 Detects 30+ plant diseases across multiple crop types
🌱 Identifies healthy vs. diseased plant leaves
📷 Accepts real-time image uploads
📊 Returns disease name with confidence score
🌐 Web interface for easy interaction
⚡ Fast inference powered by deep learning
---
🎥 Demo
> Upload a leaf image and get instant disease classification.
(Add a screenshot or GIF of your app here)
---
🛠️ Tech Stack
Layer	Technology
Language	Python 3.x
Deep Learning	TensorFlow / Keras or PyTorch
Model	CNN (e.g., ResNet, VGG, or custom)
Web Framework	Flask / FastAPI / Streamlit
Frontend	HTML, CSS, JavaScript (or React)
Dataset	PlantVillage Dataset (via Kaggle)
---
📂 Dataset
This project uses the PlantVillage Dataset, which contains 54,305 images of plant leaves covering 38 disease classes across 14 crop species.
📥 Download: Kaggle - PlantVillage Dataset
Classes include: Healthy, Early Blight, Late Blight, Leaf Mold, Bacterial Spot, and many more.
After downloading, place the dataset in:
```
data/
└── PlantVillage/
    ├── Tomato_Early_blight/
    ├── Tomato_healthy/
    ├── Potato_Late_blight/
    └── ...
```
---
🧬 Model Architecture
The model is a Convolutional Neural Network built with the following structure:
Input: RGB image (224×224)
Convolutional + MaxPooling layers
Batch Normalization + Dropout for regularization
Dense layers with ReLU activation
Output: Softmax (multi-class classification)
> Transfer learning from **ResNet50 / VGG16** pre-trained on ImageNet is used to boost accuracy.
---
📁 Project Structure
```
PlantDiseaseDetection/
├── data/                        # Dataset directory
│   └── PlantVillage/
├── models/                      # Saved trained models
│   └── plant_disease_model.h5
├── notebooks/
│   └── PlantDiseaseDetection.ipynb  # Training & evaluation notebook
├── app/
│   ├── app.py                   # Flask/Streamlit app
│   ├── templates/               # HTML templates
│   └── static/                  # CSS, JS, images
├── utils/
│   └── preprocess.py            # Image preprocessing utilities
├── requirements.txt
└── README.md
```
---
🚀 Getting Started
Prerequisites
Python 3.8+
pip
Git
Installation
```bash
# 1. Clone the repository
git clone https://github.com/Waseetkhan25/PlantDiseaseDetection.git
cd PlantDiseaseDetection

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```
Training the Model
```bash
# Open the Jupyter notebook
jupyter notebook notebooks/PlantDiseaseDetection.ipynb
```
Or train via script (if available):
```bash
python train.py --epochs 20 --batch_size 32
```
Running the Web App
```bash
# Flask
python app/app.py

# OR Streamlit
streamlit run app/app.py
```
Open your browser at `http://localhost:5000` (Flask) or `http://localhost:8501` (Streamlit).
---
🖼️ Usage
Launch the web application.
Upload a clear image of a plant leaf.
Click "Detect Disease".
View the predicted disease name and confidence score.
---
📈 Results
Metric	Value
Training Accuracy	~98%
Validation Accuracy	~95%
Test Accuracy	~94%
Model Size	~100 MB
(Update these values with your actual results)
---
🤝 Contributing
Contributions are welcome! Please follow these steps:
Fork the repository
Create your feature branch: `git checkout -b feature/your-feature`
Commit your changes: `git commit -m 'Add your feature'`
Push to the branch: `git push origin feature/your-feature`
Open a Pull Request
---
📄 License
This project is licensed under the MIT License.
---
🙌 Acknowledgements
PlantVillage Dataset
TensorFlow / Keras Documentation
Kaggle for dataset hosting
---
> Made with ❤️ by [Waseetkhan25](https://github.com/Waseetkhan25)
