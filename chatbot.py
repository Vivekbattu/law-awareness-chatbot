import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import GOOGLE_API_KEY, MODEL_NAME

genai.configure(api_key=GOOGLE_API_KEY)

llm = GoogleGenerativeAI(model=MODEL_NAME, google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a law expert. Answer the following legal question: {question}"
)

chain = LLMChain(llm=llm, prompt=prompt)

def get_response(question):
    return chain.run(question)