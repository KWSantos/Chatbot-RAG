import os

class Config:
    # Caminhos
    DOCUMENTS_DIR = "documents"
    VECTOR_STORE_PATH = "faiss_index"
    
    # Modelos
    EMBEDDING_MODEL_NAME = "bge-m3"
    LLM_MODEL_NAME = "gemma3:4b"
    TOKENIZER_NAME = "BAAI/bge-m3"
    
    # Parâmetros
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 100
    RETRIEVER_K = 3 
    TEMPERATURE = 0.2

    @staticmethod
    def ensure_directories():
        """Garante que o diretório de documentos exista."""
        if not os.path.exists(Config.DOCUMENTS_DIR):
            os.makedirs(Config.DOCUMENTS_DIR)
            print(f"Diretório '{Config.DOCUMENTS_DIR}' criado. Coloque seus PDFs lá.")