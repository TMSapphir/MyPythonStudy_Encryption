# Python Journey: Encryption 🔐

Hello and welcome to my repository. I'm Tiziano! I'm currently learning more about Python, and to practice, I've tried writing two small cryptographic codes, one using the Caesar cipher method and the other using bit manipulation with the XOR operator.


## 🛠️ Project: Encryption

The repository is divided into two main phases:

- **Cesar Cipher Code:** This was my first approach, using the Caesar cipher method.
- **Advanced XOR cryptation:** This was my second approach, using XOR for bitwise manipulation.

### 🏛️ 1. Cesar Cipher Code (`cesar_cipher_code.py`)

In this first approach, I worked on character substitution based on a fixed alphabet.
- **Logic:** It uses a linear formula `(pos * 8 + 5*6) % 36`.
- **Mathematical Analysis:** I documented a cyclic behavior of period 2 (Set Even/Odd). By applying the algorithm twice, the text follows predictable patterns that I analyzed during debugging.

### 🤖 Advanced XOR Encryption (`advanced_XOR_cryptation.py`)
In this second approach, I try to write code using a symmetric encryption method using the XOR operator.
- **Technique:** Bitwise manipulation using the XOR operator (`^`).
- **Key Management:** Implementation of a rotating key using modular arithmetic, allowing passphrases of any length (even an entire Sicilian recipe!).
- **Robustness:** Use of decorators for data sanitization and type management (strings/lists).

---
Progetto realizzato da **TMSapphir** durante il percorso di studio Python. 😊👋