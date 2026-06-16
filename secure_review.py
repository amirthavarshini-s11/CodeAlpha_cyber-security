import time

print("=========================================")
print("  TASK 3: SECURE CODING REVIEW TOOL      ")
print("=========================================")
time.sleep(1)

print("\n[!] 1. Analyzing VULNERABLE Code (SQL Injection Risk)...")
print("-" * 50)
vulnerable_code = """
# BAD PRACTICE:
def get_user_data(username):
    # பயனர் உள்ளீட்டை நேரடியாக குவரியில் இணைப்பது தவறு
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query
"""
print(vulnerable_code)
time.sleep(2)

print("\n[✔] 2. Analyzing SECURE Code (Mitigated)...")
print("-" * 50)
secure_code = """
# GOOD PRACTICE:
def get_user_data_secure(username):
    # Parameterized Query பயன்படுத்துவது பாதுகாப்பானது
    query = "SELECT * FROM users WHERE username = %s"
    return query, (username,)
"""
print(secure_code)
time.sleep(1.5)

print("\n=========================================")
print("[✔] Code Review Analysis Completed Successfully!")
print("=========================================")
