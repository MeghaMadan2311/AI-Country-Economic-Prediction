import pandas as pd
import matplotlib.pyplot as plt


def perform_eda(file_path="data.csv"):
    data = pd.read_csv(file_path)

    print("Dataset shape:", data.shape)
    print("\nDataset summary:")
    print(data.describe())

    # GDP Growth visualization
    plt.figure(figsize=(10, 6))
    plt.bar(data["country"], data["gdp_growth"])
    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("GDP Growth (%)")
    plt.title("GDP Growth by Country")
    plt.tight_layout()
    plt.savefig("gdp_growth.png")
    plt.close()

    # Inflation visualization
    plt.figure(figsize=(10, 6))
    plt.bar(data["country"], data["inflation"])
    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Inflation (%)")
    plt.title("Inflation by Country")
    plt.tight_layout()
    plt.savefig("inflation.png")
    plt.close()


if __name__ == "__main__":
    perform_eda()
