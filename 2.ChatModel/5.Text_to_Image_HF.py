from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import PIL.Image

# Load API key from .env file
load_dotenv()

client = InferenceClient(model="runwayml/stable-diffusion-v1-5")  # Make sure this is a valid text-to-image model


prompt = "A lion wearing a hat"
image = client.text_to_image(prompt)

# Ensure the returned object is an image
if isinstance(image, PIL.Image.Image):

    image.save("lion_with_hat.png")
    print("Image saved as lion_with_hat.png")
else:
    print("Error: Received unexpected response type:", type(image))
