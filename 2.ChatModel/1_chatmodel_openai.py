from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4")
result=model.invoke("Write a 5 line poem on gym",temperature=0)
print(result.content)

# temperature
# temperature is a parameter that controls the randomness of a language model's output. It affects
# how creative and deterministic the response are.
# ~Lower values(0.0 - 0.3)->more deterministic and predictable
# ~Higher values(0.7 - 1.5)->more random ,creative and diverse



# Lets simplyfy with the use case example
# Factual answers (math,code,facts) -> 0.0 - 0.3
# Balanced response  (general,QA,explanation) -> 0.5 - 0.7
# Creative writing,storytelling,jokes -> 0.9 - 1.2
# Maximum randomness (wild ideas, brainstorming) ->1.5+

# max_completion_tokens
# Limit the token to that limit


