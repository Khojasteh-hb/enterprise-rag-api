# app/cli.py

from dotenv import load_dotenv
load_dotenv()

from app.rag import ask_question


def main():
    print("RAG CLI ready. Type your question (or 'exit' to quit):\n")

    while True:
        question = input(">> ")

        if question.lower() == "exit":
            break

        answer = ask_question(question)
        print("\n", answer, "\n")


if __name__ == "__main__":
    main()
