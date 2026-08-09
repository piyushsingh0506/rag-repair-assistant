import os
import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store
from utils.rag_pipeline import create_qa_chain


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Repair Assistant",
    page_icon="🔧",
    layout="wide"
)


# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.title("🔧 AI Repair Assistant")

    st.write("---")

    menu = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📄 Upload PDF",
            "💬 Ask Question",
            "ℹ️ About"
        ]
    )

    st.write("---")

    st.subheader("⚙️ Features")

    st.write(
        """
        ✅ Repair Manual Analysis

        ✅ AI Based Troubleshooting

        ✅ RAG Question Answering

        ✅ Source Page Detection
        """
    )


    st.write("---")


    st.subheader("🛠 Technology")

    st.info(
        """
        • Streamlit

        • LangChain

        • Gemini AI

        • FAISS Vector DB

        • HuggingFace Embeddings
        """
    )



# ---------------------------------
# Home Page
# ---------------------------------

if menu == "🏠 Home":

    st.title("🔧 AI Repair Assistant")

    st.write(
        """
        Welcome to AI Repair Assistant.

        Upload any repair manual PDF and ask
        technical questions. The AI will search
        the document and provide solutions.
        """
    )


    col1, col2, col3 = st.columns(3)


    with col1:
        st.success("📄 PDF Processing")


    with col2:
        st.success("🧠 AI Understanding")


    with col3:
        st.success("🔍 Smart Search")



# ---------------------------------
# Upload PDF Page
# ---------------------------------

elif menu == "📄 Upload PDF":


    st.title("📄 Upload Repair Manual")


    uploaded_file = st.file_uploader(
        "Choose a PDF File",
        type=["pdf"]
    )


    if uploaded_file is not None:


        # Create uploads folder safely

        upload_folder = "uploads"


        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)



        pdf_path = os.path.join(
            upload_folder,
            uploaded_file.name
        )


        with open(pdf_path,"wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )


        st.success(
            "✅ PDF Uploaded Successfully"
        )


        # Store path

        st.session_state["pdf_path"] = pdf_path



        # Read PDF

        with st.spinner(
            "Reading PDF..."
        ):

            documents = load_pdf(
                pdf_path
            )


        st.success(
            "✅ PDF Read Successfully"
        )



        # Split Documents

        with st.spinner(
            "Splitting Text..."
        ):

            chunks = split_documents(
                documents
            )


        st.success(
            f"✅ {len(chunks)} Chunks Created"
        )



        # Embeddings

        embedding_model = (
            get_embedding_model()
        )



        # Vector Database

        with st.spinner(
            "Creating Vector Database..."
        ):

            vector_db = create_vector_store(
                chunks,
                embedding_model
            )


        st.success(
            "✅ Vector Database Ready"
        )



        # QA Chain

        qa_chain = create_qa_chain(
            vector_db
        )


        st.session_state["qa_chain"] = qa_chain


        st.success(
            "🚀 AI Assistant Ready"
        )



# ---------------------------------
# Ask Question Page
# ---------------------------------

elif menu == "💬 Ask Question":


    st.title(
        "💬 Ask Your Repair Question"
    )


    if "qa_chain" not in st.session_state:


        st.warning(
            "Please upload PDF first"
        )


    else:


        question = st.text_input(
            "Example: Why is my laptop not charging?"
        )



        if st.button(
            "🔍 Get Answer"
        ):


            if question.strip()=="":


                st.warning(
                    "Please enter a question"
                )


            else:


                with st.spinner(
                    "Searching..."
                ):


                    response = (
                        st.session_state["qa_chain"]
                        .invoke(
                            {
                                "query":question
                            }
                        )
                    )


                st.subheader(
                    "🤖 Answer"
                )


                st.write(
                    response["result"]
                )



                # Source Pages

                if "source_documents" in response:


                    pages=set()


                    for doc in response["source_documents"]:


                        page = doc.metadata.get(
                            "page"
                        )


                        if page is not None:

                            pages.add(
                                page+1
                            )


                    if pages:


                        st.info(
                            "📌 Page(s): "
                            +
                            ", ".join(
                                map(
                                    str,
                                    sorted(pages)
                                )
                            )
                        )



# ---------------------------------
# About Page
# ---------------------------------

elif menu == "ℹ️ About":


    st.title(
        "ℹ️ About Project"
    )


    st.write(
        """
        ## AI Repair Assistant

        This application uses RAG
        (Retrieval Augmented Generation)
        to answer repair questions.

        Workflow:

        PDF
        ↓
        Text Extraction
        ↓
        Text Splitting
        ↓
        Embeddings
        ↓
        Vector Database
        ↓
        Gemini AI
        ↓
        Answer


        """
    )