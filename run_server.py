import http.server
import socketserver
import sqlite3
import urllib.parse
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

flag = 0
template = """
Answer the question below.

Here is the conversation history: {context}

Question:{question}

Answer:
"""

model = OllamaLLM(model="llama3.2:latest")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def handel_conversation(self, input):
        global flag
        global chain
        if flag == 0:
            context = "Answer The Questions in the context of Indian Law."
        else:
            flag = 1
        user_input = f"You : {input}"
        result =  chain.invoke({"context": context, "question": user_input })
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"
        return result

    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = urllib.parse.parse_qs(post_data)
        if self.path == '/process':
            text = form_data['text'][0]
            # add chat(input) here
            output = self.handel_conversation(text)
            print(output)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(output.encode())
        elif self.path == '/index':
            username = form_data['username'][0]
            password = form_data['password'][0]
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            conn.close()
            response = "Welcome!" if user else "Login failed. Check your credentials."
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"<script>alert('{response}'); window.location='/';</script>".encode())
        elif self.path == '/register':
            username = form_data['new_username'][0]
            password = form_data['new_password'][0]
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            try:
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                response = "Registration successful. Please log in."
            except sqlite3.IntegrityError:
                response = "Username already exists."
            conn.close()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"<script>alert('{response}'); window.location='/';</script>".encode())
if __name__ == '__main__':
    # Setup database if not exists
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history (username TEXT, message TEXT)''')
    conn.commit()
    conn.close()
    with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
