import random, config

import openai, tweepy

#OpenAI API credentials
openai.api_key =config.open_ai_key

print("Connected to Twitter")


def create_tweet(prompt):
    text = prompt["text"]
    hashtags = prompt["hashtag"]

    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text,
        max_tokens=50,
    )

    tweet = response.choices[0].text
    tweet = tweet + " " + hashtags + " " + "#ai #openai #gpt3"
    return tweet

# tweet = create_tweet()
# api.update_status(tweet)