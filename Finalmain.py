from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from response_from_docsearch import retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_huggingface import HuggingFaceEndpoint
from transformers import pipeline
load_dotenv()

model = pipeline(
    "text-generation",
    model='mistralai/Mistral-7B-Instruct-v0.1',
    device=0,
    max_length=256,
    truncation=True
)

llm=HuggingFacePipeline(pipeline=model)

system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentence maximum and keep the answer concise. "
    "Context: {context}"
)


# Créer la chaîne de combinaison des docume
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

#passer les documents extraits au llm pour le contextualiser 
question_answer_chain = create_stuff_documents_chain(llm, prompt)
chain = create_retrieval_chain(retriever, question_answer_chain)



def ask_question(query):
    try:
        return chain.invoke({"input": query})

    except Exception as e:
        return f"Erreur: {e}"

if __name__=='__main__':
    question = "give a quote that the author is Albert Einstein"
    response = ask_question(question)

    print(response)