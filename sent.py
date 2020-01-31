from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sentences = ["It is very sad evening.",
"I can't take it anymore.",
"Its such a beautiful morning!",
"I hate my life. There is no point in living anymore.",
"Its hard to defend ourselves.",
"Its impossible to defeat the guy.",]

sid = SentimentIntensityAnalyzer()

for x in sentences:
    if x.count('.')>1:
        lines_list = tokenize.sent_tokenize(x)
        sentences.extend(lines_list)
        sentences.remove(x)

for x in sentences:
    ss = sid.polarity_scores(x)
#    print(x)
#    print(type(ss))
    print(ss['pos'])
