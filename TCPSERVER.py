import socket
import os


def tcp_server():
    # Obtener el puerto asignado por Render o usar uno predeterminado (5000)
    PORT = int(os.getenv("PORT", 5000))
    HOST = '0.0.0.0'  # Escuchar en todas las interfaces de red

    # Crear socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Servidor TCP escuchando en {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida con {client_address}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Recibido: {data}")

        # Enviar una respuesta al cliente
        response = "Mensaje recibido"
        client_socket.sendall(response.encode('utf-8'))

        client_socket.close()


if __name__ == "__main__":
    tcp_server()
