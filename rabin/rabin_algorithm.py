import math

class Rabin:
    def __init__(self, p, q):
        """Initialize Rabin encryption system with primes p and q."""
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError("p and q must be prime numbers.")
        if not (p % 4 == 3 and q % 4 == 3):
            raise ValueError("p and q must satisfy p ≡ 3 (mod 4) and q ≡ 3 (mod 4).")
        self.p = p
        self.q = q
        self.n = p * q  # Public key n
        self.private_key = (p, q)

    def encrypt(self, message):
        """Encrypt a message into a list of ciphertext integers."""
        m = int.from_bytes(message.encode(), 'big')
        if m >= self.n:
            raise ValueError("Message is too large for encryption. Use smaller chunks or larger primes.")
        ciphertext = (m ** 2) % self.n
        return [ciphertext]  # Return as list for consistency

    def decrypt(self, ciphertexts):
        """Decrypt a list of ciphertexts into possible plaintexts."""
        p, q = self.private_key
        n = self.n
        decrypted_messages = []

        for c in ciphertexts:
            mp = pow(c, (p + 1) // 4, p)
            mq = pow(c, (q + 1) // 4, q)

            # Chinese Remainder Theorem
            gcd, yp, yq = self.extended_euclid(p, q)
            r1 = (yp * p * mq + yq * q * mp) % n
            r2 = n - r1
            r3 = (yp * p * mq - yq * q * mp) % n
            r4 = n - r3

            # Convert results back to text
            roots = [r1, r2, r3, r4]
            for root in roots:
                try:
                    message = self.int_to_string(root)
                    if message:
                        decrypted_messages.append(message)
                except:
                    continue

        return list(set(decrypted_messages))  # Return unique messages

    @staticmethod
    def extended_euclid(a, b):
        """Extended Euclidean Algorithm to find coefficients."""
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = Rabin.extended_euclid(b, a % b)
            return gcd, y, x - (a // b) * y

    @staticmethod
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def int_to_string(num):
        """Convert an integer back to a string."""
        return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('utf-8', errors='ignore')
