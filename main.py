# Usage
from langchain_community.embeddings import CohereEmbeddings

from chunker import HTMLHeaderSplitter, get_list_of_string
from embeddings import AssessmentEmbeddings

file_path = "/Users/aaliya.manji/personal/assessment-tool/output.html"

headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
]

splitter = HTMLHeaderSplitter(headers_to_split_on=headers_to_split_on)
split_text = splitter.split_text_from_file(file_path)

db = AssessmentEmbeddings.add_to_db(split_text)

query = ("What activity could make a research proposal assessment more "
         "difficult to solve with AI?")
docs = db.similarity_search(query)
for doc in docs:
    print(doc.page_content + "\n --------------------------------- \n")
print(len(docs))
