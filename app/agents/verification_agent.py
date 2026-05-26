from langchain.schema import HumanMessage

def verify_response(llm, response_text):

    prompt = f'''
    Verify this response for:
    - factual accuracy
    - hallucinations
    - professionalism

    Response:
    {response_text}
    '''

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
