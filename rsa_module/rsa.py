import hashlib

class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = e
        self.d = self._calculate_d(e, self.phi)
        self.public_key = (self.e, self.n)
        self.private_key = (self.d, self.n)

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def _calculate_d(self, e, phi):
        for d in range(1, phi):
            if (e * d) % phi == 1:
                return d
        raise ValueError("Unable to find a valid 'd' value")

    def encrypt(self, message):
        return [(ord(char) ** self.e) % self.n for char in message]

    def decrypt(self, ciphertext):
        return ''.join([chr((char ** self.d) % self.n) for char in ciphertext])

    def sign(self, message):
        hashed = self._sha256_hash(message)
        reduced_hash = hashed % self.n
        signature = pow(reduced_hash, self.d, self.n)
        print(f"Signing: Hashed={hashed}, Reduced Hash={reduced_hash}, Signature={signature}")
        return signature

    def verify(self, message, signature):
        hashed = self._sha256_hash(message)
        reduced_hash = hashed % self.n
        decrypted_hash = pow(signature, self.e, self.n)
        print(f"Verifying: Hashed={hashed}, Reduced Hash={reduced_hash}, Decrypted Hash={decrypted_hash}")
        return reduced_hash == decrypted_hash

    def _sha256_hash(self, message):
        hashed = hashlib.sha256(message.encode()).hexdigest()
        print(f"Hash of message '{message}': {hashed}")
        return int(hashed, 16)
