# Machine Learning Algorithms for Stock Price Prediction

This project uses historical data of the Bank Nifty index over the last 10 years to predict future stock prices using Machine Learning models. It features a web-based client to visualize the predictions.

## ✨ Screenshot

![Web App Screenshot](docs/Screenshot%202025-07-19%20101951.png)

## 🚀 Features

- **Multiple Models**: Implements and experiments with both LSTM (Long Short-Term Memory) and XGBoost models for price prediction.
- **Data-Driven**: Trained on 10 years of historical Bank Nifty index data.
- **Web Interface**: A Svelte-based frontend to display historical data and model predictions.
- **Flask Backend**: A Python-based backend to serve the trained models and data.

## 🛠️ Tech Stack

- **Backend**:
  - Python
  - Flask
  - Waitress
  - TensorFlow / Keras
  - XGBoost
  - NumPy
  - Pandas

- **Frontend**:
  - Svelte
  - Vite.js
  - Chart.js

- **Data & Modeling**:
  - Jupyter Notebooks for data analysis and model experimentation.

## 📂 Project Structure

```
.
├── client/         # Svelte frontend application
├── server/         # Flask backend server
├── model/          # Saved model files (.h5, .pkl)
├── data/           # Raw and processed data files (.csv)
├── *.ipynb         # Jupyter notebooks for experimentation
└── README.md
```

## 🏁 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- `pip` and `npm`

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name/server/ml-with-stocks
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Frontend Setup

1.  **Navigate to the client directory:**
    ```bash
    cd ../../client
    ```

2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```

## 🏃‍♂️ Usage

1.  **Run the Backend Server:**
    From the `server/ml-with-stocks` directory, start the Flask server.
    ```bash
    waitress-serve --host 127.0.0.1 --port 5000 app:app
    ```
    The server will be running at `http://127.0.0.1:5000`.

2.  **Run the Frontend Client:**
    From the `client` directory, start the Vite development server.
    ```bash
    npm run dev
    ```
    The client will be available at `http://localhost:3000` (or another port if 3000 is busy).

## 🧠 Model Training

The Jupyter notebooks (`.ipynb` files) in the `notebooks` directory contain the code for data preprocessing, model training, and evaluation. You can explore these notebooks to understand the different strategies used for training the LSTM and XGBoost models.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## 📄 License

This project is open-source. See the [LICENSE](LICENSE) file for details.
