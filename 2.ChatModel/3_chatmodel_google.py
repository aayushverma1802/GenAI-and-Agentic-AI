from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
val=input("Enter the input:-")
result=model.invoke(val)
print(result.content)
