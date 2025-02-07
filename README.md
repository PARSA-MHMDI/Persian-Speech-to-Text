
# 🎧📝🎯 Automatic Speech Recognition (ASR) System 🎯📝🎧

## 📋 Outline 📋

1. **Project Overview**
2. **Features**
3. **Project Structure**
4. **Configuration Files**
   - ASR Configuration
   - LM Configuration
5. **Installation**
6. **Usage**
   - Data Preprocessing
   - Model Training
   - Inference
7. **Evaluation Metrics**
8. **Results**
9. **Deployment**
10. **Contributing**
11. **License**
12. **Acknowledgments**

## 🚀 Project Overview 🚀

This project focuses on developing an Automatic Speech Recognition (ASR) system using the E-Branchformer model architecture, optimized for Persian language datasets. 🎙️📊🤖

The system leverages the ESPnet toolkit and Mozilla's Common Voice dataset to achieve state-of-the-art performance in Persian ASR tasks. 🌍🔊💡

The project was carried out as part of an internship at **Asr Gooyesh Pardaz Company**, emphasizing the implementation and performance evaluation of ASR models in Persian. 🏢📈🎯

## 🌟 Features 🌟

- **ASR Model:** Based on E-Branchformer architecture for efficient and accurate speech recognition.
- **Language Model (LM):** Transformer-based language model to improve transcription quality.
- **Training Framework:** Utilizes ESPnet with PyTorch backend.
- **Dataset:** Common Voice dataset with Persian language samples.
- **Deployment:** Includes scripts for model training, evaluation, and deployment on servers.

## 📂 Project Structure 📂

```
.
├── asr_config.yaml        # Configuration file for ASR model training
├── config.yaml            # Configuration file for language model training
├── common_voice_ASR.ipynb # Jupyter Notebook for ASR experiments
├── Internship_Report.pdf  # Detailed project report
└── README.md              # Project documentation
```

## ⚙️ Configuration Files ⚙️

### ASR Configuration (`asr_config.yaml`) 🗂️

Key settings:

- **Model:** E-Branchformer with Transformer decoder
- **Training Parameters:** Batch size, learning rate (Adam optimizer), warm-up steps
- **Data:** Paths to training and validation datasets
- **Features:** Global mean-variance normalization

### Language Model Configuration (`config.yaml`) 🗂️

Key settings:

- **Model:** Transformer-based LM
- **Training:** Up to 50 epochs with early stopping
- **Data:** Persian language text datasets

## 🛠️ Installation 🛠️

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository>
   ```

2. **Set up the environment:**

   ```bash
   conda create -n asr_env python=3.8
   conda activate asr_env
   pip install -r requirements.txt
   ```

3. **Install ESPnet:**

   ```bash
   git clone https://github.com/espnet/espnet
   cd espnet
   pip install -e .
   ```

## 🚀 Usage 🚀

### 1️⃣ Preprocess the Data 1️⃣

Prepare the Common Voice dataset:

```bash
./run.sh --stage 0 --stop_stage 1
```

### 2️⃣ Train the ASR Model 2️⃣

```bash
./run.sh --stage 2 --stop_stage 3 --config asr_config.yaml
```

### 3️⃣ Train the Language Model 3️⃣

```bash
./run.sh --stage 4 --stop_stage 5 --config config.yaml
```

### 4️⃣ Decode (Inference) 4️⃣

```bash
./run.sh --stage 6 --stop_stage 6
```

## 📊 Evaluation Metrics 📊

- **Character Error Rate (CER)**
- **Word Error Rate (WER)**

## 🏆 Results 🏆

Achieved:

- **WER:** ~3% on Common Voice Persian dataset
- **CER:** 0.04 on validation data

## 🌐 Deployment 🌐

The model is deployed on Hugging Face servers, enabling online ASR services. 🚀💻🌍

## 🤝 Contributing 🤝

Feel free to fork this repository, submit pull requests, and suggest improvements. 🌟💬✨

## 📜 License 📜

This project is licensed under the MIT License. 📄✅🔐

## 🙏 Acknowledgments 🙏

- **ESPnet**: For providing the open-source ASR framework
- **Mozilla Common Voice**: For the publicly available dataset
- **Asr Gooyesh Pardaz Company**: For support during the internship 🎓🏢🤗
