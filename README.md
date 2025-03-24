# Boolean
# Agentic Incident Resolution

## Overview
The **Agentic Incident Resolution** script automates the process of resolving IT incidents using a knowledge base stored in a PDF document. It provides functionalities such as:
- Extracting text from a knowledge base PDF
- Running automated health checks
- Restarting services
- Summarizing root cause analysis (RCA)
- Fetching related incidents

## Prerequisites
Ensure you have the following installed on your system:
- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- Required Python libraries (install using pip):
  ```sh
  pip install PyPDF2
  ```

## Installation
1. Clone or download the script to your local machine.
2. Place your **knowledge base PDF** file in the same directory as the script.

## Usage
### Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script:
   ```sh
   cd path/to/script-directory
   ```
3. Run the script using:
   ```sh
   python agentic_resolution.py
   ```
4. Enter the **path to your knowledge base PDF** when prompted.

### Expected Output
If the script runs successfully, it will:
- Extract text from the PDF
- Perform health checks and restart services
- Provide a summarized RCA report
- Fetch related incidents

Example output:
```
Enter the path to the KB PDF file: sample_kb_document.pdf
Health check passed for app-server: All services running fine.
Service app-service restarted successfully.
Incident INC12345: Potential causes include [list of extracted keywords]. Review system logs and apply recommended fixes.
Related Incident: INC12345-A
Related Incident: INC12345-B
```

## Troubleshooting
### 1. "File not found" Error
**Issue:** The script cannot find the specified PDF file.
**Solution:** Ensure the file path is correct and the PDF exists in the specified location.

### 2. "ModuleNotFoundError: No module named 'PyPDF2'"
**Issue:** The PyPDF2 library is missing.
**Solution:** Install the library using:
```sh
pip install PyPDF2
```

## Logging
The script logs all operations in `agentic_resolution.log`, which can be reviewed for debugging or audit purposes.

## License
This script is open-source and available for modification.

---
For any issues or improvements, feel free to contribute or report a bug!


