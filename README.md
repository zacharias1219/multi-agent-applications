# **Advanced Python Multi-Agent AI Application**

This project demonstrates the development of an advanced **multi-agent AI application** using **LangFlow**, **Streamlit**, and **retrieval-augmented generation (RAG)**. It integrates modern MLOps techniques, efficient use of multiple language models (LLMs), and an intuitive front-end interface.

---

## **Features**

- **Multi-Agent AI**:
  - Combines multiple LLMs for complex task routing.
  - Includes context-specific tools for mathematical and logical reasoning.
- **Modular Design**:
  - Uses LangFlow's low-code visual editor for modular AI flow construction.
  - Implements RAG to retrieve relevant notes or context dynamically.
- **Interactive UI**:
  - Built with Streamlit for a seamless and intuitive user experience.
- **Scalable Backend**:
  - AstraDB vector database integration for efficient vector operations.

---

## **Tech Stack**

- **Programming Language**: Python
- **Backend**: LangFlow, AstraDB
- **Frontend**: Streamlit
- **AI Models**: OpenAI GPT and custom tool-integrated models
- **Database**: AstraDB with vectorization capabilities

---

## **Project Structure**

```bash
├── ai.py
├── db.py
├── form_submit.py
├── profiles.py
├── main.py
├── requirements.txt
├── workflow.json
└── README.md
```

---

## **Installation**

### Prerequisites

1. **Python 3.8+**
2. **Environment Setup**:
   - Install Python packages using `pip install -r requirements.txt`.
   - Create a `.env` file and configure the following:
   - 
     ```env
     LANGFLOW_TOKEN=<your_langflow_api_token>
     ASTRA_DB_APPLICATION_TOKEN=<your_astra_db_token>
     ASTRA_ENDPOINT=<your_astra_endpoint_url>
     OPENAI_API_KEY=<your_openai_api_key>
     ```

### Steps

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/advanced-ai-multi-agent.git
   cd advanced-ai-multi-agent
   ```

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the LangFlow environment:
   - Export the LangFlow workflow JSON (`workflow.json`) via LangFlow UI.

4. Run the application:

   ```bash
   streamlit run main.py
   ```

---

## **How It Works**

### **Pipeline**

1. **User Inputs**:
   - Collect user profiles, goals, and activity levels through Streamlit forms.
   - Retrieve or dynamically store contextual notes using AstraDB.

2. **AI Routing**:
   - Dynamically routes questions to specialized agents using LangFlow.
   - Incorporates retrieval-augmented generation for contextual responses.

3. **Mathematical Operations**:
   - Integrated calculator tool for advanced calculations.
   - Logical separation ensures error-free computations.

4. **UI/UX**:
   - Interactive inputs and results visualization through Streamlit.

---

## **Usage**

1. **Start the LangFlow backend**:
   - Host the API locally or remotely.
2. **Run the main Streamlit app**:

   ```bash
   streamlit run main.py
   ```
3. **Interact**:
   - Provide your personal information.
   - Retrieve or save notes.
   - Ask complex questions and observe dynamic AI task routing.

---

## **Future Enhancements**

- Add multi-language support for global use.
- Enhance the UI with modern frameworks.
- Introduce additional tools for broader AI capabilities.

---

## **Contributing**

We welcome contributions to enhance this project! Feel free to fork the repository, add features, and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
