def zero(s):
    if s[0] == "0":
        return s[1:]
    return None

def one(s):
    if s[0] == "1":
        return s[1:]
    return None


def rule_sequence(s, rules):
    if not (s and rules):
        return s
    return rule_sequence(rules[0](s), rules[1:])

print(rule_sequence('0101', [zero, one, zero]))

print(rule_sequence('0101', [zero, zero]))
