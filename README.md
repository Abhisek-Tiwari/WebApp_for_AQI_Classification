
# 🌫️ WebApp for AQI Classification

A Python-based web application that predicts Air Quality Index (AQI) categories using a machine learning model. 
Built with Streamlit, it offers an intuitive interface for users to input environmental data and receive AQI classifications.

## 📌 Features

- Interactive web interface for AQI prediction
- Pre-trained machine learning model for classification
- Utilizes a comprehensive pollution dataset
- Environment setup files for easy deployment

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abhisek-Tiwari/WebApp_for_AQI_Classification.git
   cd WebApp_for_AQI_Classification
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the application:**
   ```bash
   streamlit run main.py
   ```

2. **Access the web app:**
   Open your browser and navigate to `http://localhost:8501` to interact with the application.

## 📂 Project Structure

- `main.py`: Main application script utilizing Streamlit.
- `aqi_prediction.pkl`: Serialized machine learning model for AQI classification.
- `updated_pollution_dataset.csv`: Dataset used for training and evaluation.
- `requirements.txt`: Python dependencies.
- `environment.yml`: Conda environment configuration.
- `aqi_image.jpeg`: Visual representation used in the app.

## 🧠 Model Details

The application employs a pre-trained machine learning model (stored in `aqi_prediction.pkl`) to classify AQI levels based on input features. 
The model was trained on the `updated_pollution_dataset.csv`, which contains historical pollution data.

## 📧 Contact

Developed by Abhisek Tiwari

- Email: [it12212043@gmail.com](mailto:it12212043@gmail.com)
- GitHub: [Abhisek-Tiwari](https://github.com/Abhisek-Tiwari)
