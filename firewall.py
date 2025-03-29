import random


def createipaddr(random):
    return f"192.168.63.{random}"
    print(ip_addr)
    
def checkiprules(ip,rules):
    for ruleip,action in rules.items():
        if ip in rules:
            return action
    return"allow"

def main():
    
    ip_rules={
        "192.168.63.1" : "block",
        "192.168.63.12" : "block"
        }
    for i in range(15):
        ran= random.randint(0,20)
        new_ip = createipaddr(ran)
        action = checkiprules(new_ip,ip_rules)
        packet_num = random.randint(100,1000)
        print(f"IP address {new_ip},  Action {action},  Packet_number {packet_num}")

        

