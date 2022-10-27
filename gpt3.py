import openai
from decouple import config

def gpt3_response(question):
    openai.api_key = config('openai.api_key',default='')
    print(question)
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=question,
    temperature=0.7,
    max_tokens=69,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print(response.choices[0].text)
    return response.choices[0].text