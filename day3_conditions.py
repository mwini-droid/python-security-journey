#---- === IAM Access Control System ===

# User Profile
username = "MWINI"
role = "admin"
is_authenticated = True
mfa_enabled = True
account_locked = False
failed_attempts = 5
threat_score = 8.5

# Aunthentication check
if is_authenticated:
    print(f"{username} is authentiacted")
else:
    print(f"{useranme}is not authenticated")
    
#Account Lock Check
if failed_attempts >= 3:
    print(f" WARNING!: {failed_attempts} failed attempts")    
else:
    print(f"Login Attempts Normal:{failed_attempts}")    
    
#Role Based Access
if role == "admin":
    print(f"{username} Full Access Granted")    
elif role == "analyst":
    print("Read Only Access Granted")
elif role == "guest":
    print("Limited Access Granted")
else:
    print("Unknown role - access denied")        

# MFA + Autehntication together
if is_authenticated and mfa_enabled:
    print("SECURE LOGIN - MFA enabled")
else:
    print("Insecure Login - MFA missing")    

# Threat Score Alert  
if threat_score >= 8.0:
    print(f"HIGH THREAT ALERT: score {threat_score}") 
elif threat_score >= 5.0:
    print(f"Medium Threat: Score {threat_score}")   
else:
    print(f"Low Threat: score {threat_score}")      
        