from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
import json
import os



def evaluate(img_path, prompt):
    message = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": f"file://{img_path}",
                },
                {"type": "text", "text": prompt}
            ],
        }
    ]
    # Preparation for inference 
    text = processor.apply_chat_template(
        message, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(message)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to(model.device)

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=2048)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    print(f"(Answer) {output_text[0]}")
    return output_text[0]


def load_data(input_path, output_path):
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            output_data = json.load(f)
    else:
        output_data = []
    with open(input_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)
    return input_data, output_data


def find_last_generate(output_data):
    if not output_data:
        current_index = 0
    else:
        last_item = output_data[-1]
        current_index = last_item["id"] + 1
    return current_index


def compose_prompt(question, option, question_type):
    if question_type == "Yes-or-No" or question_type == "What/How":
        assume_str = "Assume you are an expert in emotional psychology. Analyze the following emotional psychology questions based " \
                     "on the image. The involved emotion categories include anger, disgust, fear, joy, neutral, sadness, and surprise." \
                     "The question is as follows: "
        option_list = [key+":"+option[key] for key in list(option.keys())]
        option_str = ' '.join(option_list)
        tips = " Choose between one of the following options: "
        prompt = assume_str + question + tips + option_str
    elif question_type == "Ranking":
        prompt = "Assume you are an expert in emotional psychology. Based on the given image, carefully identify " \
                 "the three main emotions evoked by the image, ranking them from the strongest to the weakest. " \
                 "The emotions to consider include: anger, disgust, fear, joy, neutral, sadness, and surprise." \
                 "Show the all three main emotions and use comma to separate them in []."
    elif question_type == "Open_ended":
        assume_str_single = "Assume you are an expert in emotional psychology. Based on the given image, analyze the given " \
                            "image and answer the following question or request regarding emotional responses. " \
                            "The emotions to consider include: anger, disgust, fear, joy, neutral, sadness, and surprise. " \
                            "Please provide insightful and structured responses based on your analysis. " \
                            "The question or request is shown in []:"
        prompt = assume_str_single + "[" + question + "]"
    print(f"(Prompt) {prompt}")
    return prompt


# -----------------------main---------------------------
model_name = "Qwen2.5-7b"  # Customized name
model_dir = "path/to/your/model"

# Default: Load the model on the available device(s)
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    model_dir,
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
    device_map="auto",
)

# The default range for the number of visual tokens per image in the model is 4-16384.
# You can set min_pixels and max_pixels according to your needs, such as a token range of 256-1280, to balance performance and cost.
min_pixels = 256*28*28
max_pixels = 1280*28*28
processor = AutoProcessor.from_pretrained(model_dir, min_pixels=min_pixels, max_pixels=max_pixels)

json_file = "path/to/EEmo-Bench(single).json"
output_file = "path/to/EEmo-Bench(single)_response.json"

input_data, output_data = load_data(json_file, output_file)
current_index = find_last_generate(output_data)
image_folder = "path/to/image/directory"

for index in range(current_index, len(input_data)):
    output_item = input_data[index]
    img_name = output_item["image_url"]
    img_path = os.path.join(image_folder, img_name)
    if output_item["question_type"] == "Yes-or-No":
        # Evaluate yes-or-no question
        question = output_item["question"]
        options = eval(output_item["options"])
        prompt = compose_prompt(question, options, "Yes-or-No")
        answer = evaluate(img_path, prompt)
        output_item[model_name] = answer
        # Evaluate ranking task
        prompt = compose_prompt(question, options, "Ranking")
        answer = evaluate(img_path, prompt)
        output_item[model_name + "(ranking)"] = answer
    elif output_item["question_type"] == "What/How":
        # Evaluate what/how question
        question = output_item["question"]
        options = eval(output_item["options"])
        prompt = compose_prompt(question, options, "What/How")
        answer = evaluate(img_path, prompt)
        output_item[model_name] = answer
    elif output_item["question_type"] == "Open_ended":
        # Evaluate description task
        question = output_item["question"]
        options = ""
        prompt = compose_prompt(question, options, "Open_ended")
        answer = evaluate(img_path, prompt)
        output_item[model_name] = answer
    output_data.append(output_item)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)
    print("ID {} completed.".format(output_item["id"]))
print(f"The single-image evaluation of {model_name} has been completed.")

