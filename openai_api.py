import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from io import BytesIO
from PIL import Image

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

## Example from OpenAI API docs to generate text
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

def generate_image(img_prompt, model_type="dall-e-3"):
  print("generating image: ", img_prompt)
  
  # Call API to generate an image from the prompt      
  response = client.images.generate(
    model = model_type,
    prompt = img_prompt,
    size = "1024x1024",
    quality = "standard",
    n = 1,
  )

  image_url = response.data[0].url
  save_path = os.path.join("images", img_prompt.replace(" ", "_").lower())
  print(image_url)
  
  # Fetch the image content from the URL
  response = requests.get(image_url)
  image_content = BytesIO(response.content)

  # Open the image using PIL
  image = Image.open(image_content)

  # Save the image to the specified path
  image.save(f"{save_path}.png")  # You can change the file format if needed

   
# return image_url

# response = client.images.generate(
#   model="dall-e-3",
#   prompt="A painting of a glass bowl with a flower on it.",
#   size="1024x1024",
#   quality="standard",
#   n=1,
# )

# image_url = response.data[0].url
# print(image_url)


# client.images.download(image_url, path="image.png")