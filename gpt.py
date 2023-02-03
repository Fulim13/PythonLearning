import openai 

openai.api_key = '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'

prompt = input("Ask GPT")

response = openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=2000)

print(response['choices'][0]['text'])