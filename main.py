from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Destiny(BaseModel):
    city: str = Field("A cidade recomendada para viajar")
    reason: str = Field("A razão para escolher essa cidade")

parser = JsonOutputParser(pydantic_object=Destiny)

prompt_model = PromptTemplate(
    template="Atue como um instrutor de viagens e indique uma cidade para viajar com base no meu interesse {interest}.",
    input_variables=["interest"],
    partial_variables={"output_parser": parser.get_format_instructions()}
)

model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=OPENAI_API_KEY
)

chain = prompt_model | model | JsonOutputParser()

response = chain.invoke({"interest": "praias e vida noturna"})
print(response)