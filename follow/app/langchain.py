from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.3)

prompt = PromptTemplate(
 input_variables=["assignment"],
 template="""
 Evaluate the following assignment and provide scores
 based on criteria.

 Assignment:
 {assignment}
 """
)
def build_prompt(assignment_text, criteria):

    rubric_text = ""

    for c in criteria:
        rubric_text += f"{c['id']}. {c['criterion']} - {c['description']}\n"

    prompt = f"""
    Evaluate the following student assignment.

    Assignment:
    {assignment_text}

    Score the assignment based on these criteria.

    {rubric_text}

    Return a JSON score between 0 and 10 for each criterion.
    """

    return prompt

chain = LLMChain(llm=llm, prompt=prompt)

def evaluate_assignment(text):

    result = chain.run(text)
    return result
def calculate_final_score(scores):

    total = 0
    count = len(scores)

    for value in scores.values():
        total += value

    final_score = (total / (count * 10)) * 100

    return final_score