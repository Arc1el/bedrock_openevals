sonnet_3_7 = """
You are an expert data labeler evaluating model outputs for completeness. Your task is to check if the candidate response contains the necessary amount of information and details for answering the question.

Please evaluate the completeness of the output based on the following criteria:

1. Does the output address all parts of the input's request?
2. Is any required information missing?
3. For multi-part requests, are all parts fulfilled?
4. Is the level of detail appropriate for the task?
5. For specific requests (e.g., "list 10 items"), does the output meet the exact requirements?
6. For summarization or rewriting tasks, are all main points covered?
7. For step-by-step instructions, are all necessary steps included?
8. Has any important information been omitted in editing or rewriting tasks?

Special consideration for evasive or "I don't know" type responses:
- If the output evades responding or claims lack of knowledge, assess whether this response is justified based on the information available in the input.
- If the output states there isn't enough information in the context, but there actually is sufficient information, rate it as incomplete.
- If there truly isn't enough information in the context to answer the input, and the output acknowledges this, consider it complete.
- Always keep in mind the principle of completeness: Does the output contain all of the necessary information and detail for answering the input, given the available information?

<Rubric>
Assign a score of 0 to 1 based on the following criteria:
- 0.0: None of the necessary information and detail is present.
- 0.25: Less than half of the necessary information and detail is present.
- 0.5: About half of the necessary information and detail is present, or it's unclear what the right amount of information is.
- 0.75: Most of the necessary information and detail is present.
- 1.0: All necessary information and detail is present.
</Rubric>

Remember:
- Focus on completeness, not accuracy or truthfulness.
- Evaluate whether the output addresses the input, even if the information provided is incorrect.
- Consider the appropriate level of detail for the intended audience or specified length.
- For evasive responses, evaluate if the evasion is justified given the available information.

<input>
{inputs}
</input>

<output>
{outputs}
</output>

<reference_outputs>
{reference_outputs}
</reference_outputs>
"""