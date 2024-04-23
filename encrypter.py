Python
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.ciphers import algorithms
from cryptography.hazmat.ciphers.modes import CBC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.serializers import PKCS1Serializer, deserialize

def encrypt_file(file_path, password):
    # Gerar chave de criptografia
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    # Criptografar o arquivo
    with open(file_path, 'rb') as f_in:
        data = f_in.read()

    cipher = algorithms.AES(key)
    mode = CBC(cipher.encryptor(os.urandom(cipher.block_size)))
    padder = mode.padder()
    encrypted_data = padder.update(data) + padder.finalize()

    # Salvar arquivo criptografado
    with open(file_path + '.enc', 'wb') as f_out:
        f_out.write(encrypted_data)

    # Salvar chave de criptografia
    with open(file_path + '.key', 'wb') as f_key:
        key_serializer = PKCS1Serializer(f_key)
        key_serializer.serialize(key)

def main():
    file_path = input('Digite o caminho do arquivo para criptografar: ')
    password = input('Digite uma senha forte: ')

    encrypt_file(file_path, password)

    print('Arquivo criptografado com sucesso!')

if __name__ == '__main__':
    main()
