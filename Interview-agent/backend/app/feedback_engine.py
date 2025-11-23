

class FeedbackEngine:
    def generate_report(self, answers, role):
        if not answers:
            return {"summary": "You didn't answer any questions.", "scores": {}, "recommendations": []}

        communication = self._communication_score(answers)
        clarity = self._clarity_score(answers)
        depth = self._knowledge_depth(answers, role)

        recommendations = self._recommend(communication, clarity, depth, role)

        return {
            "summary": f"You answered {len(answers)} questions for the {role} role.",
            "scores": {
                "communication": round(communication, 2),
                "clarity": round(clarity, 2),
                "knowledge_depth": round(depth, 2),
            },
            "recommendations": recommendations
        }

    def _communication_score(self, answers):
        filler = ["um", "uh", "like", "you know"]
        penalty = 0
        words = 0

        for a in answers:
            parts = a.lower().split()
            words += len(parts)
            penalty += sum(1 for f in filler if f in a.lower())

        score = 0.85
        if words < 40:
            score -= 0.2

        score -= min(0.3, penalty * 0.05)
        return max(0, score)

    def _clarity_score(self, answers):
        connectors = ["because", "therefore", "as a result", "so"]
        score = 0.5
        for a in answers:
            if any(c in a.lower() for c in connectors):
                score += 0.1
        return min(1, score)

    def _knowledge_depth(self, answers, role):
        keywords = {
            "software_engineer": ["api", "performance", "design", "scalability", "latency"],
            "sales": ["closing", "customer", "objection", "pipeline"],
            "retail_associate": ["customer", "inventory", "store", "satisfaction"]
        }
        role_keys = keywords.get(role, [])
        hits = sum(1 for ans in answers for kw in role_keys if kw in ans.lower())

        return 0.4 + min(0.6, hits * 0.12)

    def _recommend(self, comm, clarity, depth, role):
        tips = []
        if comm < 0.6:
            tips.append("Work on reducing filler words and speaking with more confidence.")
        if clarity < 0.6:
            tips.append("Try connecting ideas using 'because', 'therefore', etc.")
        if depth < 0.6:
            tips.append(f"Add more {role}-specific examples to show deeper understanding.")
        if not tips:
            tips.append("Great job overall. Keep practicing!")
        return tips
