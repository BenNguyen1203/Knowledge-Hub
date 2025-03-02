import os
import pandas as pd
from datetime import datetime

# Set repository path
repo_path = "./"

# Get the current year
current_year = datetime.now().year

# Dictionary to store counts
md_counts = {}

# Traverse the directory
for year in os.listdir(repo_path):
    year_path = os.path.join(repo_path, year)
    
    if not os.path.isdir(year_path) or not year.startswith("year"):
        continue
    
    year_int = int(year.replace("year", ""))
    
    if year_int == current_year:
        # Count per month for the current year
        for month in os.listdir(year_path):
            month_path = os.path.join(year_path, month)
            
            if not os.path.isdir(month_path) or not month.startswith("month"):
                continue
            
            month_int = int(month.replace("month", ""))
            md_count = sum(1 for f in os.listdir(month_path) if f.endswith(".md"))
            md_counts[f"{year_int}-{month_int:02d}"] = md_count
    else:
        # Count total files for past years
        total_count = sum(len([f for f in os.listdir(os.path.join(year_path, m)) if f.endswith(".md")]) 
                          for m in os.listdir(year_path) if os.path.isdir(os.path.join(year_path, m)))
        md_counts[f"{year_int}"] = total_count

# Convert to DataFrame
df = pd.DataFrame(md_counts.items(), columns=["Time", "Number of Research Papers Read"])

# Update readme.md
readme_path = os.path.join(repo_path, "readme.md")

with open(readme_path, "w") as f:
    f.write("## Research Papers Read Log\n\n")
    f.write(df.to_markdown(index=False))

print("Updated readme.md successfully.")
