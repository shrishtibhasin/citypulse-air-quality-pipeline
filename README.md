# CityPulse — Real-Time Air Quality Monitoring Data Pipeline 🌍

CityPulse is an end-to-end **real-time data engineering project** designed to collect, process, transform, and analyze air quality and weather data using:

**Python · Kafka · Spark Streaming · ETL · PostgreSQL · AWS S3 (optional)**

This project demonstrates real-world Data Engineering skills:
- Real-time ingestion (API → Kafka)
- Streaming ETL (Spark Structured Streaming)
- Batch ETL
- Data modeling
- Data quality checks
- Analytics & dashboard-ready data

---

## 🚀 Tech Stack
- **Languages:** Python, SQL  
- **Data Processing:** Apache Kafka, Apache Spark (Structured Streaming)  
- **Storage:** PostgreSQL / AWS S3  
- **Tools:** Pandas, Docker, Airflow (optional)  
- **Other:** JSON APIs, Data Quality Validation  

---

## 🏗️ Architecture

![CityPulse Architecture](architecture/citypulse_architecture.png)

### **Pipeline Stages**
1. **API Ingestion**  
   - Fetches air quality & weather data every 5 minutes  
   - Publishes to Kafka topic `air-quality-stream`

2. **Stream Processing (Spark)**  
   - Spark Structured Streaming consumes from Kafka  
   - Data validation & cleaning  
   - Enriches with AQI classifications  
   - Stores processed data in PostgreSQL or CSV

3. **Batch ETL (Optional)**  
   - Additional transformations  
   - Aggregations (city-wise AQI, pollutant levels, etc.)

4. **Analytics Layer**  
   - Notebooks for data exploration  
   - Future BI dashboards (Power BI / Looker / Tableau)

---

## 🔧 Setup Instructions

### 1. Install dependencies
