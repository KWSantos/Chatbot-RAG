# 🤖 RAG Assistant - LangChain & Ollama

Este projeto é uma implementação modular de um sistema **RAG (Retrieval-Augmented Generation)** utilizando **LangChain** e **Ollama**. A aplicação permite interagir via terminal com uma base de conhecimento formada por documentos PDF, utilizando modelos de LLM rodando localmente.

O projeto foi refatorado seguindo princípios de **Engenharia de Software**, focando em separação de responsabilidades (SoC), manutenibilidade e eficiência.

## ✨ Funcionalidades

* **RAG Local:** Utiliza modelos open-source rodando na sua própria máquina via Ollama (sem custos de API).
* **Arquitetura Modular:** Código desacoplado em módulos de ingestão, banco vetorial, configuração e pipeline de IA.
* **Persistência de Vetores:** O índice FAISS é salvo em disco (`faiss_index/`). O processamento pesado dos documentos só ocorre na primeira execução; nas seguintes, o carregamento é instantâneo.
* **Streaming de Resposta:** A resposta é gerada token por token no terminal, proporcionando uma experiência de chat fluida.
* **Observabilidade (Opcional):** Integração pronta para o **LangSmith** para tracing e debugging das cadeias de execução.

## 🛠️ Tecnologias

* **Linguagem:** Python 3.10+
* **Orquestração:** LangChain
* **LLM & Embeddings:** Ollama (Gemma 3 & BGE-M3)
* **Vector Store:** FAISS
* **Tokenização:** HuggingFace Transformers

## ⚙️ Pré-requisitos

1. Ter o [Python](https://www.python.org/) instalado.
2. Ter o [Ollama](https://ollama.com/) instalado e rodando.
3. Baixar os modelos necessários via terminal:

```bash
# Modelo de LLM (Gemma 3 - 4B)
ollama pull gemma3:4b

# Modelo de Embeddings (BGE-M3)
ollama pull bge-m3
```

> **Nota:** Se desejar alterar os modelos, edite o arquivo `src/config.py` ou utilize variáveis de ambiente.

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

### 2. Crie e ative o ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração do LangSmith (Opcional)
Para monitorar o funcionamento interno da IA, crie um arquivo `.env` na raiz do projeto com as chaves abaixo. Se não quiser usar, o projeto rodará normalmente sem ele.

```ini
# Arquivo .env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="[https://api.smith.langchain.com](https://api.smith.langchain.com)"
LANGCHAIN_API_KEY="sua-api-key-aqui"
LANGCHAIN_PROJECT="rag-local-ollama"
```

### 5. Adicione seus documentos
Coloque os arquivos PDF que deseja consultar dentro da pasta:
```
documents/
```

### 6. Execute a aplicação
```bash
python main.py
```

## 📂 Estrutura do Projeto

```text
.
├── documents/          # Coloque seus PDFs aqui
├── faiss_index/        # Banco vetorial salvo (gerado automaticamente)
├── src/                # Código fonte
│   ├── config.py       # Configurações globais
│   ├── ingestor.py     # Leitura e chunking de PDFs
│   ├── vector_db.py    # Gerenciamento do índice FAISS
│   └── rag_chain.py    # Definição do Prompt e Chain
├── main.py             # Arquivo principal (CLI)
├── requirements.txt    # Dependências
├── .env                # Variáveis de ambiente (não versionado)
└── README.md           # Documentação
```

## 🧹 Atualizando a Base de Conhecimento

O sistema verifica se a pasta `faiss_index/` existe para carregar o banco rapidamente. 

**Para adicionar ou remover documentos:**
1. Adicione/remova os PDFs na pasta `documents/`.
2. Apague a pasta `faiss_index/`.
3. Rode o `python main.py` novamente. O sistema irá reprocessar os arquivos e criar um índice atualizado.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias no código ou na documentação.