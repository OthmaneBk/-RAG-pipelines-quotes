from langchain_pinecone import PineconeVectorStore
from embedder import embeddings
from dotenv import load_dotenv
load_dotenv()

docsearch = PineconeVectorStore.from_existing_index(
    index_name="test",
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})