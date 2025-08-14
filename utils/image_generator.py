import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image_from_text(prompt: str, output_path: str = "outputs/generated_image.png") -> str:
    

    system_prompt = (
        "You are an expert that reads the summary from an audio transcript and generate a relevant description to use for image generation."
    )
    user_prompt = f"write a description based on the \n\n{prompt}\n\n to be used for image generation."
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.5,
    )

    description = response.choices[0].message.content.strip()
    
    
    description = "Generate an image based on the following description: " + description
    print(description)
    try:
        response = openai.images.generate(
            prompt=description,
            n=1,
            size="512x512"
        )
        image_url = response.data[0].url

        # Download and save the image
        image_data = requests.get(image_url).content
        print("Image data received, saving to:", output_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(image_data)

        return output_path

    except Exception as e:
        return f"[ERROR] Failed to generate image: {str(e)}"
