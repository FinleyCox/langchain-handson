from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template(
    "tell me top three popular cusines of {country}"
)
chain = prompt | llm | StrOutputParser()
output = chain.invoke({"country": "Italy"})
print(output)