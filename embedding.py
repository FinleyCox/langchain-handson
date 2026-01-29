from langchain_huggingface import HuggingFaceEmbeddings

model = "intfloat/multilingual-e5-small"

embeddings = HuggingFaceEmbeddings(model_name=model)
texts = ['犬は可愛い動物です', '猫は可愛い動物です', '車は便利なな乗り物です']
vectors = embeddings.embed_documents(texts)

print(f"ベクトルの長さ: {len(vectors[0])}")
print(f"1つ目のベクトルの最初の5要素: {vectors[0][:2]}")
