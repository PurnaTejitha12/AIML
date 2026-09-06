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


## Week 7 — RAG and Retrieval

### Overview

Week 7 focused on the fundamentals of Retrieval-Augmented Generation (RAG), document retrieval, indexing, and local LLM applications.

### Topics Covered

* **Day 1:** Haystack Pipeline Architecture
* **Day 2:** Haystack Retrieval — BM25
* **Day 3:** LlamaIndex — Document Indexing and Querying
* **Day 4:** LlamaIndex + Ollama — Local RAG
* **Day 5:** Multi-Document RAG System

### Technologies Used

* Python
* Google Colab
* Haystack
* LlamaIndex
* Ollama
* Hugging Face Embeddings
* BM25
* Vector Search
* RAG

### Implementation

All Week 7 implementations are included in a single Google Colab notebook.

The notebook demonstrates:

1. Creating and working with Haystack pipelines.
2. Performing document retrieval using BM25.
3. Creating document indexes with LlamaIndex.
4. Using LlamaIndex with Ollama for local RAG.
5. Building a simple multi-document RAG system.

### Project Workflow

```text
Documents
    ↓
Document Indexing
    ↓
Retrieval
    ↓
Relevant Information
    ↓
Answer Generation
```

### Learning Outcome

By completing Week 7, I gained a basic understanding of RAG architecture, document retrieval, vector indexing, Haystack pipelines, LlamaIndex, and local LLM-based RAG applications.



# Local AI Research Assistant

A simple Retrieval Augmented Generation (RAG) application built using local AI models.

## Features

- Document retrieval
- Sentence Transformer embeddings
- Top-K retrieval
- Local FLAN-T5 answer generation
- Grounded answers
- FastAPI API
- Docker support
- Basic RAG evaluation
- Automated API testing

## Technologies

- Python
- Sentence Transformers
- Hugging Face Transformers
- FLAN-T5
- FastAPI
- Docker
- Pytest
- Google Colab

## Project Structure

```text
local-ai-research-assistant/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── local-ai-research-assistant.ipynb


## Week 9 — AI/ML 3M Stack Practical

### Overview

Week 9 focused on building multi-agent AI workflows using the approved AI/ML 3M stack:

- CrewAI
- LangChain / LangGraph concepts
- MLflow concepts
- Ragas concepts
- MLOps concepts

The practical work was completed in a single Google Colab notebook and committed to Git day-wise.

### Notebook

`Week 9/W9_AIML_CrewAI_5Day_Practical.ipynb`

Additional notebook versions were saved day-wise during development.

---

## Day 1 — CrewAI Fundamentals

### Topics

- CrewAI Agents
- CrewAI Tasks
- CrewAI Crews
- Sequential agent workflow
- Researcher, Writer, and Reviewer agents

### Work Completed

Created three CrewAI agents:

1. **Researcher** — collects and organizes research information.
2. **Writer** — converts research findings into a structured article.
3. **Reviewer** — checks the article for clarity, completeness, and quality.

Created tasks for each agent and executed them as a sequential crew.

### Git Commit

`feat: crewai — define multi-agent research crew`

---

## Day 2 — CrewAI Tools

### Topics

- Web search
- Code execution
- CrewAI tools
- No-API-key workflow

### Work Completed

Added a simple web-search workflow using the Wikipedia public API without requiring a paid API key.

Added Python code execution for basic numerical analysis and demonstrated how CrewAI tools can be used by agents.

### Git Commit

`feat: crewai — add web search and code execution tools`

---

## Day 3 — Multi-Agent Research Pipeline

### Topics

- Multi-agent systems
- Sequential pipelines
- Task dependencies
- Research → Writing → Review workflow

### Work Completed

Built a multi-agent research pipeline where:

```text
Researcher
    ↓
Research Task
    ↓
Writer
    ↓
Writing Task
    ↓
Reviewer
    ↓
Final Review

## Week 10 — LangGraph

### Day 1 — Stateful Agent Graphs

**Topic:** LangGraph — Stateful Agent Graphs

#### What I Built

