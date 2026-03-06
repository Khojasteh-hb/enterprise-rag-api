import requests
import time

API_URL = "http://localhost:8000/ask"

test_questions = [
    "What is preventive maintenance?",
    "Why do pumps fail?",
    "How often should industrial equipment be inspected?"
]


def evaluate():

    print("\nRunning RAG evaluation...\n")

    for question in test_questions:

        start = time.time()

        response = requests.post(
            API_URL,
            json={"question": question}
        )

        end = time.time()

        result = response.json()

        print("Question:")
        print(question)

        print("\nAnswer:")
        print(result["answer"])

        print(f"\nResponse time: {round(end-start,2)} seconds")

        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    evaluate()
