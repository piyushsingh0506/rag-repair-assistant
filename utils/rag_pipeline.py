from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()


def create_qa_chain(vector_store):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    return qa_chain