import os
import calendar

# Define the path where monthly folders are stored
repo_path = os.getcwd()

# Create a list of all months
months = [f"{calendar.month_name[i]}_{2025}" for i in range(1, 13)]

# Count research papers per month
paper_count = {}
for month in months:
    folder_path = os.path.join(repo_path, month)
    if os.path.isdir(folder_path):
        md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
        paper_count[month] = len(md_files)

# Create markdown table dynamically
table_rows = "\n".join([f"| {month.capitalize()} | **{count}** |" for month, count in sorted(paper_count.items())])

# Read README.md and update the PAPER_COUNT section
readme_path = os.path.join(repo_path, "README.md")
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

# Replace placeholder with generated table
updated_readme = readme_content.replace("{{ PAPER_COUNT }}", table_rows)

# Write back to README.md
with open(readme_path, "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("✅ README.md updated with the latest research paper counts!")

