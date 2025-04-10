# 💬 Phi Quick Chat AI (LangChain + Streamlit)

This is a simple chatbot application built using [LangChain](https://www.langchain.com/), [Ollama](https://ollama.ai/), and [Streamlit](https://streamlit.io/). It uses the `phi` language model to answer user queries in a conversational interface.

---

## 🚀 Features

- Uses LangChain's `ChatPromptTemplate` for flexible prompt structuring.
- Connects to the `phi` model via Ollama for fast and efficient local inference.
- Built with a clean, minimal UI using Streamlit.
- Tracks sessions and interactions using LangSmith for better observability.

---

## Requirements 

streamlit,
langchain,
langchain-core,
langchain-community,
python-dotenv

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   LANGCHAIN_API_KEY=your_langchain_api_key
   streamlit ollama run phi 



