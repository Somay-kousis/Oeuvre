from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.vectorstore import get_vectorstore
from app.prompts import PORTFOLIO_ASSISTANT_PROMPT


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_chat_chain():
    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.4,
    )

    chain = (
        {
            "factual_context": retriever | format_docs,
            "style_context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | PORTFOLIO_ASSISTANT_PROMPT
        | model
        | StrOutputParser()
    )

    return chain


def ask(question: str):
    chain = get_chat_chain()
    return chain.invoke(question)