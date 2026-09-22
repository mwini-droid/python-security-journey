# === DAY 6 - IAM User Management with Lists ====

# --- Our user databaseas lists ---
all_users = ["alice", "bob", "mwini", "eve", "charlie"]
admin_users = ["alice", "mwini"]
suspicious_users = ["eve", "hacker"]
locked_accounts = ["bob"]
ip_blacklist = ["192.168.1.100", "10.0.0.99"]

# --- Section 1:Show all Users ---
print("=== SHOW ALL USERS === ")
for user in all_users:
    print(f"-  {user}")
print(f"Total Users: {len(all_users)}")

# --- Section 2: Check admin access ---
print("\n === ADMIN CHECK === ")
for user in all_users:
    if user in admin_users:
        print(f"[ADMIN] {user} has full access")
    else:
        print(f"[USER] {user} has limited access")

# --- Section 3:Flag Suspicious users ---
print("\n === THREAT SCAN ===")
threats_found = []
for  user in all_users:
    if user in suspicious_users:
        threats_found.append(user)
        print(f"[ALERT] {user} is supicious!")
    else:
        print(f"[CLEAN] {user} is safe")

print(f"\nThreats Found: {len(threats_found)}")
print(f"Threat List: {threats_found}")

#--- Section 4: Skip Locked Accounts ---
print("\n=== ACTIVE USERS ONLY ==== ")
active_users = []
for user in all_users:
    if user not in locked_accounts:
        active_users.append(user)
print(f"Active Users: {active_users}")
print(f"Total Active: {len(active_users)}")

# --- Section 5: IP Blacklist check ---
print("\n=== IP BLACKLIS CHECK === ")
incoming_ips = ["192.168.1.1", "192.168.1.100", "10.0.0.1", "10.0.0.99"]
for ip in incoming_ips:
    if ip in ip_blacklist:
        print(f"[BLOCKED] {ip} is blacklisted!")
    else:
        print(f"[ALLOWED] {ip} allowed to connect")

# --- Section 6: ADD and Remove users ---
print("\n === USER MANAGEMENT === ")
print(f"Before: {all_users}")
all_users.append("newuser")
print(f"After Adding newuser: {all_users}")
all_users.remove("charlie")
print(f"After Removing Charlie: {all_users}")

                    
                                