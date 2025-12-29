from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from transformers import AutoTokenizer
from src.config import Config

class DataIngestor:
    def __init__(self):
        self.directory = Config.DOCUMENTS_DIR
    
    def load_and_split(self):
        print(f"🔄 Carregando documentos de {self.directory}...")
        loader = DirectoryLoader(self.directory, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        
        if not documents:
            raise ValueError("Nenhum documento encontrado. Verifique a pasta 'documents'.")

        print("✂️  Dividindo textos em chunks...")
        tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME)
        text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(
            tokenizer, 
            chunk_size=Config.CHUNK_SIZE, 
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        
        chunks = text_splitter.split_documents(documents)
        print(f"✅ Processamento concluído: {len(chunks)} chunks criados.")
        return chunks