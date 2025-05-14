# 🚗 Car Evaluation Dataset Analysis

This project analyzes the UCI Car Evaluation dataset using Python with `pandas`, `matplotlib`, `seaborn`, and `ucimlrepo`. It demonstrates how to load, clean, analyze, and visualize data for insights.

---

## 📂 Dataset Info

- **Source:** UCI Machine Learning Repository (Dataset ID: 19)
- **Attributes:** buying, maint, doors, persons, lug_boot, safety, class
- **Type:** All attributes are categorical

---

## 📌 Features

### ✅ Data Processing
- Loads dataset using `ucimlrepo`
- Checks for and handles missing values
- Maps categorical class values for numerical analysis

### 📊 Data Analysis
- Summary statistics for categorical features
- Grouped means of class ratings by other attributes

### 📈 Visualizations (Saved in `plots/`)
- **Bar Chart:** Class distribution
- **Stacked Bar Chart:** Class by safety rating
- **Histogram:** Lug_boot distribution
- **Scatter Plot:** Buying vs maintenance cost (colored by class)

---

## 📦 Requirements

Install the required packages:

```bash
pip install ucimlrepo pandas matplotlib seaborn

🚀 How to Run
Run the Python script:
python car_evaluation_analysis.py

📁 Output
All plots will be saved in a folder named plots.

📈 Key Observations
Most cars fall under the unacc category.

Higher safety ratings tend to be associated with more acceptable cars.

Buying and maintenance costs influence class ratings significantly.

🧑‍💻 Author
Developed for a data analysis assignment using Python and UCI datasets.
