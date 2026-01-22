#  🔐 Python Journey: Encryption 

Hello and welcome to my repository. I'm Tiziano! I'm currently learning more about Python, and to practice, I've tried writing two small cryptographic codes, one using the Caesar cipher method and the other using bit manipulation with the XOR operator.

## 🤓 Arguments: what i'm learning?
In this project I've trained and experimented with some tools for my first time

- **decorators:** This is the first I've done this project. I read about them, and although I understood in theory how they worked, I couldn't "visualize" and "feel" them. For this reason, I experimented a bit (as you can see) to understand the logic. In doing so, I also learned the difference between a function extracting a function and a variable (the wrapper was a counterintuitive solution at first, as I didn't fully understand the decorator's logic).
- **flexible lists:** It's the first time that I've used the `.append()` string in a empty list. in fact, coming from university and with a vague knowledge of C, I was not used to thinking of the list as a "container to be filled after creation"
- **XOR operator and bitwise manipulation:** I've studied this operator at school but I've never used in this tipe of work and, at the beginning, I've not imagined that I could use it as a Encryption method

## 🛠️ Project: Encryption

The repository is divided into two main phases:

- **Cesar Cipher Code:** This was my first approach, using the Caesar cipher method.
- **Advanced XOR cryptation:** This was my second approach, using XOR for bitwise manipulation.

### 🏛️ Cesar Cipher Code (`cesar_cipher_code.py`)

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

