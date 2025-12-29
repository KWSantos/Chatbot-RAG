from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.config import Config

class RAGPipeline:
    def __init__(self, vector_store):
        self.retriever = vector_store.as_retriever(
            search_type="similarity", 
            search_kwargs={"k": Config.RETRIEVER_K}
        )
        self.llm = OllamaLLM(
            model=Config.LLM_MODEL_NAME, 
            temperature=Config.TEMPERATURE
        )

    def _format_docs(self, docs):
        return "\n\n".join([doc.page_content for doc in docs])

    def get_chain(self):
        template = """
        Você é um especialista em política de cartões de crédito. 
        Responda exclusivamente com base nas informações fornecidas nos documentos abaixo.
        Se a informação não estiver no contexto, diga que não sabe.

        Contexto:
        {context}

        Pergunta: {question}
        """
        
        prompt = ChatPromptTemplate.from_template(template)

        rag_chain = (
            {
                "context": self.retriever | self._format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return rag_chain