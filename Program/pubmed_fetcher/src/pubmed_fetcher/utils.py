import re

def is_non_academic(affil: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "faculty", "hospital", "center", "centre"]
    affil_lower = affil.lower()
    return not any(word in affil_lower for word in academic_keywords)

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text or "")
    return match.group(0) if match else None
