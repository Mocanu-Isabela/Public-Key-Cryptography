class KeyGeneration:
    def __init__(self, p=0, q=0):
        self.p = p
        self.q = q

    def generate_public_key(self) -> int:
        return self.p * self.q

    def generate_private_key(self) -> tuple:
        return self.p, self.q
