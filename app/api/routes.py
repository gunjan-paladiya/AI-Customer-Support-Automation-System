from fastapi import APIRouter
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

from app.database.vector_store import build_vector_store
from app.agents.ticket_classifier import classify_ticket
from app.agents.sentiment_agent import analyze_sentiment
from app.agents.retrieval_agent import retrieve_knowledge
from app.agents.response_agent import generate_response
from app.agents.verification_agent import verify_response

router = APIRouter()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)

vectorstore = build_vector_store()

retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

@router.post("/support")
def customer_support(query: str):

    category = classify_ticket(llm, query)

    sentiment = analyze_sentiment(llm, query)

    knowledge = retrieve_knowledge(query, qa_chain)

    generated_response = generate_response(
        llm,
        query,
        knowledge
    )

    verified_response = verify_response(
        llm,
        generated_response
    )

    return {
        "query": query,
        "ticket_category": category,
        "sentiment": sentiment,
        "knowledge": knowledge,
        "response": verified_response
    }
