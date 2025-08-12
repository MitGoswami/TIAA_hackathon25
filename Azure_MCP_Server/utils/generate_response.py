from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

def generate_response(user_query, vectorstore, openai_api_key):
    prompt_template = """
    You are a helpful assistant. Use only the information from the context below to answer the question.

    Context:
    {context}

    Chat History:
    {chat_history}

    User: {question}

    AI:
    """

    gpt_prompt = PromptTemplate(
        input_variables=["context", "chat_history", "question"],
        template=prompt_template
    )

    llm = ChatOpenAI(model="gpt-4",temperature=0, api_key=openai_api_key)

    rag_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 2, "fetch_k": 5}),
        memory=ConversationBufferMemory(memory_key="chat_history", output_key='answer', return_messages=True),
        return_source_documents=True,
        combine_docs_chain_kwargs={'prompt': gpt_prompt}
    )

    result = rag_chain.invoke(user_query)

    return result