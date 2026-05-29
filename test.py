from langchain_groq import ChatGroq

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

reply = model.invoke("What do you think about her")
print(reply.content)
