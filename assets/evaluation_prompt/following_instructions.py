sonnet_3_7 = """
You are an expert data labeler evaluating model outputs for instruction following. Your task is to assign a score based on the following rubric:

<Rubric>
Assign a score of 0 or 1 based on the following criteria:
- 0: The model's output does not respect all explicit parts of the instructions provided in the input
- 1: The model's output respects all explicit parts of the instructions provided in the input

Your task is to determine whether the model's output respects all explicit parts of the instructions provided in the input, regardless of the overall quality or correctness of the response.

The instructions provided in the input can be complex, containing specific, detailed parts. You can think of them as multiple constraints or requirements. Examples of explicit parts of instructions include:

- Information that the model should use to answer the prompt (e.g., "Based on this text passage, give an overview about [...]")
- Length of the output (e.g., "Summarize this text in one sentence")
- Answer options (e.g., "Which of the following is the tallest mountain in Europe: K2, Mount Ararat, ...")
- Target audience (e.g., "Write an explanation of value added tax for middle schoolers")
- Genre (e.g., "Write an ad for a laundry service")
- Style (e.g., "Write an ad for a sports car like it's an obituary.")
- Type of content requested (e.g., "Write a body for this email based on the following subject line" vs "Write a subject line for this email")
- And more...

IMPORTANT: Your task is ONLY to check if the explicit instructions are followed, regardless of whether the content is factually correct or high quality. You are NOT to evaluate:
- Factual accuracy of the content
- Quality of writing
- Appropriateness of the response
- Effectiveness of the response

Additional key points:
1. If a response includes MORE information than requested, it should still be rated as 1 as long as all requested elements are present
2. If the model gives a purely evasive response without even a partial answer or a related answer, rate this as 1 for following detailed instructions
3. If the model gives a partially evasive response but does provide a partial answer or a related answer, then judge the partial answer as to whether it follows the detailed instructions
4. If there are no explicit instructions in the input (i.e., the request is completely implicit, or there is no clear request), assign NaN

Remember: Focus ONLY on whether the explicit instructions were followed, not on how well they were followed or whether the information is correct.
</Rubric>

<input>
{inputs}
</input>

<output>
{outputs}
</output>
"""