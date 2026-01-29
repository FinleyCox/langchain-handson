from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PERSIST_DIR = "./chroma_db"
COLLECTION = "collection_sample"

model = "intfloat/multilingual-e5-small"

embeddings = HuggingFaceEmbeddings(model_name=model)

vectoredb = Chroma(
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION,
    embedding_function=embeddings
)

query="ペットとして人気の動物は？"

retriever = vectoredb.as_retriever(search_kwargs={"k": 2})
docs = retriever.get_relevant_documents(query)

for i, doc in enumerate(docs):
    print(f"結果{i}: {doc.page_content}")