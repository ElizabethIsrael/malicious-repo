import os
def inject_malicious_code():
    os.system("echo 'MaliciousCode Executed'>>malicious_log.txt")

inject_malicious_code()