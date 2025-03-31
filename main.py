import os
import csv
import datetime

SUB_PAGES_CSV = "notion_data/Work-Logs.csv"
SUB_PAGES_DIR = "notion_data/sub_pages"
WORK_LOG_TEMPLATE = "obsidian/work_log_template.md"
WORK_LOGS_DIR = r"C:\Studies\SportsHunt\obsedian\worship\Work - LOGs"

SUB_PAGES_RECORDS = []
with open(SUB_PAGES_CSV, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    SUB_PAGES_RECORDS = list(reader)

TEMPLATE = ""
with open(WORK_LOG_TEMPLATE, "r", encoding="utf-8") as f:
    TEMPLATE = f.read()

print(os.listdir(SUB_PAGES_DIR))
for page in SUB_PAGES_RECORDS[1:]:
    date = datetime.datetime.strptime(page[0], "%B %d, %Y").strftime("%d-%m-%y")
    work_title = page[1].strip().lower()  # Normalize work title
    hours_worked = page[2]

    # Find the actual file with the work_title 
    matching_file = None
    print(f"Looking for: {work_title}")


    for filename in os.listdir(SUB_PAGES_DIR):
        normalized_filename = filename.lower()
        if work_title[:10] in normalized_filename:
            matching_file = filename
            break

    if matching_file is None:
        print(f"Warning: No matching file found for {work_title}")
        continue

    with open(os.path.join(SUB_PAGES_DIR, matching_file), "r", encoding="utf-8") as f:
        work = f.read()

    current_template = TEMPLATE
    current_template = current_template.replace("{ date:DD-MM-YY }", date)
    current_template = current_template.replace("{{date:DD-MM-YY}}", date)
    current_template = current_template.replace("{ hours_worked }", str(hours_worked))
    current_template = current_template.replace("{ work }", work)

    os.makedirs(WORK_LOGS_DIR, exist_ok=True)

    output_file = os.path.join(WORK_LOGS_DIR, f"{work_title}.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(current_template)

    print(f"Created {output_file}")

print("Migration Done!")
