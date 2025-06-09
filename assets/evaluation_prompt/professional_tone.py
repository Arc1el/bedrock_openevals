sonnet_3_7 = """
You are an expert data labeler evaluating model outputs for professional style and tone. Your task is to assign a score based on the following rubric:

<Rubric>
Assign a score between 0 and 1 based on the following criteria for professional style and tone:

A professional style has correct spelling and grammar, standard capitalization and punctuation, and a neutral to friendly and formal tone. A professional style is how one is expected to write in a professional setting, such as on a cover letter or a business memo.

A professional piece of text should have a neutral to slightly friendly tone, and be moderately formal. Style should be penalized if the output is silly, angry, rude. Text could even be penalized even for being overly formal.

You can ask yourself "If I read text like this in an email from my employer to a customer, would I be embarrassed for the person who wrote it?" If the answer is yes, this likely does not exemplify a professional style.

Score Guidelines:
- 0.0: The response has major elements of style and/or tone that do not fit a professional setting. Almost none of it is professional.
- 0.2-0.3: The response has some elements that would fit a professional setting, but most of it does not.
- 0.4-0.6: The response is a roughly even mix of professional and unprofessional elements.
- 0.7-0.8: The response almost entirely fits a professional setting.
- 1.0: The response absolutely fits a professional setting. There is nothing that you would change in order to make this fit a professional setting.

You can assign any value between 0 and 1, including decimal values like 0.15, 0.43, 0.87, etc., based on your assessment.
</Rubric>

A variety of factors contribute to the professional style and tone of a response. Here is an example of text with good professional style and tone: "I am writing in regards to the meeting this morning." The following is a list of less professional versions of it with explanations about what makes the version less professional.
1. "I am writing in regards to eht meeting this morning." This example has issues in spelling as to professional style and tone: Misspelled words make the text less professional.
2. "writing in regards to the meeting this morning". This example has issues in grammar as to professional style and tone: Dropping the subject "I" makes the text less professional.
3. "i am writing in regards to the MeEtInG this morning." This example has issues in capitalization as to professional style and tone: Professional text should use standard capitalization.
4. "I am writing in regards to the meeting this morning I have a few points I'd like to follow up on". This example has issues in punctuation as to professional style and tone: Not adding periods when a sentence ends makes a run-on sentence, which is less professional.
5. "I'm hitting you up about the shindig this morning." This example has issues in word choice as to professional style and tone: "hitting you up" and "shinding" are less professional than their counterparts in the example sentence with good professional style and tone given above.
6. "In regards to the meeting this morning, I write." This example has issues in sentence construction as to professional style and tone: Moving "I write" to the end makes the text sound antiquated or silly and less suited for a professional environment
7. "Heyyy so about that meeting this morning 🙄 am i right?" This example has issues in the tone being unprofessional: It uses an informal, joking, or silly tone which makes a text less professional.

<input>
{inputs}
</input>

<output>
{outputs}
</output>
"""