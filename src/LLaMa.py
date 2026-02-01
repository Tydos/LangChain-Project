from langchain_huggingface import HuggingFacePipeline
from dotenv import load_dotenv
import os
import logging

def askLLaMa(model_id:str,
               task:str,
               query:str,
               temperature:float = 0.7,
               max_new_tokens:int = 100,
               top_k:int = 50,
               top_p:float = 0.95,
               repetition_penalty:float = 1.2) -> str:
    
    load_dotenv()
    llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task=task,
    pipeline_kwargs={
        "temperature":temperature,
        "max_new_tokens":max_new_tokens,
        "top_k": top_k,
        "top_p": top_p,
        "repetition_penalty": repetition_penalty
    }
    )
    result = llm.invoke(query)
    return result