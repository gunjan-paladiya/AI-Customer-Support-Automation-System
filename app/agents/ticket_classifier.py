from langchain.schema import HumanMessage

def classify_ticket(llm, query):

    prompt = f'''
    Categorize this ticket:
    - Billing
    - Refund
    - Technical Support
    - Subscription
    - Account Access

    Ticket:
    {query}
    '''

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
