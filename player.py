import openai

def get_player_input():
    return input("Player: ")

def generate_player_response(prompt):
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
    print("Player agent starting...")
    while True:
        player_input = get_player_input()
        if player_input.lower() == "exit":
            break
        response = generate_player_response(player_input)
        print("AI Agent: " + response)

if __name__ == "__main__":
    main()
