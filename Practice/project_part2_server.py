# Content of server.py; To complete/implement

from tkinter import *
import socket
import threading

class ChatServer:
    """
    This class implements the chat server.
    It uses the socket module to create a TCP socket and act as the chat server.
    Each chat client connects to the server and sends chat messages to it. When 
    the server receives a message, it displays it in its own GUI and also sends 
    the message to other clients.  
    It uses the tkinter module to create the GUI for the server client.
    """

    def __init__(self, window):
        self.window = window
        self.window.title("Chat Server")

        # GUI components
        self.chat_log = Text(self.window, state='disabled', width=50, height=20)
        self.chat_log.pack(padx=10, pady=10)

        # Start the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        port = 5000
        self.server_socket.bind((host, port))
        self.server_socket.listen()

        self.clients = []
        self.client_usernames = {}

        # Start accepting clients in a separate thread
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        """
        Accept incoming client connections.
        """
        while True:
            client_socket, client_address = self.server_socket.accept()
            # Assign a username based on the client's address
            username = f"Client{len(self.clients) + 1}"
            self.client_usernames[client_socket] = username
            self.clients.append(client_socket)
            # Start a thread to handle client messages
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()
            self.update_chat_log(f"{username} has connected.")

    def handle_client(self, client_socket):
        """
        Handle incoming messages from a client.
        """
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    username = self.client_usernames[client_socket]
                    formatted_message = f"{username}: {message}"
                    self.update_chat_log(formatted_message)
                    self.broadcast_message(formatted_message, client_socket)
                else:
                    # Client has disconnected
                    self.remove_client(client_socket)
                    break
            except ConnectionResetError:
                # Handle abrupt disconnection
                self.remove_client(client_socket)
                break

    def broadcast_message(self, message, from_socket):
        """
        Send a message to all connected clients except the sender.
        """
        for client in self.clients:
            if client != from_socket:
                try:
                    client.send(message.encode())
                except BrokenPipeError:
                    self.remove_client(client)

    def remove_client(self, client_socket):
        """
        Remove a client from the server.
        """
        if client_socket in self.clients:
            username = self.client_usernames[client_socket]
            self.clients.remove(client_socket)
            del self.client_usernames[client_socket]
            self.update_chat_log(f"{username} has disconnected.")
            client_socket.close()

    def update_chat_log(self, message):
        """
        Update the server's chat log in the GUI.
        """
        self.chat_log.config(state='normal')
        self.chat_log.insert(END, message + '\n')
        self.chat_log.config(state='disabled')
        self.chat_log.see(END)

def main():  # Note that the main function is outside the ChatServer class
    window = Tk()
    ChatServer(window)
    window.mainloop()

if __name__ == '__main__':  # May be used ONLY for debugging
    main()
