from huggingface_hub import InferenceClient  
from dotenv import load_dotenv  

load_dotenv()  

client = InferenceClient("runwayml/stable-diffusion-v1-5")  

image = client.text_to_image(input("Enter prompt: "))  

image.show()
