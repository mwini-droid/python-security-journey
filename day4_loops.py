## -- DAY 4 - Security scanning with loops

##User Database
users = ["alice", "bob", "mwini", "eve", "hacker"]
suspicious_users = ["eve", "hacker"]
locked_accounts = ["bob"]

#Scan 1 - Check All Users
print("==USER SCAN ==")
for user in users:
    print(f"Scanning : {user}")
    
#Scan 2 - Flag Suspicious users
print("\n=== THREAT DETECTON ===")
for user in users :
    if user in suspicious_users:
        print(f"ALERT: {user} is suspicious!")
    else:
        print(f" {user} is clean")  

#Scan 3  Skip locked accounts
print("\n === ACTIVE USERS ONLY ===") 
for user in users:
    if user in locked_accounts:
       print(f"Skipping locked account: {user}")  
       continue
    print(f"Processing: {user}")
    
#Scan 4 -Simulate brute force action
print("\n=== BRUTE FORCE SIMULATION ===")    
failed_attempts = 0
max_attempts = 0
while failed_attempts < max_attempts:
    failed_attempts += 1
    print(f" Failed attempt: {failed_attempts}") 
    if failed_attempts == max_attempts:
        print("Account locked after 3 attempts!")
    break

#Scan 5 - Count suspicious users
print("\n === THREAT SUMMARY ===")
threat_count = 0
for user in users :
    if user in suspicious_users:
        threat_count += 1
print(f"Total threats found; {threat_count} out of {len(users)} users")        
        


          