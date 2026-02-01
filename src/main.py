from src.config_loader import load_config
from src.data_loader import stream_passages
from src.LLaMa import askLLaMa

import logging
logging.basicConfig(level=logging.INFO)

config = load_config()

files= config.file_list

data_iterator = stream_passages(file_path=f"data/{files[0]}",context_size=config.context_size)

for chunk in data_iterator:
    text = chunk["text"]
    query = f"Write a 4-line poem based on: \n{text}"
    answer = askLLaMa(model_id=config.model_id,
                    task=config.task_id,
                    query=query)

    print("text: ",text)
    print("\n")
    print("summary: ",answer)
    break