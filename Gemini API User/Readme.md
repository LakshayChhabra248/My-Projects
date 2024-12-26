# 💬 Gemini AI Chatbot

This project implements a simple chatbot powered by the Google Gemini AI model. It features a graphical user interface (GUI) using Tkinter, providing a real-time, streamed response experience.

## ✨ Features

*   **💬 Chat-Style Interface:**  A simple GUI to send prompts and receive responses.
*   **⚡ Real-time Streaming:** The Gemini AI's responses are displayed in real-time as they are being generated.
*   🎨 **Styled Messages**: User messages and AI responses have distinct colors for readability.
*   ⚠️ **Error Handling**: The app will handle any errors gracefully.
*   🔑 **API Key Management**: The API key is managed with a .env file.

## 🛠️ Setup

### Prerequisites

*   🐍 **Python 3.6+**
*   📦 **pip** (Python package installer)
*   🔑 **Google AI API Key**: Get one at [https://ai.google.dev/](https://ai.google.dev/)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/LakshayChhabra248/My-Projects/tree/b754e0ec3eb62aa45dcbfcdf2ebafa97b2067251/Gemini%20API%20User
    cd 'GEMINI API USER'
    ```
 
2.  **Install Dependencies:**
    ```bash
    pip install google-generativeai tkinter python-dotenv
    ```
3.  **Create a `.env` file:**
    *   Create a file named `.env` in the same directory as your Python script.
    *   Add your Google AI API key, replacing `YOUR_API_KEY_HERE` with your actual key:

        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

## 🏃‍♂️ How to Run

1.  **Execute the Script:**

    ```bash
    python gemini_gui.py
    ```



2.  **Interact with the Chatbot:**
    *   A window will appear.
    *   Type your message in the input box at the bottom.
    *   Press the "Send" button or hit `Enter` to send the message.
    *   The response will be streamed into the chat box above, with styled colors for user and AI text.
    *   The response time will be displayed under the response.

## 📝 Important Notes

*   🤖 **Model:** The project uses the `gemini-2.0-flash-exp` model.

## 🤝 Contributing

If you'd like to contribute to this project, please:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes and push to your fork.
4.  Submit a pull request.
