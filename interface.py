import tkinter as tk
from tkinter import scrolledtext,filedialog
import threading
import os
from main import run_agent

app = tk.Tk()
app.title("CodeForgeAI")
app.geometry("950x650")
app.minsize(700, 500)

uploaded_file = ""
uploaded_filename = ""

chat_box = scrolledtext.ScrolledText(app,wrap=tk.WORD,font=("Arial", 18))
chat_box.pack(padx=20,pady=20,expand=True,fill="both")
file_label = tk.Label(app,text="No file uploaded",font=("Arial", 12))
file_label.pack()
chat_box.insert(tk.END,"Welcome to CodeForgeAI!\n\n""Your AI-powered coding assistant.\n\n""Describe what you'd like to build, fix, or understand, and I'll help you.\n\n")
input_box = tk.Entry(app,font=("Arial", 18))
input_box.pack(padx=20,pady=10,fill="x")

def add_message(message):
    chat_box.insert(tk.END,message + "\n\n")
    chat_box.see(tk.END)

def upload_file():
    global uploaded_file
    global uploaded_filename

    path = filedialog.askopenfilename(title="Select a file",filetypes=[("Code Files", "*.py *.js *.java *.cpp *.c *.go *.ts *.html *.css"),
       ("Text Files", "*.txt"),("All Files", "*.*")])

    if not path:
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            uploaded_file = f.read()
        uploaded_filename = os.path.basename(path)

        file_label.config(text=f" {uploaded_filename}")

        add_message(f"Uploaded {uploaded_filename}")

    except Exception as e:
        add_message(str(e))
def process_request():
    user_prompt = input_box.get()
    if not user_prompt:
        return

    input_box.delete(0,tk.END)

    add_message("You:\n" + user_prompt)
    add_message("CodeForgeAI:\nThinking...")

    def run():
        try:
            if uploaded_file:
                 final_prompt = f"""The user uploaded a file named:{uploaded_filename}Here is the file:{uploaded_file}User question:{user_prompt}"""
            else:
                 final_prompt = user_prompt
            response = run_agent(final_prompt)
            chat_box.delete("end-3l",tk.END)

            add_message("CodeForgeAI:\n" + response)

        except Exception as e:
            add_message("Error:\n" + str(e))

    threading.Thread(target=run).start()
upload_button = tk.Button(app,text="Upload File",font=("Arial", 14),command=upload_file)

upload_button.pack(pady=5)
send_button = tk.Button(app,text="Send",font=("Arial", 14),command=process_request)
send_button.pack(pady=10)

input_box.bind("<Return>",lambda event: process_request())
app.mainloop()