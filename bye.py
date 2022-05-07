
def Bye(lang):
    if lang == "en":
        print("Bye,man")
    elif lang == "ja":
        print("さようなら")
    else:
        print("i don't understand what lang you speak")

print("tell your lang. expect for en or ja")
lang = input()
Bye(lang)

