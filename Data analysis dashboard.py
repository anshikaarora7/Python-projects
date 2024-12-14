import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Sample dataset
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [300, 450, 500, 700, 600, 800]
    }
    df = pd.DataFrame(data)

    # Display summary
    print("Dataset Summary:")
    print(df.describe())

    # Plot data
    plt.plot(df["Month"], df["Sales"], marker="o")
    plt.title("Monthly Sales Data")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.show()

analyze_data()