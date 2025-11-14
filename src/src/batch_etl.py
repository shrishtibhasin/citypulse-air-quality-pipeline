import pandas as pd

df = pd.read_json("data/sample_api_response.json")

df['AQI_Category'] = pd.cut(
    df['value'],
    bins=[0, 50, 100, 150, 200, 300, 500],
    labels=["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous", "Severe"]
)

df.to_csv("clean/air_quality_cleaned.csv", index=False)
print("ETL complete → clean/air_quality_cleaned.csv")
