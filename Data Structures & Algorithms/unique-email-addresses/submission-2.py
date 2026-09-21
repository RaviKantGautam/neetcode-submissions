class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send = set()
        for email in emails:
            if "@" in email:
                local, domain = email.split("@")
                plus_email = local.split("+")[0]
                dotted_email = "".join(plus_email.split("."))
                real_email = dotted_email+"@"+domain
                send.add(real_email)
        return len(send)