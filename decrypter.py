import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.ciphers import algorithms
from cryptography.hazmat.ciphers.modes import CBC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.serializers import PKCS1Serializer, deserialize

def decrypt_file(file_path, password):
    # Carregar chave de criptografia
    with open(file_path + '.key', 'rb') as f_key:
        key_data = f_key.read()
        key = deserialize(key_data, PKCS1Serializer(backend=default_backend()))

    # Descriptografar o arquivo
    with open(file_path + '.enc', 'rb') as f_in:
        encrypted_data = f_in.read()

    cipher = algorithms.AES(key)
    mode = CBC(cipher.decryptor(encrypted_data[:cipher.block_size]))
    decrypted_data = mode.update(encrypted_data[cipher.block_size:]) + mode.finalize()

    # Salvar arquivo descriptografado
    with open(file_path, 'wb') as f_out:
        f_out.write(decrypted_data)

    print('Arquivo descriptografado com sucesso!')

def main():
    file_path = input('Digite o caminho do arquivo criptografado: ')
    password = input('Digite a senha: ')

    decrypt_file(file_path, password)

if __name__ ==
