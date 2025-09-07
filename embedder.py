import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings


# Ignorer les avertissements de TensorFlow
#warnings.filterwarnings("ignore", category=DeprecationWarning)

#embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Charger tes citations
with open("quotes_data.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)




# Étape 1 : convertir les données en documents texte
documents = []
for item in data:
    for corpus in data[item]:
        full_text = f"quote: {corpus['quote']} — autor: {corpus['author']} - tags: {corpus['tags']}"
        documents.append(Document(page_content=full_text, metadata={"url": item}))

# Étape 2 : Définir la fonction chunk_text()
def chunk_text():
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

# Exécution
chunks = chunk_text()



def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )
    return embeddings

# charger le modele 
embeddings=download_hugging_face_embeddings()
