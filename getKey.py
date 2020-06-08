import tweepy
import webbrowser
import keys


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

try:
	redirect_url = auth.get_authorization_url()
	webbrowser.open(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

verifier = input('Verifier:')

try:
	auth.get_access_token(verifier)
except tweepy.TweepError:
	print('Error! Failed to get access token.')

print('Acess Token:' + auth.access_token)
print('Acess Token Secret:' + auth.access_token_secret)
