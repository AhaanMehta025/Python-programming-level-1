from textblob import TextBlob
# a = TextBlob('Thas is wrng spellng')
# print(a.correct())

# b = TextBlob('Como Estas')
# print(b.detect_language())

b = TextBlob('This sentence is in english')
print(b.translate(from_lang="en", to = "hi"))