# AIML Week 1

Completed NumPy fundamentals:

* Array creation
* Broadcasting
* Vectorized operations
* Matrix multiplication
* Statistical analysis using CSV dataset
Week 1 submission completed.

## Week 2: Machine Learning Preprocessing

Topics Covered:

* Feature Engineering \& Encoding
* Feature Scaling \& Feature Selection
* Handling Imbalanced Data using SMOTE
* Train/Test Split and Cross Validation
* End-to-End Preprocessing Pipeline

Tools \& Technologies:

* Python
* Google Colab
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn

Outcome:
Learned and implemented machine learning preprocessing techniques including feature creation, encoding, scaling, feature selection, data balancing, and building an end-to-end preprocessing pipeline.



\## Week 3: Machine Learning Algorithms



Topics Covered:

\- Linear Regression

\- Logistic Regression \& Classification

\- Decision Trees \& Random Forests

\- SVM and KNN

\- Hyperparameter Tuning using GridSearchCV and RandomizedSearchCV



Tools \& Technologies:

\- Python

\- Google Colab

\- Pandas

\- NumPy

\- Scikit-learn

\- Matplotlib



Outcome:

Implemented supervised machine learning algorithms, evaluated models using performance metrics, and optimized models using hyperparameter tuning techniques.

## Week 4: Model Evaluation and Deployment

Topics Covered:
- Model Evaluation Metrics (Precision, Recall, AUC)
- Bias-Variance Tradeoff
- Regularization Techniques
- Model Serialization using Pickle and Joblib
- FastAPI Model Serving Endpoint
- Sentiment Classifier Capstone Project

Tools & Technologies Used:
- Python
- Google Colab
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Pickle
- FastAPI

Outcome:
Learned how to evaluate machine learning models using different metrics, reduce overfitting using regularization techniques, save and load trained models using serialization methods, and understand how machine learning models can be deployed using FastAPI.

## Week 5: Running LLMs Locally with Ollama

### W5D1: Ollama Setup & First Local LLM Inference

Completed tasks:
- Installed and configured Ollama for running Large Language Models locally.
- Pulled and tested the llama3.2:3b model.
- Ran first local inference using Ollama.
- Built a Python script to interact with Ollama API.
- Added custom system prompts for controlling model responses.
- Tested multiple prompts using local LLM inference.
- Compared response quality between llama3.2:3b and qwen2.5:3b models.

### Tools & Technologies Used
- Ollama
- Python
- VS Code
- Requests Library
- Local LLM Models (llama3.2:3b, qwen2.5:3b)

### Key Learnings
- Understanding how to run LLMs locally without cloud APIs.
- Using Ollama API for programmatic model interaction.
- Difference between local inference and cloud-based AI services.
- Effect of model selection and prompts on response quality.

### Deliverables
- Python script for Ollama API inference
- Model comparison documentation
- Output evidence screenshots
# Week 5 - Day 2: Prompt Engineering & System Prompts with Ollama

## Tasks Completed
- Installed Ollama
- Pulled llama3.2:3b and qwen2.5:3b models
- Built a Python script using the Ollama API with a custom system prompt
- Tested five prompts
- Compared llama3.2:3b and qwen2.5:3b responses
- Documented model differences

## Files
- ollama_system_prompt.py
- compare_models.py

## Technologies Used
- Python
- Ollama
- Requests Library
# ChromaDB Vector Store Setup & Ollama RAG

## Overview
Implemented ChromaDB vector store setup, document embeddings, similarity search, metadata filtering, and PDF retrieval with Ollama integration.

## Tools Used
- Python
- ChromaDB
- Ollama
- Sentence Transformers
- PyPDF

## Implemented Tasks
- Created ChromaDB collection
- Added documents with embeddings
- Performed similarity search
- Applied metadata filtering
- Embedded PDF documents
- Retrieved top-3 relevant chunks
- Passed retrieved context to Ollama LLM

## Run

Install dependencies:

pip install chromadb sentence-transformers pypdf ollama

Run:

python ollama_rag.py

## Result
Successfully built a basic RAG pipeline using ChromaDB and Ollama.

## Week 5

# W5D4: Semantic Search with ChromaDB

