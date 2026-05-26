from langchain.schema import HumanMessage

def analyze_sentiment(llm, query):

    prompt = f'''
    Detect customer sentiment:
    - Positive
    - Neutral
    - Negative
    - Urgent

    Query:
    {query}
    '''

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
