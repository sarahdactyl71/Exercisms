def hey(phrase):
    if not phrase or phrase.isspace():
        return "Fine. Be that way!"
    elif '?' in phrase and all_caps(phrase):
        return "Calm down, I know what I'm doing!"
    elif phrase[-1] == '?' or (phrase[-1].isspace() and '?' in phrase):
        return "Sure."
    elif all_caps(phrase):
        return "Whoa, chill out!"
    else:
        return "Whatever."

def all_caps(phrase):
    return phrase.isupper()
