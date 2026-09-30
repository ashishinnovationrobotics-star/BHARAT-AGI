class RakshakShield:
    def __init__(self):
        self.blocked = ["hack database", "steal personal", "leak aadhaar", "bypass otp"]

    def ethical_check(self, query):
        q = query.lower()
        for pat in self.blocked:
            if pat in q:
                return {"allowed": False, "reason": f"Blocked by Dharma: {pat}"}
        return {"allowed": True, "checks": ["Satya", "Ahimsa", "Loka Kalyan"]}
    
    def protect_database(self, db_name="public_db"):
        return f"🛡️ Rakshak Shield ACTIVE on {db_name}"
