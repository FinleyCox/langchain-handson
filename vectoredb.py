from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PERSIST_DIR = "./chroma_db"
COLLECTION = "collection_sample"

model = "intfloat/multilingual-e5-small"

embeddings = HuggingFaceEmbeddings(model_name=model)

texts = ["犬は可愛い動物です", "猫も可愛いペットです", "車は便意な乗り物です"]

Chroma.from_texts(
    texts=texts,
    embedding=embeddings,
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION,
)
