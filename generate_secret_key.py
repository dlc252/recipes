#!/usr/bin/env python3
"""
Script para generar una clave secreta segura para Django
"""
import secrets
import string

def generate_secret_key():
    """Genera una clave secreta segura similar a la de Django"""
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for _ in range(50))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Clave secreta generada:")
    print(secret_key)
    print("\nCopia esta clave y úsala como valor para SECRET_KEY en Railway")
    print("\nTambién puedes usar este comando online:")
    print("python -c \"import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%^&*(-_=+)') for _ in range(50)))\"")
