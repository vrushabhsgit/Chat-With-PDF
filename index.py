
---

# index.py

```python
def load_pdf(file_path):
    """
    Load and process the PDF file.
    """
    print(f"Loading PDF: {file_path}")


def ask_question(question):
    """
    Process user question and return an answer.
    """
    return f"You asked: {question}"


def main():
    print("📄 Chat With PDF")
    print("Type 'exit' to quit.\n")

    pdf_path = input("Enter PDF path: ")
    load_pdf(pdf_path)

    while True:
        question = input("\nAsk a question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_question(question)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()