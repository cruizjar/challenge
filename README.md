# MeLiMA assistant
This project is a threat modeling assistant called MeLiMA. 
It can help identify security threats in applications and systems. 
Input: an application description 
Output: potential threats with suggested mitigations in JSON format (description and mitigation).

## Project Structure

```
fastapi-chatbot
├── app
│   ├── main.py                 # Entry point of the application and logic for interacting with the OpenAI API
├── .env                        # Environment variables (OpenAI API key)
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd apiTemp
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate a virtual environment:**
   ```
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   You should see something like this in your prompt:
   (venv) C:\your-path>
   ```

4. **Install dependencies on virtual environment:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

6. **Run the application:**
   ```
   uvicorn app.main:app --reload
   If you want to change default port (8000) to n:
   uvicorn app.main:app --port n --reload
   ```

## Usage

Once the application is running, you can interact with the assistant by sending POST requests to the `/chat` endpoint with your own application description. 
The assistant will respond based on the input provided with threats and mitigations.

