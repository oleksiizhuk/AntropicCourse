from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-sonnet-4-5-20250929"


def add_user_message(messages: list, text: str) -> None:
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages: list, text: str) -> None:
    messages.append({"role": "assistant", "content": text})


def chat(messages: list) -> str:
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


def main() -> None:
    messages: list = []

    print("Start \n")

    while True:

        user_input = input("> ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("BB!")
            break

        add_user_message(messages, user_input)

        answer = chat(messages)

        add_assistant_message(messages, answer)

        print("---")
        print(answer)
        print("---")


if __name__ == "__main__":
    main()
