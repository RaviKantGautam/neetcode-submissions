class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        send = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            send.add((local,domain))
        return len(send)