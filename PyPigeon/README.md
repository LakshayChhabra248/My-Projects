# 🐦 PyPigeon - WhatsApp Auto-Messenger

PyPigeon is a Streamlit-based tool to automate sending WhatsApp messages using data from an Excel file. It is designed for sending financial updates (Purchase, Payment, Balance).

## Features
- **Excel Integration**: Upload your data easily.
- **Automated Messaging**: Uses a real Chrome browser to send messages via WhatsApp Web.
- **Smart Delays**: Randomized delays between messages to prevent spam detection.
- **Data Generation**: Built-in tool to generate sample data for testing.

## Installation

1. **Install Python**: Ensure Python 3.8+ is installed.
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the App**:
   ```bash
   streamlit run app.py
   ```
2. **Generate Data**: Use the sidebar button to download a sample Excel file.
3. **Upload Data**: Upload your `.xlsx` file.
4. **Start**: Click "Start Sending Messages".
5. **Scan QR**: A Chrome window will open. Scan the QR code with your WhatsApp mobile app.
6. **Watch**: The bot will send messages one by one.

## Important Notes
- **Do not minimize** the Chrome window while it is running (you can keep it in the background, but don't minimize it to the taskbar if possible, though Selenium usually handles it).
- **Internet Connection**: Ensure a stable connection for WhatsApp Web to load.
- **Privacy**: Your data stays on your machine. The automation runs locally.

## Troubleshooting
- **Chrome Driver Error**: If the browser doesn't open, try running `pip install webdriver-manager --upgrade`.
- **Login Timeout**: If the QR code isn't scanned in time, the app will stop. Refresh and try again.
