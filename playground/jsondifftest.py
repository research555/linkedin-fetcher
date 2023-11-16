import json
import pandas as pd
from datetime import datetime

json_file_path = r"C:\Users\immi\PyCharmProjects\Startups\kale-linkedin-api\playground\files\individuals\try1\temp_proxy.json"

# List to store keys from all profiles
all_keys = []

with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    profiles = data.get('profiles', [])

    # Recursive function to fetch keys from nested JSON structure and convert DateItem to datetime
    def extract_and_convert(d, parent_key=''):
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k

            if isinstance(v, list):
                for idx, item in enumerate(v):
                    indexed_key = f"{new_key}_{idx + 1}"
                    if isinstance(item, dict):
                        extract_and_convert(item, indexed_key)
                    else:
                        all_keys.append(indexed_key)

            elif isinstance(v, dict):
                # Check if the dictionary has day, month, and year keys, indicating it's a DateItem
                if {'day', 'month', 'year'}.issubset(v.keys()):
                    day = v.get('day', 1)  # Default to first day if day is None
                    month = v.get('month', 1)  # Default to January if month is None
                    year = v.get('year', 2000)  # Default to year 2000 if year is None
                    d[k] = datetime(year, month, day).date()
                else:
                    extract_and_convert(v, new_key)
            else:
                all_keys.append(new_key)

    # Iterate over each profile and extract keys
    for profile in profiles:
        extract_and_convert(profile)

        # Optionally, convert DateItem in each profile to datetime strings
        for profile in profiles:
            profile = json.loads(json.dumps(profile, default=str))

# Convert the list of keys into a DataFrame
df = pd.DataFrame(all_keys, columns=["Keys"])

# If you want to remove duplicate keys
df = df.drop_duplicates().reset_index(drop=True)

print(df)
