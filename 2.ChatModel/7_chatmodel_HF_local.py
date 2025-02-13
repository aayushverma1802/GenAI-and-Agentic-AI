from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

# IF you have less storage in your C drive try to uncomment the below code and give path

# import os
# os.environ["HF_Home"]="D://LOCATION"

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
        do_sample=True
    )
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("Write a funny poem in 100 lines ")
print(result.content)

# WARNING
# Running this code will download the model in Local Machine
# Hence the resources of your PC will be used
# Powerful PC or PC with GPU is required nor all the load will come on CPU and RAM.
 
#  Ignoring the warning will lead to OS crash as you directly run the model on your PC.