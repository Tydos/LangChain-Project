from typing import Iterator, Dict
import logging 

#stream passages from a given file path
def stream_passages(file_path:str,context_size:int) -> Iterator[Dict[str, str]]:
    logging.info(f"file {file_path} - context - {context_size}")
    with open(file_path, "r", encoding="utf-8") as f:
        buffer = ""
        for line in f:
            buffer += line
            if len(buffer) >= context_size:
                yield {"text": buffer[:context_size].strip()}
                buffer = buffer[context_size:]
        if buffer:
            yield {"text": buffer}