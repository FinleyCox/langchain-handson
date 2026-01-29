from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini")

template = ChatPromptTemplate.from_messages([
    ("system", "You are a assistant, answer in japanese" ),
    ("user", "{question}")
])
chain = template | llm
response = chain.invoke({"question": "what is the capital. city of japan?"})

print(response.content)