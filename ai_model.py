from transformers import pipeline

classifier = pipeline(
    'sentiment-analysis'
)


THREAT_KEYWORDS = {

    'Credential Theft': [
        'password',
        'credentials',
        'bank account',
        'stolen account',
        'login data'
    ],
     'Malware': [
        'virus',
        'trojan',
        'ransomware',
        'malware'
    ],

    'Scam': [
        'fraud',
        'scam',
        'phishing',
        'fake payment'
    ]
}


def detect_threat(post):

    post_lower = post.lower()

    category = 'Safe'

    risk = 'LOW'
    confidence = 0.20

    for threat_type, keywords in THREAT_KEYWORDS.items():

        for keyword in keywords:

            if keyword in post_lower:

                category = threat_type

                result = classifier(post)[0]

                confidence = round(result['score'], 2)

                if confidence > 0.80:
                    risk = 'HIGH'

                elif confidence > 0.50:
                    risk = 'MEDIUM'

                else:
                    risk = 'LOW'
                    return {
                    'content': post,
                    'category': category,
                    'risk_level': risk,
                    'confidence': confidence
                }

    return {
        'content': post,
        'category': category,
        'risk_level': risk,
        'confidence': confidence
    }