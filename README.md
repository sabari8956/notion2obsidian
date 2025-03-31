# Notion Work Logs to Obsidian Converter

A Python tool that converts Notion work log exports to Obsidian-compatible markdown files. This tool is specifically designed to process daily work logs from Notion and format them according to a predefined Obsidian template.

## Features

- Converts Notion work log entries to Obsidian markdown format
- Maintains work log metadata (date, hours worked)
- Automatically processes all entries from a CSV export
- Creates properly formatted markdown files for Obsidian
- Preserves the original work log content
- Handles date formatting conversion

## Project Structure

```
notion2obsidian/
├── notion_data/
│   ├── Work-Logs.csv        # Exported CSV from Notion
│   └── sub_pages/           # Exported markdown files from Notion
├── obsidian/
│   ├── work_log_template.md # Template for Obsidian format
│   └── work_logs/           # Output directory for converted files
├── main.py                  # Main conversion script
└── README.md               
```

## Prerequisites

- Python 3.6 or higher
- Notion workspace with work logs
- Obsidian vault (for viewing converted files)

## Setup

1. Export your Notion work logs:
   - Export your work log database as CSV to `notion_data/Work-Logs.csv`
   - Export the individual work log pages as Markdown & CSV
   - Place the exported markdown files in `notion_data/sub_pages/`

2. Configure the template:
   - Review and modify `obsidian/work_log_template.md` if needed
   - The template supports the following variables:
     - `{ date:DD-MM-YY }` - Work log date
     - `{ hours_worked }` - Hours spent on the task
     - `{ work }` - Main content of the work log

## Usage

1. Ensure all exported files are in their correct locations
2. Run the conversion script:
   ```bash
   python main.py
   ```
3. Check the converted files in `obsidian/work_logs/`

## Template Format

The default template creates files with this structure:
```markdown
---
type: daily-work-log
date: "DD-MM-YY" 
hours_worked: X
tags:
  - work-log
---

# Daily Work Log - DD-MM-YY

[Work log content]
```

## Known Limitations

- Requires specific Notion export format
- File names must match between CSV and markdown files
- Template structure is fixed (modify code to change)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
