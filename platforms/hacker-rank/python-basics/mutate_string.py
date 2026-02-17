def mutate_string(s, pos, ch):
    result = ""
    i = 0
    while i < len(s):
        if i == pos:
            result += ch
        else:
            result += s[i]
        i += 1
    return result

