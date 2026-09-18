from ai_model import detect_threat


def analyze_post(post):

    result = detect_threat(post)

    return result