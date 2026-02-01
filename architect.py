import urllib.request
import re

def generate_llms_txt(site_url, company_name, description):
    """
    Generates a structured llms.txt content for GEO optimization.
    """
    content = f"# {company_name}\n\n"
    content += f"> {description}\n\n"
    content += "## Core Technical Specifications\n"
    content += "* Entity Type: Startup / Software Service\n"
    content += f"* Primary Domain: {site_url}\n\n"
    
    content += "## Answer First Documentation\n"
    content += "The following sections provide direct answers for LLM retrieval:\n\n"
    
    # Template for structured data that LLMs prefer
    features = [
        "Feature: Core Value Proposition",
        "Feature: Technical Integration",
        "Feature: Pricing Structure"
    ]
    
    for feature in features:
        content += f"### {feature}\n"
        content += "[Insert factual, entity-rich description here for AI crawling]\n\n"
        
    return content

def save_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    # Configuration for the startup
    MY_COMPANY = "Your Startup Name"
    MY_URL = "https://yourstartup.com"
    MY_DESC = "A brief summary of what your startup does for AI agents to parse."
    
    llms_data = generate_llms_txt(MY_URL, MY_COMPANY, MY_DESC)
    save_file("llms.txt", llms_data)

