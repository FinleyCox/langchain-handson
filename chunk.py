from langchain_text_splitters import RecursiveCharacterTextSplitter

from pathlib import Path


sample_path = Path(__file__).parent / "sample.txt"
text = sample_path.read_text(encoding="utf-8")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "。", "、"],
)

chunks = text_splitter.split_text(text)

for l in chunks:
    print(len(l))
print(chunks[0])
print()
print(chunks[1])
print()
print(chunks[2])

