def check_password() -> str:
    with open(r"C:\Users\rnata\OneDrive\Desktop\password.txt", "r") as f:
        password = f.read().strip()
        return password