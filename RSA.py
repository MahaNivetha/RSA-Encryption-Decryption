import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_d(e, z):
    dt = [0, 0]
    r1_s1 = [1, 0]
    r2_s2 = [0, 1]
    temp = z
    while e % z != 0:
        m = e % z
        quotient = e // z
        dt[0] = r1_s1[0] - quotient * r2_s2[0]
        dt[1] = r1_s1[1] - quotient * r2_s2[1]
        r1_s1, r2_s2 = r2_s2[:], dt[:]
        e, z = z, m
        if dt[0] <= 0:
            while dt[0] < 0:
                dt[0] = dt[0] + temp
    return dt[0]


def is_prime(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True
    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    z = (q - 1) * (p - 1)
    e = random.randrange(1, n)
    while gcd(e, z) != 1:
        e = random.randrange(1, n)
    d = get_d(e, z)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    m = ord(plaintext)
    pk0, pk1 = pk
    cipher = pow(m, pk0, pk1)
    return cipher


def decrypt(pk, ciphertext):
    pk0, pk1 = pk
    plain = chr(pow(ciphertext, pk0, pk1))
    return plain


# Testing code
if __name__ == '__main__':
    p = 1297369
    q = 1297799
    xx, xz = generate_keypair(p, q)
    print("Public Key:", xx)
    print("Private Key:", xz)

    # Example encryption and decryption
    plaintext = 'h'
    encrypted_text = encrypt(xx, plaintext)
    decrypted_text = decrypt(xz, encrypted_text)

    print("Original text:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
