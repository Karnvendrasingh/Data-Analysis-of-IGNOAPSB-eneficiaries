
## 📊 Beneficiary Data Analysis & Visualization using Python

### 📝 Overview
This project explores a real-world **beneficiary dataset** using **Pandas**, **Matplotlib**, and **Seaborn** in Python. The aim is to analyze demographic and Aadhaar/mobile availability data **state-wise and district-wise**, clean inconsistencies, and visualize insights effectively.

---

### 🎯 Objectives
- Clean and preprocess the dataset.
- Perform **descriptive** and **comparative** analysis.
- Visualize data by **state**, **district**, and **caste category**.
- Analyze availability of **Aadhaar** and **Mobile numbers**.
- Detect and visualize **outliers** in beneficiary counts.

---

### 🧹 Data Cleaning Steps
- Removed rows where:
  - Aadhaar > Total Beneficiaries
  - Mobile > Total Beneficiaries
- Checked rows where SC + ST + OBC + GEN ≠ Total Beneficiaries.
- Standardized state name:  
  `"THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU"` ➔ `"DNH & DIU"`

---

### 📈 Visualizations Used
| Plot Type     | Description |
|---------------|-------------|
| **Bar Plot** (Horizontal) | Total beneficiaries by state |
| **Bar Plot** (Vertical)   | Top 5 districts by beneficiaries |
| **Bar Plot** (Vertical)   | Beneficiaries by caste (SC/ST/OBC/GEN) |
| **Pie Charts**            | Aadhaar and Mobile availability analysis |
| **Scatter Plot**          | Correlation between Aadhaar and Beneficiaries |
| **Box Plot**              | Outlier detection for beneficiary data |

---

### 📌 Key Insights
- Identified top 5 and bottom 5 districts by beneficiaries.
- Found correlation between Aadhaar and total beneficiaries.
- Detected mismatches in caste-wise and total values.
- Calculated Aadhaar/Mobile penetration rates.
- Outliers were detected using **IQR-based boxplot**.

---

### 🛠️ Technologies Used
- **Python 3.9+**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Jupyter Notebook / VS Code**

---

### ▶️ How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/beneficiary-analysis.git
   cd beneficiary-analysis
   ```
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the notebook or script:
   ```bash
   python beneficiary_analysis.py
   ```
4. Make sure your dataset is named `Dataset.csv` and is in the same directory.

---

### 📂 Folder Structure
```
beneficiary-analysis/
├── Dataset.csv
├── beneficiary_analysis.py
├── README.md
```

---

### 🙌 Acknowledgements
Thanks to the data providers and inspiration from real-world government datasets for public welfare analysis.
