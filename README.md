# End-to-End ETL Pipelines - Building Network Security system for Phising Data 

An automated **Extract-Transform-Load (ETL) pipeline** designed to preprocess raw network security data, transform it into structured formats, and load it into a secure database for anomaly detection and analytics.  

---

## Project Overview  

This project enables the efficient handling of **large-scale network traffic logs** by automating the ETL process. It prepares clean, structured data for **security analysis, anomaly detection, and intrusion detection systems (IDS)**.  

By implementing this pipeline, security analysts can **reduce manual effort**, ensure **data consistency**, and focus on **advanced analytics for cyber threat detection**.  

---

## Key Features 

- **Automated Data Ingestion**: Supports multiple formats (CSV, JSON, log files)  
- **Data Cleaning & Transformation**: Handles missing values, normalizes IPs, extracts key security features  
- **Database Loading**: Structured data stored in PostgreSQL/MySQL for querying  
- **Scalability**: Designed to process high-volume security logs  
- **Visualization Support**: Generates plots for anomaly trends & traffic insights  
- **CI/CD Enabled**: GitHub Actions with self-hosted runner for automation  

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.9+
- **Data Handling:** Pandas, NumPy
- **Database:** MongoDB Atlas
- **Machine Learning:** Scikit-learn
- **Data Processing & Pipelines:** Custom ETL (Extract, Transform, Load) modules
- **MLOps:** MLflow, DagsHub
- **Cloud Services:** AWS (S3, ECR, EC2)
- **Model Deployment:** Flask / FastAPI (for serving ML models)
- **Version Control:** Git & GitHub
- **Environment Management:** Conda / Virtualenv

---

## System Architecture  

The system follows a 3-stage ETL pipeline:  

1. **Extraction**  
   - Ingests raw log files from CSV/JSON sources  
   - Collects simulated network traffic datasets  

2. **Transformation**  
   - Cleans and normalizes IP addresses, ports, timestamps  
   - Applies feature engineering for anomaly detection  
   - Generates structured tables  

3. **Loading**  
   - Stores processed data into relational databases  
   - Enables queries for threat analysis  

![ETL_pipeline](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/ETL_pipeline.png)

---

## Installation & Setup  

### Prerequisites  
- Python 3.8+  
- PostgreSQL / MySQL  
- Docker (optional)  
- AWS EC2 (if deploying CI/CD)  

### Steps  

1. Clone the repository: 

```bash
git clone https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System.git
cd ETL-Pipelines-Building-Network-Security-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

4. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate
``` 

5. Run ETL pipeline:
```bash
python src/extract.py
python src/transform.py
python src/load.py
```

6. Run the training pipeline:
```bash
python main.py
```

7. Start the flask app for prediction
```bash
python app.py
```

The API/UI will be available at: http://127.0.0.1:5000/


---

## Project strcuture

```bash
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # CI/CD pipeline for deployment
│
├── Network_Data/                   # Raw network dataset (ETL input)
│   ├── train.csv
│   ├── test.csv
│   └── sample.csv
│
├── data_schema/                    # Data validation schemas
│   └── schema.yaml                 # Defines expected data format
│
├── final_model/                     # Trained models stored
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── mlruns/                          # MLflow tracking
│   └── 0/                           # Experiment ID folder
│       └── meta.yaml
│
├── networksecurity/                 # Core project package
│   ├── __init__.py
│   ├── components/                  # ETL + ML pipeline steps
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── config/                      # Project configs
│   │   ├── __init__.py
│   │   └── configuration.py
│   │
│   ├── entity/                      # Input/Output entities
│   │   ├── __init__.py
│   │   └── artifact_entity.py
│   │
│   ├── exception/                   # Custom exception handling
│   │   └── __init__.py
│   │
│   ├── logger/                      # Custom logging
│   │   └── __init__.py
│   │
│   ├── pipeline/                    # End-to-end pipeline orchestrator
│   │   ├── __init__.py
│   │   └── training_pipeline.py
│   │
│   └── utils/                       # Helper functions
│       └── __init__.py
│
├── prediction_output/               # Predictions generated by model
│   └── results.csv
│
├── templates/                       # Flask web app HTML templates
│   └── index.html
│
├── valid_data/                      # Post-validation data
│   ├── valid_train.csv
│   └── valid_test.csv
│
├── .gitignore                       # Ignore unnecessary files
├── Dockerfile                       # Docker image setup
├── README.md                        # Project documentation
├── app.py                           # Flask API for prediction
├── best_model.pkl                   # Saved best performing model
├── main.py                          # Training + MLflow experiment run
├── push_data.py                     # ETL pipeline to push raw data
├── requirements.txt                 # Python dependencies
├── setup.py                         # Package installer
└── test_mongodb.py                  # MongoDB connection & test script
```

---


## 🚀 Usage Workflow

The project follows a complete **ETL + ML pipeline** integrated with CI/CD:

### 1. Data Ingestion
- Raw network traffic datasets are stored in the `Network_Data/` folder.
- `push_data.py` is used to ingest the data into **MongoDB Atlas** for structured storage.
- `test_mongodb.py` ensures connectivity and validates ingestion.
![Data_ingestion](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Data_Ingestion.png)


### 2. Data Validation
- Validation schemas are defined in the `data_schema/` folder.
- Incoming data is validated against the schema to ensure consistency and correctness.
- Cleaned data is stored in the `valid_data/` folder.
![Data_validation](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Data_Validation.png)

### 3. Data Transformation
- Preprocessing and feature engineering steps (e.g., handling nulls, encoding categorical data, normalization).
- Stored under `networksecurity/` components and utilities.
![Data_transformation](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Data_transformation.png)

### 4. Model Training & Experiment Tracking
- `main.py` is used for model training and evaluation.
- Multiple models are tried, and the best one is stored as `best_model.pkl`.
- **MLflow** (stored in `mlruns/`) is used for experiment tracking and versioning.
![Mode_training](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Model_training.png)

### 5. Prediction
- Final predictions are saved in the `prediction_output/` folder.
- The trained model is validated on test datasets.

### 6. Deployment
- `app.py` exposes a **Flask API** for real-time inference.
- Dockerfile is provided to containerize the application.
- CI/CD is configured via **GitHub Actions** to deploy the container to **AWS ECR + EC2**.
![Deployment](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Deployment.png)


---


 **End-to-End Flow:**

![Project_Structure](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/Project_structure.png)
---

## Results & Insights
- Successfully transformed raw logs into structured tables
- Data is ready for anomaly detection models

---

## CI/CD-CD Workflow
GitHub Actions integrated with self-hosted runner (AWS EC2)
Workflow: On push → Run ETL jobs → Store data in DB → Generate reports
![CI_CD-CD](https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System/blob/b38c8682420d89198ece451d56eaa8ad7563d56a/Images/CI_CD-CD.png)

---

##  Contributing
 1. Fork the repo
 2. Create feature branch (git checkout -b feature/new-feature)
 3. Commit changes (git commit -m "Added new feature")
 4. Push (git push origin feature/new-feature)
 5. Open Pull Request

---

## 🎯 Conclusion

This project builds an **end-to-end Network Security System** using ETL pipelines and machine learning.  
The system is capable of:

- Collecting and preprocessing raw network traffic data  
- Transforming and extracting key features for analysis  
- Training ML models to **detect anomalies, cyber-attacks, or suspicious activity**  
- Deploying the trained model for **real-time prediction** and monitoring  

Ultimately, it predicts **whether a given network connection is safe or malicious**, helping in proactive cyber threat detection.
