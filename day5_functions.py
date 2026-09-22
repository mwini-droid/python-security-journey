# === DAY 5 - IAM Security Functions ===

# Function 1 - Check password strength
def check_password_strength(password):
    if len(password) >= 12:
        return "[STRONG] Password is strong"
    elif len(password) >= 8:
        return "[OK] Password is acceptable"
    else:
        return "[WEAK] Password is too short!"

# Function 2 - Check if account is locked
def check_account_lock(username, failed_attempts):
    if failed_attempts >= 3:
        return f"[LOCKED] {username} locked after {failed_attempts} attempts!"
    else:
        return f"[ACTIVE] {username} is active"

# Function 3 - Assign role access
def get_access_level(role):
    if role == "admin":
        return "Full access - all systems"
    elif role == "analyst":
        return "Read only - monitoring systems"
    elif role == "guest":
        return "Limited - public areas only"
    else:
        return "No access - unknown role"

# Function 4 - Full login check
def login_check(username, password, mfa_enabled, role):
    print(f"\n=== LOGIN CHECK: {username} ===")
    print(check_password_strength(password))
    print(f"MFA: {'[ON] Secure' if mfa_enabled else '[OFF] Insecure!'}")
    print(f"Access Level: {get_access_level(role)}")

# Function 5 - Threat score rating
def rate_threat(threat_score):
    if threat_score >= 8.0:
        return "[CRITICAL] Immediate action required!"
    elif threat_score >= 5.0:
        return "[HIGH] Monitor closely"
    elif threat_score >= 3.0:
        return "[MEDIUM] Keep an eye on this"
    else:
        return "[LOW] All clear"

# === RUN ALL FUNCTIONS ===

print("=== PASSWORD CHECKS ===")
print(check_password_strength("abc"))
print(check_password_strength("kali1234"))
print(check_password_strength("kali@secure#2024"))

print("\n=== ACCOUNT STATUS ===")
print(check_account_lock("alice", 1))
print(check_account_lock("bob", 3))
print(check_account_lock("mwini", 5))

login_check("mwini", "kali@secure#2024", True, "admin")
login_check("eve", "abc", False, "guest")

print("\n=== THREAT RATINGS ===")
print(rate_threat(9.5))
print(rate_threat(6.0))
print(rate_threat(3.5))
print(rate_threat(1.0))