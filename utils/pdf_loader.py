from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    """
    Load the PDF and return its pages.
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents