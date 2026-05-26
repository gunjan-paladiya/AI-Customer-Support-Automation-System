# AI Customer Support Automation System

An intelligent multi-agent AI customer support automation platform built using CrewAI, LangChain, OpenAI APIs, FastAPI, and Retrieval-Augmented Generation (RAG) pipelines.

## Features

- Multi-Agent AI Workflow
- Ticket Classification
- Sentiment Analysis
- Retrieval-Augmented Generation (RAG)
- AI Verification & Self Reflection
- FastAPI REST APIs
- Vector Database Integration
- Docker Support

## Tech Stack

- Python
- CrewAI
- LangChain
- OpenAI API
- FastAPI
- FAISS

## Installation

```bash
git clone https://github.com/gunjan-paladiya/ai-customer-support-automation-system.git
cd ai-customer-support-automation-system
pip install -r requirements.txt
```

## Environment Variables

Create `.env`:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Run Project

```bash
python run.py
```

## API Endpoint

POST `/support`

Example:

```json
{
  "query": "I was charged twice for my subscription."
}
```

## Skills Demonstrated

- Multi-Agent Systems
- RAG Pipelines
- Prompt Engineering
- FastAPI Development
- Vector Databases
- Semantic Search
- AI Workflow Automation

## Author

Gunjan Paladiya
