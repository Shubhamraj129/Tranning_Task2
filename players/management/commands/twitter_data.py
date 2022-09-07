from players.models import *
from django.core.management.base import BaseCommand
import tweepy


class Command(BaseCommand):

    def handle(self, *args, **options):
        api_key = "Hyr3SrTEUGywlsiRXD4meLrwC"
        api_secrets = "qA1nuhnioOrrAIXiV4oNHW8JFhoXefNgK9Q6TairlQrZb52YxF"
        access_token = "1564199078359347200-1JPB5B052wDZHHziLhzmtFoAGQEYcM"
        access_secret = "FECUOmmTomauKjo1XmaK8wmXSZFFYqUC9Submv8djpJ9q"
        auth = tweepy.OAuthHandler(api_key, api_secrets)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)  # , wait_on_rate_limit=True,
        api.verify_credentials()
        for x in TwitterInfo.objects.values('username')[:4]:
            frist_name = x.get('username')
            print(frist_name)
            try:
                user = api.get_user(screen_name=frist_name)
                tweets_count = user.statuses_count
                print(tweets_count)
                profile_name = user.name
                print(profile_name)
                location = user.location
                print(location)
                following = user.friends_count
                print(following)
                followers = user.followers_count
                print(followers)
                lasttweet = api.user_timeline(screen_name=frist_name)
                last_tweet = str(lasttweet[0].text).encode('unicode_escape')
                print(last_tweet)
                global retweet
                for pages in tweepy.Cursor(api.user_timeline, screen_name=frist_name, count=200).items(1):
                    retweet = pages.retweet_count
                TwitterInfo.objects.filter(username=frist_name).update(tweets_count=tweets_count,
                                                                       followers_count=followers,
                                                                       following_count=following, last_tweet=last_tweet,
                                                                       retweets_count=retweet,
                                                                       profile_name=profile_name,
                                                                       location=location)
            except:
                print("  ")
