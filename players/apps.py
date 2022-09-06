from django.apps import AppConfig


class PlayersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'players'
#
#
# class Test_Player_offer(APITestCase):
#     def setUp(self):
#
#         data = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "last_nam"}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             data,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         teams = {
#             'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Alabama',
#             'https://s3media.247sports.com/Uploads/Assets/201/648/4648201.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Miami',
#             'https://s3media.247sports.com/Uploads/Assets/863/84/11084863.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Florida',
#             'https://s3media.247sports.com/Uploads/Assets/672/698/9698672.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Arkansas',
#             'https://s3media.247sports.com/Uploads/Assets/597/649/4649597.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Auburn',
#             'https://s3media.247sports.com/Uploads/Assets/528/682/4682528.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'BYU'}
#         for logo, name in teams.items():
#             try:
#                 friend = Team.objects.get(name=name)
#             except ObjectDoesNotExist:
#                 friend = Team(name=name, logo=logo)
#                 friend.save()
#         sere = []
#         for logo, name in teams.items():
#             teamid = Team.objects.get(name=name)
#             sere.append(teamid.id)
#         offers_id = {'teams': sere}
#         # offers_id = Offers.objects.get(pk=self.data.id)
#         self.response = self.client.post(
#             reverse('players:offer_list'), offers_id,
#             # self.data.id,
#             format="json")
#         print(self.response.data)
#
#     # def test_Create_year(self):
#     #     url = reverse('players:offer_list')
#     #     data = {'year': 2300}
#     #     response = self.client.post(url, data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_offer(self):
#         """
#             This Function test the Read the user data
#         """
#         year = Offers.objects.get()
#         response = self.client.get(
#             reverse('players:offer_detail',
#                     kwargs={'pk': year.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_offer(self):
#         """
#             This is player is updated
#         """
#         update_data = {"teams": " "}
#         year = Offers.objects.get()
#         print(year)
#         response = self.client.patch(
#             reverse('players:offer_detail',
#                     kwargs={'pk': year.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_offer(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         year = Offers.objects.get()
#         response = self.client.delete(
#             reverse('players:offer_detail',
#                     kwargs={'pk': year.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# try:
#     auth = tweepy.OAuthHandler(api_key, api_secrets)
#     auth.set_access_token(access_token, access_secret)
#     api = tweepy.API(auth)
#     api.verify_credentials()
#     print('Successful Authentication')
# except:
#     print('Failed authentication')


# for i in range(1625, 1626):
#     names = TwitterInfo.objects.get(id=i)
#     a = names.username
#     print(a)
#     cursor = tweepy.Cursor(api.user_timeline, id=a, tweet_mode="extended").items(1)
#     for j in cursor:
#         retweet_count = j.retweet_count
#     k = a
#     cursor1 = tweepy.Cursor(api.user_timeline, screen_name=frist_name, tweet_mode="extended", count=200,).items(1)
#             for j in cursor1:
#                 retweet_count = j.retweet_count
#                 print(retweet_count)

