import openai

# Create a client with your API key
client = openai.OpenAI(api_key="")  # Replace with your actual API key

def ask_openai(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-3.5-turbo" if you don’t have GPT-4 access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Welcome to your OpenAI chatbot!")
    while True:
        user_input = input("you: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        print("Bot:", ask_openai(user_input))
