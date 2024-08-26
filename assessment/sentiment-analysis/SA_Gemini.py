
import asyncio
import os
from PIL import Image
import json
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import pathlib
import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

month = "01_January"
GOOGLE_API_KEY="AIzaSyBYG3RuSaxKE3nHgokSsnK62jDTWFkzIw4" # TODO replace with your API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')  # gemini-pro-vision
folder_path = f"/Users/I539205/Library/CloudStorage/OneDrive-SAPSE/Uni Master/Team Project/{month}/"
prompt = """What is the sentiment of the image? 
Please classify the image' sentiment into positive, negative and neutral and provide 
a confidence score in [0,1] as well as a short explanation. 
Structure your answer in the same json format as this example and do not add any additional information: 
{"sentiment": "XX", "confidence": XX, "explanation": "XX"},
"""

all_responses = {}

async def process_image(file: str, count) -> str:
    print(count)
    img = Image.open(os.path.join(folder_path, file))
    response = await model.generate_content_async([prompt,img])
    # TODO: error handling
    response.resolve()
    to_markdown(response.text)
    text = response.text
    # replace any " with ' to make it valid json only for text inside "explanation" value
    start_index = text.find('"explanation": "') + len('"explanation": "')
    end_index = text.find('"}', start_index)
    explanation = text[start_index:end_index].replace('"', "'")
    output_string = text[:start_index] + explanation + text[end_index:]

    print(output_string)
    r_dict = json.loads(output_string)
    all_responses[file] = r_dict

    return response.text

jobs = asyncio.gather(*[process_image(file, i) for i, file in enumerate(os.listdir(folder_path))])
#results = await jobs  # or run_until_complete(jobs)

with open(f'results/responses_{month}.json', 'w') as f:
    json.dump(all_responses, f)

# convert all_responses to csv
import csv
with open(f'results/responses_{month}.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['image', 'sentiment', 'confidence', 'explanation'])
    for image, dict in all_responses.items():
        writer.writerow([image, dict['sentiment'], dict['confidence'], dict['explanation']])