- Built a LangGraph workflow using `classify → route → respond` nodes.
- Added conditional edges based on classification.
- Tested the graph with 5 different inputs.
- Verified that inputs were routed correctly.
- Implemented human-in-the-loop using LangGraph `interrupt()`.
- Tested graph pause, human feedback, and resume.
- Used `MemorySaver` for checkpointing graph state.

#### Graph Flow

```text
START
  ↓
classify
  ↓
route
  ↓
conditional routing
  ├── technical
  ├── billing
  └── general
        ↓
   human_review
        ↓
     respond
        ↓
       END


W10D2 — LangGraph State Machines & Conditional Edges

Today I built a simple stateful agent workflow using LangGraph. The workflow follows three main steps: classify → route → respond. The input is first classified, then conditionally routed to the correct path, and finally a response is generated.

I tested the workflow with multiple inputs to verify that the routing worked correctly. I also added a human-in-the-loop interrupt, which pauses the workflow, waits for human input, and then resumes execution.

Technologies Used
Python
LangGraph
LangChain
Google Colab
Git & GitHub
What I Learned

I learned how LangGraph manages state between nodes, how conditional edges control the flow of a graph, and how human-in-the-loop interrupts can be used to pause and resume an AI workflow.

Workflow

START → classify → route → respond → END

For requests requiring human review:

START → classify → route → human_review → END

LangGraph Stateful Agent with Routing
Overview

This project implements a simple stateful agent using LangGraph with three nodes:

classify → route → respond

The graph classifies the user's input, routes it based on the classification, and generates an appropriate response.

Features
3-node LangGraph workflow
Conditional routing based on classification
Billing, technical, and general request handling
Human-in-the-loop interruption for uncertain requests
Resume graph execution after human input
Tested with 5 different inputs
Routing verification using assertions
Technologies Used
Python
LangGraph
LangChain Core
Google Colab
Git
GitHub
Graph Flow
START
  |
  v
classify
  |
  v
route
  |
  +---- billing ------+
  |                   |
  +---- technical ----+--> respond --> END
  |                   |
  +---- general ------+
  |
  +---- human_review --> interrupt --> human input --> respond

Testing

The graph was tested with inputs related to:

Billing/refund
Technical errors
General queries
Invoice/payment issues
Uncertain requests requiring human review

All expected routing tests passed successfully.

Human-in-the-Loop

For uncertain requests, the graph pauses using LangGraph's interrupt() function.

A human provides the classification, and execution is resumed using:

Command(resume="technical")


This demonstrates stateful execution and human intervention in the workflow.

Git

Feature branch:

feat/aiml-W10-your-name


Commits:

feat: langgraph — stateful agent graph with routing
test: add routing and human-in-the-loop verification

Result

Successfully built and tested a stateful LangGraph agent with conditional routing and human-in-the-loop support.

## W10D4 — Human-in-the-Loop with LangGraph

### Today's Work

- Built a stateful LangGraph workflow with classification and response routing.
- Added conditional edges based on the classification result.
- Tested the graph with 5 different inputs to verify correct routing.
- Implemented Human-in-the-Loop using LangGraph `interrupt()`.
- Tested pausing the workflow, receiving human input, and resuming execution.
- Created Git commits and pushed the Day 4 implementation to the feature branch.

### Technologies Used

- Python
- LangGraph
- Git & GitHub

### Git Commits

- `feat: langgraph — stateful agent graph with routing`
- `feat: add human-in-the-loop interrupt and resume`


# W10D5 – Stateful Customer Support Agent

## Project Description

Built a Stateful Customer Support Agent using Python that can remember information from previous conversations and provide context-aware responses.

## Features

- Maintains conversation history.
- Remembers the customer's name.
- Remembers the order number.
- Detects common customer issues such as delivery, refund, damaged products, and cancellation.
- Uses previous conversation context to generate relevant responses.
- Provides an interactive chatbot interface.
- Includes automated tests to verify conversation state and memory.

## Technologies Used

- Python
- Google Colab
- Regular Expressions
- Dataclasses

## Example Conversation

```text
You: Hi, my name is Rahul and my delivery is late
Agent: Rahul, I can help with the delivery issue. Please provide your order number.

You: My order number is ORD12345
Agent: Rahul, I can help check the delivery status for order ORD12345.

You: Can you check my order?
Agent: Rahul, I can help check the delivery status for order ORD12345.
