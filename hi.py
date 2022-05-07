
def Hello(lang):
    if lang == "en":
        print("hello,man")
    elif lang == "ja":
        print("こんにちは")
    else:
        print("i don't understand what lang you speak")

print("tell your lang.")
lang = input()
Hello(lang)

