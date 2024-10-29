# server.py
import socket
from des import hex_to_bit_array, key_generation, decrypt_long_text

def server_receive_message(key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server menunggu pesan terenkripsi...")

    conn, addr = server_socket.accept()
    encrypted_message = conn.recv(1024).decode('utf-8')
    conn.close()
    server_socket.close()

    print(f"Pesan terenkripsi yang diterima: {encrypted_message}")

    key_bits = hex_to_bit_array(key)
    round_keys = key_generation(key_bits)
    decrypted_message = decrypt_long_text(encrypted_message, round_keys)

    print(f"Pesan yang didekripsi: {decrypted_message}")

if __name__ == "__main__":
    key = '133457799BBCDFF1'  # Hardcode kunci atau bisa diinput
    server_receive_message(key)
