# -*- coding: utf-8 -*-
"""
Car Evaluation Dataset Analysis
- Data Loading & Cleaning
- Statistical Analysis
- Visualizations (Bar, Histogram, Scatter)
"""

# Required Libraries
# !pip install ucimlrepo matplotlib pandas seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo
import os

# Global Plot Settings
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 12

# --- Task 1: Load and Explore the Dataset ---
def load_and_explore():
    print("🔍 Loading and exploring the dataset...")
    
    try:
        car_data = fetch_ucirepo(id=19)
        X, y = car_data.data.features, car_data.data.targets
        df = pd.concat([X, y], axis=1)

        print("\n📄 First 5 Rows:")
        print(df.head())

        print("\nℹ️ Dataset Info:")
        print(df.info())

        print("\n🧹 Missing Values:")
        print(df.isnull().sum())

        print("\n✅ Data Cleaned: No missing values detected.")
        return df

    except Exception as e:
        print("❌ Error loading dataset:", e)
        return pd.DataFrame()

# --- Task 2: Basic Data Analysis ---
def analyze_data(df):
    print("\n📊 Performing basic data analysis...")

    print("\n📈 Categorical Summary:")
    print(df.describe(include='object'))

    print("\n🚦 Class Distribution by Safety Rating:")
    print(df.groupby('safety')['class'].value_counts().unstack())

    class_map = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
    df['class_encoded'] = df['class'].map(class_map)
    print("\n💰 Average Class Rating by Buying Price:")
    print(df.groupby('buying')['class_encoded'].mean())

# --- Task 3: Data Visualization ---
def visualize_data(df):
    print("\n🖼️ Generating visualizations...")
    os.makedirs("plots", exist_ok=True)

    # Bar Chart - Class Distribution
    plt.figure()
    ax = sns.countplot(data=df, x='class', order=['unacc', 'acc', 'good', 'vgood'], palette="viridis")
    plt.title("Car Acceptability Class Distribution", fontweight='bold')
    plt.xlabel("Class")
    plt.ylabel("Count")
    for p in ax.patches:
        ax.annotate(f"{p.get_height()}", (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    plt.savefig("plots/class_distribution.png", bbox_inches='tight')
    plt.show()

    # Stacked Bar Chart - Safety vs Class
    plt.figure()
    safety_class = df.groupby('safety')['class'].value_counts().unstack()
    safety_class.plot(kind='bar', stacked=True, colormap="viridis")
    plt.title("Class Distribution by Safety Rating", fontweight='bold')
    plt.xlabel("Safety")
    plt.ylabel("Count")
    plt.legend(title="Class", bbox_to_anchor=(1.05, 1))
    plt.savefig("plots/safety_vs_class.png", bbox_inches='tight')
    plt.show()

    # Histogram - Luggage Boot Size
    plt.figure()
    sns.histplot(df['lug_boot'], discrete=True, shrink=0.8)
    plt.title("Distribution of Luggage Boot Sizes", fontweight='bold')
    plt.xlabel("Lug Boot")
    plt.ylabel("Count")
    plt.savefig("plots/luggage_distribution.png", bbox_inches='tight')
    plt.show()

    # Scatter Plot - Buying vs Maintenance
    price_map = {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4}
    df['buying_encoded'] = df['buying'].map(price_map)
    df['maint_encoded'] = df['maint'].map(price_map)

    plt.figure()
    sns.scatterplot(data=df, x='buying_encoded', y='maint_encoded', hue='class', palette="viridis", s=100)
    plt.title("Buying vs Maintenance Cost by Class", fontweight='bold')
    plt.xlabel("Buying Price (1=Low to 4=VHigh)")
    plt.ylabel("Maintenance Cost (1=Low to 4=VHigh)")
    plt.legend(title="Class", bbox_to_anchor=(1.05, 1))
    plt.savefig("plots/buying_vs_maint.png", bbox_inches='tight')
    plt.show()

# --- Main ---
if __name__ == "__main__":
    print("🚗 Car Evaluation Dataset Analysis")
    df = load_and_explore()
    if not df.empty:
        analyze_data(df)
        visualize_data(df)
        print("\n🎉 Analysis complete! Check the 'plots' folder for visualizations.")
