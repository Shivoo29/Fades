import openai
import requests
from PIL import Image
from io import BytesIO


openai.api_key = 'please put your own OpenAi AIP Key visit:https://openai.com/blog/openai-api'


def get_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()


def generate_image(text):
    response = openai.Image.create(
        prompt=text,
        n=4,
        size="256x256"
    )
    for i, data in enumerate(response['data']):
        image_url = data['url']

        # Download the image
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        image.save(f"generated_image_{i}.png")
        image.show()
    print("Images saved")

# Main chat loop
while True:
    user_input = input("User: ")
    if user_input == 'quit':
        break
    elif user_input.lower().startswith('generate image'):
        
        image_text = user_input.lower().replace('generate image', '').strip()
        generate_image(image_text)
    else:
        response = get_response(user_input)
        print("ChatBot: ", response)
