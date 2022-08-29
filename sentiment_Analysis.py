from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100,"% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100,"% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100,"% Positive")

    print("Sentence Overall Rated As", end=" ")

    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("Negative")
    else:
        print("Neutral")


print("First statement:")
sentence = "Python is the best language"
sentiment_scores(sentence)

print("Second statement:")
sentence1 = "Study is going on as usual"
sentiment_scores(sentence1)

print("Third statement:")
sentence2 = "I am very sad today"
sentiment_scores(sentence2)
