import openai

client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key = "sk-or-v1-***")

def get_completion(prompt, model="openai/gpt-3.5-turbo-16k"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo-16k", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message.content

messages =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'},
    {'role':'assistant', 'content':'Why did the tomato turn red? Because it saw the salad dressing!'},
    {'role':'user', 'content':'Not a good one. Some more spicy!'},
]

response = get_completion_from_messages(messages, temperature=1)
print(response)