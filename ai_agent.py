import openai

def get_ai_input():
    return input("AI Agent: ")

def generate_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    print("AI agent starting...")
    while True:
        ai_input = get_ai_input()
        if ai_input.lower() == "exit":
            break
        response = generate_ai_response(ai_input)
        print("Player: " + response)

if __name__ == "__main__":
    main()
