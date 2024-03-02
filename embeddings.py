from typing import List

from langchain_community.embeddings import CohereEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma


class AssessmentEmbeddings:

    @staticmethod
    def embed_text(text):
        embeddings = CohereEmbeddings()
        return embeddings.embed_documents(text)

    @staticmethod
    def embed_query(text):
        embeddings = CohereEmbeddings()
        query_result = embeddings.embed_query(text)
        return query_result

    @staticmethod
    def add_to_db(document_list: List[Document]):
        return Chroma.from_documents(document_list, CohereEmbeddings())
