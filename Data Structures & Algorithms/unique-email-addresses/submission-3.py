class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send = set()
        for email in emails:
            if "@" in email:
                local, domain = email.split("@")
                send.add("".join(local.split("+")[0].split("."))+"@"+domain)
        return len(send)