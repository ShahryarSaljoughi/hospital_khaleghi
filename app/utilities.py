PRtoEN = {
    'آقا' : 'male',
    'خانم': 'female'
}

ENtoPR = {
    'male': 'آقا',
    'female': 'خانم'
}

def translate(word):
    if word in ENtoPR.keys():
        return ENtoPR[word]
    elif word in PRtoEN.keys():
        return PRtoEN[word]
    return word

def is_safe_url(url):
    return True