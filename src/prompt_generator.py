from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input = ["topic"],
    template=(
        "Summarise this {topic} in a clear and concise way"
    )
)