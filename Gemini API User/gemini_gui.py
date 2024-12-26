import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

# 1. Set your API key (Replace with your actual key)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Choose a Model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

def generate_response_stream(prompt, chat_area):
    """Generates a response from the Gemini AI model and streams the response into a chat area"""
    start_time = time.time()  # Capture start time
    try:
       response_stream = model.generate_content(prompt, stream=True)
       full_response = ""
       chat_area.config(state=tk.NORMAL) #Enable writing
       for chunk in response_stream:
           if chunk.text:
                chat_area.insert(tk.END, f"{chunk.text}", "ai")
                chat_area.see(tk.END) #makes the chat follow the stream
                chat_area.update()
                full_response += chunk.text
       chat_area.config(state=tk.DISABLED) #disable writing
       end_time = time.time()  # Capture end time
       response_time = end_time - start_time  # Calculate time taken
       return full_response, response_time

    except Exception as e:
        end_time = time.time()  # Capture end time
        response_time = end_time - start_time  # Calculate time taken
        chat_area.config(state=tk.NORMAL) #Enable writing
        chat_area.insert(tk.END, f"\nAn error occurred: {e}", "error")
        chat_area.config(state=tk.DISABLED) #disable writing
        return f"An error occurred: {e}", response_time


def send_message():
    """Handles sending the user's message and getting the AI's response."""
    user_message = prompt_entry.get()
    prompt_entry.delete(0, tk.END)  # Clear the input area
    if not user_message:
        messagebox.showerror("Error", "Please enter a message.")
        return

    chat_area.config(state=tk.NORMAL) #Enable writing
    chat_area.insert(tk.END, f"You: {user_message}\n", "user")  # Display user's message
    chat_area.config(state=tk.DISABLED) #disable writing


    chat_area.config(state=tk.NORMAL) # enable writing
    chat_area.insert(tk.END, "Generating...\n", "generating")  # Show a "loading" message
    chat_area.config(state=tk.DISABLED) # disable writing

    window.after(1, lambda: generate_response_stream(user_message, chat_area))


    chat_area.config(state=tk.NORMAL) # enable writing
    chat_area.insert(tk.END, "")
    chat_area.config(state=tk.DISABLED) # disable writing


    # we will update the response time after the generation is done
    def update_response_time(response, response_time):
      chat_area.config(state=tk.NORMAL)
      chat_area.insert(tk.END, f"Response Time: {response_time:.4f} seconds\n")
      chat_area.config(state=tk.DISABLED)
    window.after(1, lambda: generate_response_stream(user_message, chat_area))

# Set Up Tkinter window
window = tk.Tk()
window.title("Gemini AI Chatbot")
window.geometry("800x600")
window.configure(bg="#f0f0f0")

# Custom ttk styles
style = ttk.Style(window)
style.configure('Rounded.TButton', borderwidth=0, relief=tk.FLAT, padding=10, background="#4CAF50", foreground="green", bordercolor="#4CAF50", focusthickness=0, font=("Arial", 11)) #green button
style.map('Rounded.TButton', background=[('active', '#388E3C')]) #darker green on hover
style.configure("Rounded.TEntry", relief=tk.SOLID, focusthickness=0, padding=10, font=("Arial", 11), borderwidth=1, bordercolor="#ddd")
# Create widgets
chat_area = scrolledtext.ScrolledText(window, height=20, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 11), borderwidth=0, background="#ffffff", highlightthickness=0)  # Chat display area
prompt_label = ttk.Label(window, text="Type your message:", font=("Arial", 12), background="#f0f0f0")
prompt_entry = ttk.Entry(window, width=70, style="Rounded.TEntry")
send_button = ttk.Button(window, text="Send", command=send_message, style='Rounded.TButton')

# Add tags to chat_area for different formatting
chat_area.tag_config("user", foreground="#3367d6")
chat_area.tag_config("ai", foreground="green")
chat_area.tag_config("error", foreground="red")
chat_area.tag_config("generating", foreground="grey")

# Layout
chat_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
prompt_label.pack(pady=5)
prompt_entry.pack(pady=10, padx=20, fill=tk.X)
send_button.pack(pady=20)

# Handle enter key press in the prompt entry
def on_enter(event):
    send_button.invoke()
prompt_entry.bind("<Return>", on_enter)


window.mainloop()
