from transformers import AutoProcessor,AutoModelForCausalLM
from utils import get_dataset
from tqdm import tqdm
from literal import ANSWER,IMG,QUESTION
import pandas as pd

processor = AutoProcessor.from_pretrained("microsoft/git-large-r-coco")
model = AutoModelForCausalLM.from_pretrained("output/checkpoint-5250/")

model.to('cuda')
test_datasets = get_dataset('data/preprocess_test.csv')

labels = []

for i in tqdm(range(len(test_datasets))):
    image = test_datasets[i][IMG]
    question = test_datasets[i][QUESTION].lower()
    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to('cuda')
    input_ids = processor(text=question, return_tensors="pt").input_ids.to('cuda')

    generated_ids = model.generate(pixel_values=pixel_values, input_ids=input_ids, max_length=50,eos_token_id = 102)[0]
    answer = processor.tokenizer.decode(generated_ids,skip_special_tokens=True).replace(question,"").lstrip().rstrip()
    labels.append(answer)

sub = pd.read_csv('data/sample_submission.csv')
sub[ANSWER] = labels

sub.to_csv('0.csv',index=False)