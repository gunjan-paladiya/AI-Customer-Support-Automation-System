from langchain.schema import HumanMessage


def generate_response(llm, query, knowledge):

    prompt = f'''
    You are a professional AI customer support assistant.

    Customer Query:
    {query}

    Knowledge Base:
    {knowledge}

    Generate a concise professional response.
    '''

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
