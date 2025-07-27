import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[*] Listening on {HOST}:{PORT}\n")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Connected by {addr}\n")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("[>] Received:\n", data.decode())
            conn.sendall(data)
