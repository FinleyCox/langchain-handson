from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import dotenv
dotenv.load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini")

message = HumanMessage(content="hiya")

response = llm.invoke([message])
print(response.content)