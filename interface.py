import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the trained model
model_path = r"C:\Users\ramak\OneDrive\Desktop\ML MODELS\corona prediction\covid_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Function for prediction
def predict_covid():
    try:
        # Get values from user input
        age = int(entry_age.get())
        fever = int(entry_fever.get())
        cough = int(entry_cough.get())
        breath_shortness = int(entry_breath.get())
        contact = int(entry_contact.get())

        # Convert input into NumPy array for prediction
        input_data = np.array([[age, fever, cough, breath_shortness, contact]])

        # Predict using the trained model
        prediction = model.predict(input_data)[0]

        # Display result
        result = "COVID Positive" if prediction == 1 else "COVID Negative"
        messagebox.showinfo("Prediction Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create Tkinter window
root = tk.Tk()
root.title("COVID Prediction Model")
root.geometry("350x300")

# Labels and Entry Fields
tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

tk.Label(root, text="Fever (0/1):").grid(row=1, column=0, padx=10, pady=5)
entry_fever = tk.Entry(root)
entry_fever.grid(row=1, column=1)

tk.Label(root, text="Cough (0/1):").grid(row=2, column=0, padx=10, pady=5)
entry_cough = tk.Entry(root)
entry_cough.grid(row=2, column=1)

tk.Label(root, text="Shortness of Breath (0/1):").grid(row=3, column=0, padx=10, pady=5)
entry_breath = tk.Entry(root)
entry_breath.grid(row=3, column=1)

tk.Label(root, text="Contact with Confirmed (0/1):").grid(row=4, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root)
entry_contact.grid(row=4, column=1)

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_covid)
predict_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run application
root.mainloop()
