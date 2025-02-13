from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=300)
documents=[
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of the France"
]
query="tell me about the Delhi"
doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)
print(cosine_similarity([query_embedding],doc_embeddings))
score=cosine_similarity([query_embedding],doc_embeddings)[0]
print(sorted(list(enumerate(score)),key=lambda x:x[1])[-1])
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("Similarity score is:",score)



