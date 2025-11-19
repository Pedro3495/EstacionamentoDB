import bcrypt

def criotpgrafar(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def checar_password(senha, hashed_password_db):
    # Garante que o hash está no tipo bytes
    if isinstance(hashed_password_db, memoryview):
        hashed_password_db = hashed_password_db.tobytes()
    import bcrypt
    return bcrypt.checkpw(senha.encode('utf-8'), hashed_password_db)