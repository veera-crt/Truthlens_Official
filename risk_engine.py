def classify_channel(subscribers):
    if subscribers > 1000000:
        return "Verified"
    elif subscribers > 10000:
        return "Moderate"
    else:
        return "Unverified"

def compute_risk_vector(video):
    title_lower = video["title"].lower()
    views = int(video.get("views", 0))
    likes = int(video.get("likes", 0))
    subs = int(video.get("subscribers", 50000))
    
    channel_type = classify_channel(subs)
    risk_points = 0
    reasons = []
    
    # 1. Clickbait Keywords Check
    if any(word in title_lower for word in ["shocking", "breaking", "truth", "exposed"]):
        risk_points += 2
        reasons.append("Clickbait keywords")
        
    # 2. Engagement Integrity Test
    if views > 0:
        ratio = likes / views
        if ratio < 0.02:
            risk_points += 2
            reasons.append("Low engagement")
    elif views == 0:
        risk_points += 3
        reasons.append("Missing engagement data")
        
    # 3. Trust Vectors
    if risk_points >= 4:
        risk = "HIGH"
    elif risk_points >= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"
        
    return {
        "channel_type": channel_type,
        "risk": risk,
        "reason": " + ".join(reasons) if reasons else "Normal content signals"
    }


