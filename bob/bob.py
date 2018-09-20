def hey(phrase):
    if phrase[-1] == '?' and all_caps(phrase):
        return "Calm down, I know what I'm doing!"
    elif phrase[-1] == '?':
        return "Sure."
    elif all_caps(phrase):
        return "Whoa, chill out!"
    elif not phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."

def all_caps(phrase):
    return phrase.isupper()

# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
#
# Bob answers 'Sure.' if you ask him a question.
#
# He answers 'Whoa, chill out!' if you yell at him.
#
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
#
# He says 'Fine. Be that way!' if you address him without actually saying anything.
#
# He answers 'Whatever.' to anything else.
