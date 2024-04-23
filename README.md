# Detailed Technical Report - Ransomware Challenge for Educational Purposes

## Introduction

This detailed technical report outlines the challenge of implementing a simple ransomware in Python, exclusively for educational purposes. The goal was to create a safe environment to explore encryption and decryption concepts, as well as to demonstrate the dangers of ransomware attacks and the importance of cybersecurity.

## Development of the Solution

The solution was divided into two main parts:

1. Encrypter.py:

   - This script uses the cryptography library to encrypt files with the AES algorithm.
   - A strong encryption key is generated using PBKDF2 and stored in a separate file.
   - The original file is encrypted and saved with the .enc extension.

2. Decrypter.py:

   - This script allows the decryption of a previously encrypted file.
   - The user needs to provide the correct password to load the encryption key.
   - The decrypted file is saved with the original name.

## Challenges and Solutions

- **Security**: It was crucial to ensure that the code was not used for malicious purposes.
  - The ransomware was designed to only work in a local environment and does not connect to the internet.
  - The user's password is stored encrypted and is not directly accessible by the code.

- **Usability**: The code was written clearly and concisely, with explanatory comments to facilitate understanding.
  - Simple on-screen instructions guide the user through the encryption and decryption process.

- **Efficiency**: The cryptography library was chosen for its reliability and performance.
  - The code was optimized to minimize the time required to encrypt and decrypt files.

## Additional Considerations

- This challenge was developed only for educational purposes and should not be used in real-world scenarios.
- It is important to emphasize that ransomware poses a serious cybersecurity threat and should be avoided at all costs.
- Organizations and individuals should take proactive measures to protect their data against ransomware attacks, such as:
  - Implementing regular data backups.
  - Keeping software and systems updated.
  - Educating employees about the risks of ransomware and phishing.
  - Utilizing robust security solutions.

## Conclusion

The challenge of implementing an educational ransomware was a valuable experience that provided insights into encryption concepts, cybersecurity, and the dangers of ransomware attacks. The developed code serves as a practical example for educational purposes and demonstrates the importance of protecting data against online threats.
