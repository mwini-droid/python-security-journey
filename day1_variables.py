# === - IAM User Profile - ===
# User Profile ...
username = "MWINI" 
user_id = "10001"
role = "security_analyst"
department = "cybersecurity"
   
# === - Access Control - ===   
is_authenticated = False
mfa_enabled = True
account_locked = False
failed_attempts = 0

# Network INfo 
ip_address  = "192.168.1.10"
threat_score = 3.5

# Display Profile 
print("=== IAM User Profile ===")
print("Username:", username)
print("User ID:", user_id)
print("Role:", role)
print("Department:", department)
print("MFA Enabled:", mfa_enabled)
print("Threat SCORE:", threat_score)
print("Account Locked:", account_locked)

# show examples of some data types
print(type(user_id))
print(type(username))
print(type(account_locked))
