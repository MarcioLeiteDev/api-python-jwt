from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "123456"  # Coloque a senha real que deseja usar
hashed_password = pwd_context.hash(password)

print("Senha criptografada:", hashed_password)
