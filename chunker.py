from langchain.text_splitter import HTMLHeaderTextSplitter


def get_list_of_string(doc_list):
    return [doc.page_content for doc in doc_list]


class HTMLHeaderSplitter:
    def __init__(self, headers_to_split_on):

        self.headers_to_split_on = headers_to_split_on
        self.html_splitter = HTMLHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on)

    def split_text_from_file(self, file_path):

        return self.html_splitter.split_text_from_file(file_path)

    def print_splits(self, file_path):

        html_header_splits = self.split_text_from_file(file_path)
        for i, split in enumerate(html_header_splits, 1):
            print(f"Split {i}:\n{split}\n{'-' * 40}")

