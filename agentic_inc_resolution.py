import PyPDF2
import os
import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("agentic_resolution.log"), logging.StreamHandler()]
    )

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file if it exists."""
    if not os.path.exists(pdf_path):
        logging.error("PDF file not found: %s", pdf_path)
        return "Error: PDF file not found. Please check the file path."
    
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    
    logging.info("Successfully extracted text from %s", pdf_path)
    return text

def run_health_check(server):
    """Simulate a health check command."""
    result = f"Health check passed for {server}: All services running fine."
    logging.info(result)
    return result

def restart_service(service):
    """Simulate a service restart."""
    result = f"Service {service} restarted successfully."
    logging.info(result)
    return result

def summarize_rca(incident_id, knowledge_base_text):
    """Perform simple RCA summarization using keyword extraction."""
    keywords = [word for word in knowledge_base_text.split() if len(word) > 6][:10]  # Extract key terms
    summary = f"Incident {incident_id}: Potential causes include {', '.join(keywords)}. Review system logs and apply recommended fixes."
    logging.info("Generated RCA summary for %s", incident_id)
    return summary

def fetch_related_incidents(incident_id):
    """Simulate fetching related incidents."""
    related = [f"Related Incident: {incident_id}-A", f"Related Incident: {incident_id}-B"]
    logging.info("Fetched related incidents for %s", incident_id)
    return related

def main():
    setup_logging()
    pdf_path = input("Enter the path to the KB PDF file: ").strip()
    kb_text = extract_text_from_pdf(pdf_path)
    
    if "Error:" not in kb_text:
        print(run_health_check("app-server"))
        print(restart_service("app-service"))
        print(summarize_rca("INC12345", kb_text))
        print(fetch_related_incidents("INC12345"))
    else:
        print(kb_text)  # Print the error message if the PDF file is missing

if __name__ == "__main__":
    main()
