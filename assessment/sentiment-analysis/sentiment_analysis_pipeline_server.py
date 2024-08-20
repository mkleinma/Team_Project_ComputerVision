import os
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer


# load model
model_name = "moondream"

# currently best with 0.6 accuracy
model_id = "vikhyatk/moondream2"
revision = "2024-07-23"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
all_responses = []
prompt = """What is the sentiment of the image? 
Please classify the image' sentiment into positive, negative and neutral. 
Only return the sentiment, i.e., do not add any additional information, but only the sentiment.
""" # json mit explanation and confidence hat gar nicht funktioniert



# access all images on server
image_directory = '/home/tp-socialmedia/Dataset_small/' # CHANGE TODO

def process_image(image, filename): 
    image = Image.open(image_path).convert("RGB")
    enc_image = model.encode_image(image)
    moonDreamResult = model.answer_question(enc_image, prompt, tokenizer)
    dict = {
        "image": filename,
        "sentiment": moonDreamResult
    }
    return dict

all_responses = []

for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_directory, filename)
        image = Image.open(image_path).convert("RGB")

    dict = process_image(image, filename)
    all_responses.append(dict)

import pandas as pd
df_temp = pd.DataFrame(all_responses)
df_temp.to_csv(f"SA_results_{model_name}.csv")
