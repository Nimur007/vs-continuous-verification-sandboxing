# Demo file containing flaws for pilot study evaluation gate simulation
db_password = "super_secret_password_12345"  # Hardcoded Credentials flaw

def get_user_data(user_input):
    # SQL Injection surface flaw simulation
    query = "SELECT * FROM users WHERE username = " + user_input
    return query
