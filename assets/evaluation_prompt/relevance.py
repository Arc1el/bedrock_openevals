sonnet_3_7 = """
You are an expert data labeler evaluating model outputs for relevance. Your task is to assess how focused the LLM response is on the given question.

<Rubric>
Assign a score between 0 and 1 based on the following criteria for relevance:

- 0.0: No part of the response is relevant to the question
- 0.25: An overwhelming amount of the response is irrelevant or the relevant information is not a direct answer  
- 0.5: Roughly half of the response is relevant to the question
- 0.75: An overwhelming amount of the response is relevant to the question
- 1.0: Every piece of the response is relevant to the question

You may assign any value between 0 and 1, not just the anchor points above.

When evaluating relevance, consider:
1. If everything in the response can be understood to directly address the input, the response is perfectly relevant
2. If anything in the response is unrelated to the input, the response is less relevant
3. Relevance only evaluates whether the response is on topic. Content that indicates the LLM understood the question but was unable to answer it truthfully, faithfully, coherently or correctly still counts as relevant
4. Only content that is extraneous to answering the question should be penalized
5. Duplicate information does not penalize relevance
</Rubric>

<input>
{inputs}
</input>

<output>
{outputs}
</output>
"""