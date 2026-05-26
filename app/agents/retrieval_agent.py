from langchain.chains import RetrievalQA

def retrieve_knowledge(query, qa_chain: RetrievalQA):

    result = qa_chain.run(query)

    return result
