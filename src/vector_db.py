import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from src.config import Config

class VectorStoreManager:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model=Config.EMBEDDING_MODEL_NAME)
        self.path = Config.VECTOR_STORE_PATH

    def get_vectorstore(self, chunks=None):
        if os.path.exists(self.path) and os.path.isdir(self.path):
            if os.listdir(self.path):
                print("💾 Carregando banco vetorial existente...")
                return FAISS.load_local(
                    self.path, 
                    self.embeddings, 
                    allow_dangerous_deserialization=True
                )
        
        if not chunks:
            raise ValueError("Banco vetorial não encontrado e nenhum chunk fornecido para criação.")

        print("🆕 Criando novo banco vetorial (Isso pode demorar um pouco)...")
        vector_store = FAISS.from_documents(chunks, self.embeddings)
        vector_store.save_local(self.path)
        print("💾 Banco vetorial salvo localmente.")
        return vector_store