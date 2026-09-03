# 🌸 Rose Color Classification using PyTorch & EfficientNet-B0

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Torchvision](https://img.shields.io/badge/Torchvision-0055FF?style=for-the-badge&logo=pytorch&logoColor=white)
![EfficientNet-B0](https://img.shields.io/badge/Model-EfficientNet--B0-brightgreen?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Test_Accuracy-100%25-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)

A PyTorch-based Deep Learning project for classifying rose flower colors (*rose color classification*) into 4 distinct color categories using fine-tuned **EfficientNet-B0** via Transfer Learning.

---

## 📌 Table of Contents
- [About The Project](#-about-the-project)
- [Dataset](#-dataset)
- [Architecture & Data Augmentation](#-architecture--data-augmentation)
- [Hyperparameters & Training](#-hyperparameters--training)
- [Results & Model Evaluation](#-results--model-evaluation)
- [Project Structure](#-project-structure)
- [Installation & Usage Guide](#-installation--usage-guide)
- [Dependencies](#-dependencies)

---

## 📖 About The Project

This project aims to build a high-precision Computer Vision model capable of identifying and categorizing rose flower colors from visual imagery. By leveraging the state-of-the-art **EfficientNet-B0** architecture pre-trained on ImageNet, the model achieves exceptional feature extraction and classification performance across flower petal textures and color tones.

### 🌟 Key Features
- **Transfer Learning**: Utilizes pre-trained weights (`EfficientNet_B0_Weights.DEFAULT`) for fast convergence and ultra-high accuracy.
- **Robust Data Augmentation**: Prevents overfitting using random cropping, horizontal flipping, random rotation, and color jittering.
- **Stratified Dataset Splitting**: Methodical split into 70% Training, 15% Validation, and 15% Test sets.
- **Comprehensive Evaluation**: Evaluated using Confusion Matrix, Loss/Accuracy curves, and classification metrics (Precision, Recall, F1-Score).

---

## 📊 Dataset

The dataset is sourced from Kaggle:
- **Dataset Name**: [`maulikgajera/rose-color-classification-dataset`](https://www.kaggle.com/datasets/maulikgajera/rose-color-classification-dataset)
- **Number of Classes**: 4 Rose Colors
  1. **Pink**
  2. **Red**
  3. **White**
  4. **Yellow**

### ✂️ Data Splitting
Data is split using a stratified approach based on class labels:

| Data Subset | Percentage | Number of Samples |
| :--- | :---: | :---: |
| **Train Set** | 70% | ~2,100 images |
| **Validation Set** | 15% | ~450 images |
| **Test Set** | 15% | 450 images |

---

## 🏗️ Architecture & Data Augmentation

### 1. Data Augmentation (*Pipeline Transforms*)
- **Training Pipeline**:
  - `Resize & RandomResizedCrop` (224x224, scale 0.8–1.0)
  - `RandomHorizontalFlip` ($p=0.5$)
  - `RandomRotation` (up to $\pm 15^\circ$)
  - `ColorJitter` (brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1)
  - Standard ImageNet Normalization ($\mu = [0.485, 0.456, 0.406]$, $\sigma = [0.229, 0.224, 0.225]$)
- **Validation & Test Pipeline**:
  - `Resize` (224x224)
  - Standard ImageNet Normalization

### 2. Model Architecture
- **Base Backbone**: `torchvision.models.efficientnet_b0`
- **Custom Classifier Head**:
  - Modified Linear layer: `nn.Linear(in_features=1280, out_features=4)`

---

## ⚙️ Hyperparameters & Training

- **Image Resolution**: $224 \times 224$ pixels
- **Batch Size**: 32
- **Epochs**: 20
- **Learning Rate**: $1 \times 10^{-4}$ ($0.0001$)
- **Optimizer**: `AdamW` ($\text{weight\_decay} = 1\times 10^{-4}$)
- **Loss Function**: `CrossEntropyLoss`
- **Early Stopping**: Patience = 5 Epochs (saves optimal model weights as `best_efficientnet_b0.pth`)
- **Device**: CUDA GPU / CPU

---

## 📈 Results & Model Evaluation

The model was evaluated on an unseen, independent **Test Set** of 450 images.

### 🏆 Performance Summary
- **Test Accuracy**: **100.00%**
- **Test Loss**: **0.0002**
- **Best Validation Accuracy**: **100.00%**

### 📋 Classification Report (Test Set)

| Class | Precision | Recall | F1-Score | Support (Images) |
| :--- | :---: | :---: | :---: | :---: |
| **Pink** | 1.0000 | 1.0000 | 1.0000 | 135 |
| **Red** | 1.0000 | 1.0000 | 1.0000 | 180 |
| **White** | 1.0000 | 1.0000 | 1.0000 | 60 |
| **Yellow** | 1.0000 | 1.0000 | 1.0000 | 75 |
| **Overall / Macro Avg** | **1.0000** | **1.0000** | **1.0000** | **450** |

---

## 📁 Project Structure

```text
Flower color classification/
│
├── pytorch-based-rose-color-classification.ipynb   # Main Jupyter Notebook (Data prep, EDA, training & evaluation)
├── requirements.txt                                 # Python package dependencies
└── README.md                                        # Project documentation
```

---

## 🚀 Installation & Usage Guide

### 1. Prerequisites
- Python 3.8 or higher.
- A GPU with CUDA support is recommended for accelerated training/inference.

### 2. Navigate to Project Directory
Open your terminal or Command Prompt and change to the project directory:
```bash
cd "C:\latihan\Summer Project\Flower color classification"
```

### 3. Install Dependencies
Install all necessary Python dependencies using:
```bash
pip install -r requirements.txt
```

### 4. Run Notebook
Launch Jupyter Notebook or JupyterLab:
```bash
jupyter notebook pytorch-based-rose-color-classification.ipynb
```
Alternatively, open the `.ipynb` file in VS Code, Google Colab, or Kaggle.

---

## 📦 Dependencies

Required packages listed in [`requirements.txt`](file:///C:/latihan/Summer%20Project/Flower%20color%20classification/requirements.txt):
- `torch`
- `torchvision`
- `numpy`
- `pandas`
- `Pillow`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `tqdm`
- `kagglehub`

---

## 🤝 License & Notes

Developed as part of the **Summer Project - Flower Color Classification**. Free to use and adapt for learning or computer vision experiments using PyTorch.
