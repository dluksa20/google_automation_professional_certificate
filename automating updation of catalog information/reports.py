#!/usr/bin/env python3

import reportlab
import glob
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from report_email import generate as email_generate
from report_email import send as email_send

descriptionsPath = 'supplier-data/descriptions/*.txt'
descriptionsList = glob.glob(descriptionsPath)


# Create a PDF file
def process_descriptions(desc):
    data = []
    for description in desc:
        product_dict = {} 
        with open(description) as d:
            lines = d.readlines()
            product_dict['name'] = lines[0].strip()
            product_dict['weight'] = int(lines[1].split()[0]) 
            data.append(product_dict)
    return data


def generate_report(data, filename="processed.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Set the title with the current date
    c.setFont("Helvetica-Bold", 16)
    title = f"Processed Update on {datetime.now().strftime('%B %d, %Y')}"
    c.drawString(100, height - 40, title)

    c.setFont("Helvetica", 12)
    y = height - 80  # Start from below the title

    for item in data:
        # Write the name and weight to the PDF
        c.drawString(100, y, f"name: {item['name']}")
        y -= 20
        c.drawString(100, y, f"weight: {item['weight']} lbs")
        y -= 40  # Add a blank line

    c.save()

def main():
    sample_data = process_descriptions(descriptionsList)
    generate_report(sample_data)

if __name__ == "__main__":

    # Prepare email content
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    # Prepare the email message with attachment
    msg = email_generate("automation@example.com", "student@example.com", 
                         email_subject, email_body, 'processed.pdf')
    email_send(msg)