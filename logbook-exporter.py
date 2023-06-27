import pandas as pd
import json

# Read JSON data from file
activity_id = input("ID Aktivitas: ")
with open("km-logbook-{}.json".format(activity_id), 'r') as file:
    json_data = json.load(file)

# Flat the data
flattened_data = []

for item in json_data['data']:
    for report in item['daily_report']:
        flattened_item = {
            'id': item['id'],
            'learned_weekly': item['learned_weekly'],
            'report_date': report['report_date'],
            'report_text': report['report'],
        }
        flattened_data.append(flattened_item)

# Convert JSON to DataFrame
df = pd.json_normalize(flattened_data)

# Export DataFrame to Excel
excel_file = "km-logbook-{}.xlsx".format(activity_id)  # Specify the output Excel file name
df.to_excel(excel_file, index=False)
