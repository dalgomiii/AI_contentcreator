from openai import OpenAI

client = OpenAI(api_key='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')


temperatures = [0, 0.5 , 0.8, 1]

def get_completion_from_messages(messages, model = 'gpt-3.5-turbo', temperature = temperatures):
    response = client.chat.completions.create(model = model, messages = messages, temperature = temperature)
    
    return response.choices[0].message.content
messages = [

    {'role':'system', 'content': 'You are an Instagram content creator who likes Mathematics, Physics and Computer Science \ You will generate posts about famous scientists about their lives and work; concepts in this field at a university or post-graduate research level and explain to viewers at the level of a high school student'},

    {'role':'user','content': 'I want to create content and spread knowledge about mathematics, physics and computer science for the general public'}

]


for temperature in temperatures:
    print(temperature)
    content = get_completion_from_messages(messages=messages , temperature=temperatures)
    print(content)