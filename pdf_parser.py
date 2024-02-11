import fitz  # PyMuPDF

def extract_stars(text):
    # Assuming stars are represented by the character '★'
    stars = text.count('★')
    return f'<div class="stars">{stars}</div>' if stars else ''

def pdf_to_html(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    font_sizes = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    font_sizes.extend([span["size"] for span in line["spans"]])
    font_sizes = sorted(set(font_sizes), reverse=True)

    html_content = '<!DOCTYPE html>\n<html>\n<body>'

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        html_content += '\n<div>'  # Start of slide div

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    max_font_size = max([span["size"] for span in line["spans"]])
                    text = " ".join([span["text"] for span in line["spans"]])

                    if '★' in text:
                        # Handle star ratings
                        html_content += extract_stars(text)
                    elif max_font_size == font_sizes[0]:
                        # Main heading
                        html_content += f'<h1>{text}</h1>'
                    elif max_font_size == font_sizes[1]:
                        # Section heading
                        html_content += f'<h2>{text}</h2>'
                    else:
                        # Paragraph text
                        html_content += f'<p>{text}</p>'

        html_content += '</div>\n'  # End of slide div

    html_content += '</body>\n</html>'
    doc.close()
    return html_content

def save_html(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Usage
pdf_path = 'assessment_ideas.pdf'
html_content = pdf_to_html(pdf_path)
output_path = 'output.html'
save_html(html_content, output_path)
