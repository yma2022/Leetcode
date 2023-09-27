class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = collections.defaultdict(set)
        
        for email in emails:
            local, domain = email.split("@")
            # check if domain is valid
            domain_split = domain.split(".")
            if domain_split[-1] == "com":
                # check email local
                local = local.split("+")[0]
                local = "".join(local.split("."))
                d[domain].add(local)
        ans = 0
        for key in d:
            ans += len(d[key])
        return ans