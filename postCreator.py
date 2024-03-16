def get_completion_from_messages(client,input_message, temperature, model = 'gpt-3.5-turbo'):
    response = client.chat.completions.create(model = model, messages = input_message, temperature = temperature ,top_p=0.9)
    
    return response.choices[0].message.content


def get_image_url(client,prompt:'str',model="dall-e-3",size="1024x1024",quality="standard",n=1):
    response=client.images.generate(model = model, prompt=prompt, size = size, quality = quality, n=n)

    return response.data[0].url

