from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from app.vectorstore import get_vectorstore
from app.prompts import (
    PORTFOLIO_ASSISTANT_PROMPT,
    CHAT_SUMMARY_PROMPT,
    CONTEXT_MERGE_PROMPT,
)

load_dotenv()

vectorstore = get_vectorstore()

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5},
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

parser = StrOutputParser()

conversation_summary = ""


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_style_context():
    style_docs = vectorstore.similarity_search(
        "presence tone writing style conversational rhythm informal expressive Somay",
        k=5,
    )
    return format_docs(style_docs)


def merge_context(retrieved_context: str, question: str) -> str:
    merge_chain = CONTEXT_MERGE_PROMPT | model | parser

    return merge_chain.invoke({
        "retrieved_context": retrieved_context,
        "conversation_summary": conversation_summary,
        "question": question,
    })


def update_summary(user_message: str, ai_response: str):
    global conversation_summary

    summary_chain = CHAT_SUMMARY_PROMPT | model | parser

    conversation_summary = summary_chain.invoke({
        "existing_summary": conversation_summary,
        "user_message": user_message,
        "ai_response": ai_response,
    })


def ask(question: str) -> str:
    factual_context = format_docs(retriever.invoke(question))
    style_context = get_style_context()

    merged_context = merge_context(factual_context, question)

    answer_chain = PORTFOLIO_ASSISTANT_PROMPT | model | parser

    answer = answer_chain.invoke({
        "factual_context": merged_context,
        "style_context": style_context,
        "question": question,
    })

    update_summary(question, answer)

    return answer


if __name__ == "__main__":
    while True:
        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = ask(question)
        print("\nAI:", answer)