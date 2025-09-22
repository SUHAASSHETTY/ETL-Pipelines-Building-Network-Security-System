# End-to-End ETL Pipelines - Building Network Security system for Phising Data 

An automated **Extract-Transform-Load (ETL) pipeline** designed to preprocess raw network security data, transform it into structured formats, and load it into a secure database for anomaly detection and analytics.  

---

## 📌 Project Overview  

This project enables the efficient handling of **large-scale network traffic logs** by automating the ETL process. It prepares clean, structured data for **security analysis, anomaly detection, and intrusion detection systems (IDS)**.  

By implementing this pipeline, security analysts can **reduce manual effort**, ensure **data consistency**, and focus on **advanced analytics for cyber threat detection**.  

Live Demo: *(Optional link if hosted)*  

---

## ✨ Key Features  

- **Automated Data Ingestion**: Supports multiple formats (CSV, JSON, log files)  
- **Data Cleaning & Transformation**: Handles missing values, normalizes IPs, extracts key security features  
- **Database Loading**: Structured data stored in PostgreSQL/MySQL for querying  
- **Scalability**: Designed to process high-volume security logs  
- **Visualization Support**: Generates plots for anomaly trends & traffic insights  
- **CI/CD Enabled**: GitHub Actions with self-hosted runner for automation  

---

## 🛠 Technology Stack  

- **Backend / ETL**: Python, Pandas, NumPy  
- **Database**: PostgreSQL / MySQL  
- **Visualization**: Matplotlib, Seaborn  
- **Orchestration (Optional)**: Airflow / Prefect  
- **CI/CD**: GitHub Actions (Self-hosted runner on AWS EC2)  
- **Infrastructure**: AWS EC2 (Linux), Docker  

---

## 🏗 System Architecture  

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

📸 Add Image Here → `images/architecture.png`  

---

## ⚙️ Installation & Setup  

### Prerequisites  
- Python 3.8+  
- PostgreSQL / MySQL  
- Docker (optional)  
- AWS EC2 (if deploying CI/CD)  

### Steps  

Clone the repository:  
```bash
git clone https://github.com/SUHAASSHETTY/ETL-Pipelines-Building-Network-Security-System.git
cd ETL-Pipelines-Building-Network-Security-System
