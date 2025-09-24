# Grocery Sales Forecasting

## Project Setup

This project uses the **Grocery Sales Forecasting** dataset from Kaggle.  
👉 Dataset: [https://www.kaggle.com/datasets/littlesaplings/grocery-sales-forecasting-parquet](https://www.kaggle.com/datasets/littlesaplings/grocery-sales-forecasting-parquet)

### 1. Clone this Repository

git clone https://github.com/<your-username>/grocery-sales-forecasting.git
cd grocery-sales-forecasting


### 2. Virtual Environment
We are using the virtual environments created in class.  
Make sure you activate your course environment before running the project code:


conda activate <your-class-env-name>

### 3. Setup Kaggle API
	1.	Create a Kaggle account if you don’t already have one.
	2.	Go to your Kaggle Account settings and scroll to API.
	3.	Click Create New API Token – this downloads a file called kaggle.json.
	4.	Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\Users\<Windows-User>\.kaggle\ (Windows).
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

### 4. Download Dataset

Once Kaggle API is set up, run:
kaggle datasets download -d littlesaplings/grocery-sales-forecasting-parquet -p data/raw/ --unzip

The raw parquet files will appear in data/raw/.


### Notes
	•	The dataset is not included in the repo because it’s large. Everyone must download it locally with the steps above.
	•	Keep all raw data inside data/raw/ (this folder is git-ignored).
