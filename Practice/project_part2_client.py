# Content of client.py; to complete/implement

from tkinter import *
import socket
import threading
from multiprocessing import current_process  # only needed for getting the current process name

class ChatClient:
    """
    This class implements the chat client.
    It uses the socket module to create a TCP socket and to connect to the server.
    It uses the tkinter module to create the GUI for the chat client.
    """

    def __init__(self, window):
        self.window = window
        self.window.title(current_process().name)

        # GUI components
        self.chat_log = Text(self.window, state='disabled', width=50, height=15)
        self.chat_log.pack(padx=10, pady=5)

        self.message_entry = Entry(self.window, width=40)
        self.message_entry.pack(side=LEFT, padx=(10, 0), pady=(0, 10))
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side=LEFT, padx=(5, 10), pady=(0, 10))

        # Start the client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 5000
        try:
            self.client_socket.connect((host, port))
        except ConnectionRefusedError:
            self.update_chat_log("Unable to connect to the server.")
            return

        # Start a thread to receive messages from the server
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        """
        Send a message to the server.
        """
        message = self.message_entry.get()
        if message:
            try:
                self.client_socket.send(message.encode())
                self.update_chat_log(f"You: {message}")
                self.message_entry.delete(0, END)
            except BrokenPipeError:
                self.update_chat_log("Connection to the server was lost.")
                self.client_socket.close()
        else:
            self.update_chat_log("Cannot send an empty message.")

    def receive_messages(self):
        """
        Receive messages from the server and display them.
        """
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    self.update_chat_log(message)
                else:
                    # Server closed connection
                    self.update_chat_log("Disconnected from the server.")
                    self.client_socket.close()
                    break
            except ConnectionAbortedError:
                break
            except OSError:
                break

    def update_chat_log(self, message):
        """
        Update the client's chat log in the GUI.
        """
        self.chat_log.config(state='normal')
        self.chat_log.insert(END, message + '\n')
        self.chat_log.config(state='disabled')
        self.chat_log.see(END)

def main():  # Note that the main function is outside the ChatClient class
    window = Tk()
    c = ChatClient(window)
    window.mainloop()

if __name__ == '__main__':  # May be used ONLY for debugging
    main()
