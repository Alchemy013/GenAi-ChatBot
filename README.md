
# Gemini LLM Q&A Chatbot

This repository hosts a simple **Streamlit-based web application** that integrates with **Google's Gemini Pro model** via the `google.generativeai` API. Powered by **LangChain**, the application enables a dynamic chatbot that holds memory of the conversation, allowing it to engage in real-time, context-aware conversations.

## Features

- **Real-time Chat** with the Gemini Pro model for user queries.
- **Conversation History** displayed in the chat interface.
- **Session Memory** that retains context throughout the conversation.
- **Instant Responses** powered by Google Generative AI.
- Utilizes the `dotenv` library for seamless environment variable management.

## Prerequisites

Before getting started, ensure that you have the following:

- Python 3.7+
- A **Google API Key** for accessing Gemini Pro.
- Basic understanding of **Streamlit** and **LangChain**.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd smart-ats-resume-analyzer
```

### 2. Create a Virtual Environment

Create a virtual environment using **Conda**:

```bash
conda create -p env python=3.10 -y
```

### 3. Install Required Dependencies

Install the necessary Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your **Google API Key**:

```bash
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the Application

Launch the application using **Streamlit**:

```bash
streamlit run app.py
```

---
