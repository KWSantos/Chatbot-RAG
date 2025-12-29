import sys
import os
from dotenv import load_dotenv

load_dotenv()

from src.config import Config
from src.ingestor import DataIngestor
from src.vector_db import VectorStoreManager
from src.rag_chain import RAGPipeline

def main(): 
    Config.ensure_directories()
    
    vector_manager = VectorStoreManager()
    
    try:
        try:
            vector_store = vector_manager.get_vectorstore()
        except ValueError:
            print("⚠️ Índice não encontrado. Iniciando ingestão de dados...")
            ingestor = DataIngestor()
            chunks = ingestor.load_and_split()
            vector_store = vector_manager.get_vectorstore(chunks)
            
        pipeline = RAGPipeline(vector_store)
        chain = pipeline.get_chain()

        print("\n🤖 Assistente de Cartões de Crédito Iniciado")
        print("Digite 'sair' para encerrar.\n")

        while True:
            question = input("Pergunte: ")
            if question.lower() in ["sair", "exit", "quit"]:
                print("Encerrando...")
                break
            
            if not question.strip():
                continue

            print("\n🤔 Pensando...")
            try:
                full_response = ""
                for chunk in chain.stream(question):
                    print(chunk, end="", flush=True)
                    full_response += chunk
                print("\n" + "-"*30 + "\n")
            except Exception as e:
                print(f"Erro ao gerar resposta: {e}")

    except Exception as e:
        print(f"Erro crítico na aplicação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()