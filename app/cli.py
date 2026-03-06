from app.ask import query_index


def run_cli():
    print("RAG CLI ready. Type your question (or 'exit' to quit):\n")

    while True:
        question = input(">> ")

        if question.lower() == "exit":
            break

        results = query_index(question)

        print("\nTop relevant chunks:\n")

        for i, doc in enumerate(results, 1):
            print(f"Result {i}:")
            print(doc)
            print("-" * 50)


if __name__ == "__main__":
    run_cli()
