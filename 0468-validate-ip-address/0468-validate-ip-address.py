class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if len(queryIP.split(".")) == 4:
            print(queryIP.split("."))
            for ele in queryIP.split("."):
                if len(ele) > 1 and ele[0] == "0" or not ele.isdigit():
                    return "Neither"
                if int(ele) < 0 or int(ele) > 255:
                    return "Neither"
            return "IPv4"           
            
        if len(queryIP.split(":")) == 8:
            for ele in queryIP.split(":"):
                if not ele or len(ele) > 4:
                    return "Neither"
                for c in ele:
                    if c.isdigit():
                        continue
                    if 'a' <= c <= 'f' or 'A' <= c <= 'F':
                        continue
                    return "Neither"
            return "IPv6"            
            
            
        return "Neither"
        