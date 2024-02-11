from langchain.text_splitter import HTMLHeaderTextSplitter

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text_from_file("/Users/aaliyamanji/anthropic/assessment-tool/output.html")

# Print the splits
for i, split in enumerate(html_header_splits, 1):
    print(f"Split {i}:\n{split}\n{'-'*40}")
