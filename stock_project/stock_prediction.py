import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
from sklearn.linear_model import LinearRegression

class StockPredictor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.model = LinearRegression()
        self.data = None

    # Load Data
    def load_data(self):
        if not os.path.exists(self.file_path):
            print("❌ stock_data.csv not found!")
            return False

        self.data = pd.read_csv(self.file_path)
        print("✅ Data loaded")
        return True

    # Prepare Data
    def preprocess(self):
        self.data['Target'] = self.data['Close'].shift(-1)
        self.data.dropna(inplace=True)

        X = self.data[['Close']]
        y = self.data['Target']
        return X, y

    # Train Model
    def train(self, X, y):
        self.model.fit(X, y)
        print("✅ Model trained")

    # Save Model
    def save_model(self):
        with open("model.pkl", "wb") as f:
            pickle.dump(self.model, f)
        print("💾 Model saved as model.pkl")

    # Predict
    def predict_next(self, last_price):
        prediction = self.model.predict(np.array([[last_price]]))
        return prediction[0]

    # Plot Data
    def plot(self):
        plt.plot(self.data['Close'])
        plt.title("Stock Closing Prices")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.show()


# ---------- RUN ----------
if __name__ == "__main__":
    predictor = StockPredictor("stock_data.csv")

    if predictor.load_data():
        X, y = predictor.preprocess()
        predictor.train(X, y)
        predictor.save_model()

        last_price = float(input("Enter last closing price: "))
        next_price = predictor.predict_next(last_price)

        print(f"📈 Predicted Next Price: {next_price:.2f}")

        predictor.plot()