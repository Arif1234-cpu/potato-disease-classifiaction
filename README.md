# 🥔 Potato Disease Detection Using Deep Learning

An end-to-end **deep learning and computer vision application** for identifying potato leaf diseases from images.

The project uses a trained TensorFlow/Keras image-classification model and a **Streamlit-based interactive interface**, allowing users to upload a potato leaf image and obtain a predicted disease category.

---

## 🔬 Project Overview

Potato diseases can significantly affect crop health and agricultural productivity. Early identification of visible disease symptoms can help in taking timely preventive or management measures.

This project explores the application of **deep learning-based image classification** for automated potato leaf disease identification.

The system follows the pipeline:

**Leaf Image → Image Preprocessing → Deep Learning Model → Prediction → Streamlit Interface**

The project focuses on connecting a trained computer vision model with an accessible application interface rather than limiting the work to model training alone.

---

## 🎯 Objectives

* Apply deep learning to a real-world agricultural problem.
* Develop an image classification system for potato leaf diseases.
* Process and prepare leaf images for model inference.
* Integrate the trained model into an interactive application.
* Provide predictions through a simple Streamlit interface.
* Explore practical considerations involved in deploying machine learning models.

---

## 🧠 Machine Learning Approach

The system uses a trained **TensorFlow/Keras image classification model**.

During inference, an uploaded potato leaf image is processed into the format expected by the model. The model then generates prediction scores for the learned disease categories.

The predicted class is presented to the user through the Streamlit application.

### Inference Pipeline

```text
                Potato Leaf Image
                        │
                        ▼
                Image Preprocessing
                        │
                        ▼
                Trained DL Model
                        │
                        ▼
                 Model Prediction
                        │
                        ▼
                Predicted Disease
                        │
                        ▼
              Streamlit Application
```

---

## 🌱 Disease Classification

The model is trained to distinguish between the disease categories represented in its training dataset.

The application predicts the class of an uploaded potato leaf image based on the visual patterns learned by the model.

> The actual supported classes depend on the dataset and trained model used in this project.

---

## 🛠️ Technology Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Core development                |
| TensorFlow   | Deep learning                   |
| Keras        | Model development and inference |
| NumPy        | Numerical operations            |
| Pillow       | Image processing                |
| Streamlit    | Interactive ML application      |
| Git & GitHub | Version control                 |

---

## 🖥️ Application

The project uses **Streamlit** to provide an interactive interface for model inference.

Users can:

1. Open the application.
2. Upload a potato leaf image.
3. Preview the uploaded image.
4. Run the trained model.
5. View the predicted disease category.

This makes the trained model accessible without requiring users to interact directly with Python code.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Potato-disease.git
```

Navigate to the project:

```bash
cd Potato-disease
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Replace `app.py` with the actual name of your Streamlit entry file if it is different.

Streamlit will provide a local URL where the application can be opened in a browser.

---

 
## 🔎 Research Perspective

The project provides a foundation for investigating the use of deep learning in agricultural disease identification.

Several research questions can be explored further:

 
### 2. Data Augmentation

Investigate whether augmentation improves generalization to variations in:

* Resize
* Scale
 
### 3. Generalization

A model trained on controlled images may not perform equally well on images captured in real agricultural environments.

Testing with different lighting conditions, backgrounds, cameras, and field environments would provide a stronger assessment of real-world robustness.

### 4. Explainable AI

Methods such as **Grad-CAM** could be used to visualize which regions of a leaf contribute most strongly to the model's prediction.

This could help determine whether the model is focusing on visually meaningful disease symptoms.

### 5. Lightweight Deployment

The model could be optimized for resource-constrained environments through techniques such as:

* Model compression
* Quantization
* Lightweight architectures

This could make the system more suitable for mobile or edge-based agricultural applications.

---

## ⚠️ Limitations

The current application should be considered an educational and experimental system rather than a replacement for professional agricultural diagnosis.

Potential limitations include:

* Predictions depend on the quality of the input image.
* Different lighting conditions may affect performance.
* Backgrounds may differ from those represented in the training data.
* Visually similar symptoms can lead to incorrect classifications.
* Dataset bias may affect generalization.
* Real-world field performance may differ from test-set performance.

Therefore, model predictions should not be treated as definitive agricultural diagnoses.

---

## 🚀 Future Improvements

* [ ] Compare multiple CNN and transfer-learning architectures
* [ ] Perform detailed model evaluation
* [ ] Add confusion matrix visualization
* [ ] Add prediction confidence scores
* [ ] Investigate data augmentation strategies
* [ ] Implement Grad-CAM visualizations
* [ ] Evaluate performance on real-world images
* [ ] Optimize the model for lightweight deployment
* [ ] Deploy the Streamlit application publicly
* [ ] Investigate model robustness and generalization

---

## 📌 Project Status

**Status:** In Development

The current version demonstrates:

* Deep learning-based image classification
* Potato leaf disease prediction
* Image preprocessing
* TensorFlow/Keras model inference
* Interactive Streamlit deployment

Further development can focus on systematic experimentation, model comparison, robustness evaluation, and explainable AI.

---

## 👨‍💻 Author

**Mohammad Arif Khan**

B.Tech Computer Engineering
Aligarh Muslim University

**Interests:** Machine Learning · Deep Learning · Computer Vision · MLOps · Software Engineering 

---
