from langchain_pinecone import PineconeVectorStore
from embedder import chunks, embeddings
from dotenv import load_dotenv
load_dotenv()

vector_store = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name="test"
)


# Connexion à un index Pinecone déjà existant
