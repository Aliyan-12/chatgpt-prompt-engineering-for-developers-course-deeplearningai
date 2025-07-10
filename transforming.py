import openai
from redlines import Redlines
from IPython.display import display, HTML

client = openai.OpenAI(base_url="https://openrouter.ai/api/v1", api_key = "sk-or-v1-***")

def get_completion(prompt, model="openai/gpt-3.5-turbo-16k"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

# prompt = f"""
# Translate the following English text to Spanish:  
# ```Hi, I would like to order a blender```
# """

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
]

for issue in user_messages:
    prompt = f"""
    Translate the following text to English
    ```{issue}```
    """

# prompt = f"""
# Translate the following from slang to a business letter: 
# 'Dude, This is Joe, check out this spec on this standing lamp.'
# """

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"

response = get_completion(prompt)
diff = Redlines(text,response)
display(HTML(diff.output_markdown))
print(response)