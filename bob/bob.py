def hey(phrase):
    if not phrase:
        return "Fine. Be that way!"
    elif phrase[-1] == '?' and all_caps(phrase):
        return "Calm down, I know what I'm doing!"
    elif phrase[-1] == '?':
        return "Sure."
    elif all_caps(phrase):
        return "Whoa, chill out!"
    else:
        return "Whatever."

def all_caps(phrase):
    return phrase.isupper()
