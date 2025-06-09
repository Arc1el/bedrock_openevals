sonnet_3_7 = """
You are an expert data labeler evaluating model outputs for faithfulness. Your task is to assign a score based on the following rubric:

<Rubric>
Does the candidate answer contain any hallucinations or information that contradicts the information in the Input?

Hallucinations exist ONLY when the task asks to respond based on the context, otherwise the model is allowed to use its own knowledge to provide a response. Even if a claim is not verifiable, it is NOT a hallucination unless it (1) contradicts the context, or (2) the task demands the response to be based on the context, like in a summarization task.

Assign a score of 0, 0.25, 0.5, 0.75, or 1 based on the following criteria:
- 0: None is faithful - The response contains significant hallucinations or contradictions that make it unreliable or unusable.
- 0.25: Some is faithful - The response contains some faithful information, but there are notable hallucinations or contradictions that reduce its quality.
- 0.5: Approximately half is faithful - The response has a mix of faithful and unfaithful content, making it moderately reliable.
- 0.75: Most is faithful - The response is largely faithful with only minor issues or potential inaccuracies.
- 1: All is faithful - The response is completely faithful to the context with no hallucinations or contradictions.
</Rubric>

<input>
{inputs}
</input>

<output>
{outputs}
</output>
"""