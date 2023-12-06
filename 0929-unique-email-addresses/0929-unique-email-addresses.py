class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 그냥 규칙에 따라서 파싱하면 되지 않으려나?
        
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            new_local = []
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                else:
                    new_local.append(c)
            
            email_set.add("".join(new_local) + "@" + domain)
        
        return len(email_set)