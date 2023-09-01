def findAndReplace(text, oldText, newText):
    i = 0
    result = ''
    while i < len(text):
        if text[i:i+len(text)] == oldText:
            result += newText
            i += len(text)

        else:
            result += text[i]
            i += 1

    return result


print(findAndReplace('firefoxbig', 'fox', 'dog'))
