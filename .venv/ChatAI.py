import openai

openai.api_key = "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"

models = openai.Model.list()
print(models)

def handle_input(user_input):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return copletion