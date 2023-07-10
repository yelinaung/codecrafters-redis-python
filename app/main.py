import socket


PONG_RESP = "+PONG\r\n"


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            if data := conn.recv(1024):
                print(f"Received {data.decode()}")
                conn.sendall(PONG_RESP.encode())
            else:
                break


if __name__ == "__main__":
    main()