## Objective

Implemented semantic search using ChromaDB by creating a vector store, generating embeddings, and retrieving relevant documents based on semantic similarity.

## Work Done

- Installed and configured ChromaDB.
- Created ChromaDB collections for storing vector embeddings.
- Used SentenceTransformer to generate document embeddings.
- Added 20 documents with metadata into the vector database.
- Implemented cosine similarity search to retrieve relevant documents.
- Implemented metadata filtering for targeted document retrieval.
- Verified search results manually.

### PDF Embedding and Retrieval

- Uploaded and processed PDF documents.
- Extracted text using PyPDF.
- Split documents into smaller chunks using text splitters.
- Generated embeddings for PDF chunks.
- Stored chunks in ChromaDB.
- Retrieved the top-3 relevant chunks for user queries.

### Workflow

### Technologies Used

- Python
- Google Colab
- ChromaDB
- SentenceTransformers
- PyPDF
- LangChain Text Splitter
- Git & GitHub


---

# W5D5: Local Q&A Bot — Ollama + ChromaDB

## Objective

Built a local question-answering chatbot by combining ChromaDB vector retrieval with Ollama local LLM inference using a Retrieval-Augmented Generation (RAG) pipeline.

## Work Done

- Created a knowledge base using PDF documents.
- Extracted and processed document content.
- Split documents into smaller chunks for efficient retrieval.
- Generated embeddings using SentenceTransformer.
- Stored document embeddings in ChromaDB.
- Implemented semantic retrieval to find relevant context.
- Retrieved top relevant chunks based on user questions.
- Integrated retrieved context with Ollama for generating answers.

### RAG Pipeline

### Features Implemented

- Semantic document search
- Vector-based retrieval
- PDF question answering
- ChromaDB vector storage
- Ollama local LLM integration
- Context-based response generation

### Technologies Used

- Python
- Ollama
- ChromaDB
- SentenceTransformers
- LangChain
- PyPDF
- Google Colab
- VS Code
- Git & GitHub


## Challenges Faced

- Configuring Ollama with the local environment.
- Understanding embedding generation and vector similarity search.
- Improving retrieval quality through document chunking.
- Testing local LLM responses with retrieved context.

## Learning Outcomes

- Learned how vector databases store and retrieve information.
- Understood semantic similarity using embeddings.
- Implemented a complete RAG workflow.
- Learned how ChromaDB and Ollama can be combined to build local AI applications.


# Week 6 — LangChain Fundamentals & RAG

## Overview
Implemented LangChain-based LLM applications using Ollama, ChromaDB, and Retrieval Augmented Generation (RAG). Completed practical tasks covering chains, memory, agents, vector databases, and document chatbots.

## Technologies Used
- Python
- Google Colab
- LangChain
- Ollama (Llama 3.2)
- ChromaDB
- HuggingFace Embeddings
- PyPDF

## Tasks Completed

### Day 1 — LangChain Chains & Prompts
- Built PromptTemplate → Ollama LLM → OutputParser pipeline.
- Tested the chain with multiple inputs.

### Day 2 — Conversation Memory
- Implemented ConversationBufferMemory.
- Verified that conversation history is maintained across multiple interactions.

### Day 3 — LangChain Agents & Tools
- Created an agent with:
  - Calculator tool
  - Web search stub tool
- Tested agent execution with different tasks.

### Day 4 — ChromaDB Vector Store
- Created vector collections.
- Added documents and generated embeddings.
- Performed similarity search and metadata filtering.

### Day 5 — Document Chatbot using RAG
- Built a PDF-based chatbot.
- Loaded PDF documents.
- Split documents into chunks.
- Created embeddings.
- Stored vectors in ChromaDB.
- Retrieved relevant chunks and generated answers using Ollama.

## Project Workflow

PDF Document  
↓  
PDF Loader  
↓  
Text Chunking  
↓  
Embeddings Generation  
↓  
ChromaDB Vector Store  
↓  
Similarity Retrieval  
↓  
Ollama LLM Response

## Notebook
Week 6 implementation was completed using Google Colab:

`Week6_LangChain.ipynb`

## Git Branch
`feat/aiml-W6-your-purnatejitha`
