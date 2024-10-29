# client.py
import socket
from des import hex_to_bit_array, key_generation, encrypt_long_text

def client_send_message(key, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    key_bits = hex_to_bit_array(key)
    round_keys = key_generation(key_bits)
    encrypted_message = encrypt_long_text(message, round_keys)

    # Tampilkan pesan asli dan hasil enkripsi sebelum dikirim
    print(f"Pesan asli dari user: {message}")
    print(f"Teks terenkripsi yang dikirim: {encrypted_message}")
    
    client_socket.send(encrypted_message.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    key = '133457799BBCDFF1'  # Hardcode kunci atau bisa diinput
    message = input("Masukkan pesan yang ingin dienkripsi dan dikirim: ")
    client_send_message(key, message)
