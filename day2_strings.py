# === DAY 2 - STRINGS OPERATIONS ===

# LOG ENTRY SIMULATION
log_entry = "failed login: user=mwini ip=192.168.1.10"
username = "mwini"
role = "security_analyst"
ip_address = "192.168.1.10"

#Uppercase alert 
print(log_entry.upper())

# Check if failed is in log 
print("failed" in log_entry)

# Password length Check
password = "kali@1234"
print("Password Length:", len(password))

# F-string Alert Message 
print(f"ALERT: {username} with role {role} from {ip_address}")

# Split log into parts
parts = log_entry.split(":")
print(parts)

# Replace Username
print(username.replace ("mwini", "anonymous"))