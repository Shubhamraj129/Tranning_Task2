from django.apps import AppConfig


class PlayersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'players'

# class Test_school(APITestCase):
#     # @classmethod
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.data = {'name': 'arin'}
#         self.response = self.client.post(
#             reverse('players:school_list'),
#             self.data,
#             format="json")
#
#     def test_Create_school(self):
#         url = reverse('players:school_list')
#         data = {'name': 'Rajaram'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_school(self):
#         """
#             This Function test the Read the user data
#         """
#         school = HighSchool.objects.filter(name='arin').first()
#         response = self.client.get(
#             reverse('players:school_detail',
#                     kwargs={'pk': school.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_school(self):
#         """
#             This is player is updated
#         """
#         update_data = {"name": "Lion"}
#         school = HighSchool.objects.get()
#         response = self.client.patch(
#             reverse('players:school_detail',
#                     kwargs={'pk': school.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_school(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         user = HighSchool.objects.get()
#         response = self.client.delete(
#             reverse('players:school_detail',
#                     kwargs={'pk': user.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_player_Position(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.data = {'pos': 'DLAR'}
#         self.response = self.client.post(
#             reverse('players:position_list'),
#             self.data,
#             format="json")
#
#     def test_Create_position(self):
#         url = reverse('players:position_list')
#         data = {'pos': 'Raja'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_position(self):
#         """
#             This Function test the Read the user data
#         """
#         posit = Position.objects.filter(pos='DLAR').first()
#         response = self.client.get(
#             reverse('players:position_detail',
#                     kwargs={'pk': posit.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_position(self):
#         """
#             This is player is updated
#         """
#         update_data = {"pos": "Lion"}
#         position = Position.objects.get()
#         response = self.client.patch(
#             reverse('players:position_detail',
#                     kwargs={'pk': position.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_position(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         posi = Position.objects.get()
#         response = self.client.delete(
#             reverse('players:position_detail',
#                     kwargs={'pk': posi.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_player_team(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.data = {'name': 'arin',
#                      'logo': 'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop'}
#         self.response = self.client.post(
#             reverse('players:team_list'),
#             self.data,
#             format="json")
#
#     def test_Create_team(self):
#         url = reverse('players:team_list')
#         data = {'name': 'Rajaram',
#                 'logo': 'https://s3media.247sports.com/Uploads/Assets/592/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_team(self):
#         """
#             This Function test the Read the user data
#         """
#         team = Team.objects.filter(name='arin').first()
#         response = self.client.get(
#             reverse('players:team_detail',
#                     kwargs={'pk': team.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_team(self):
#         """
#             This is player is updated
#         """
#         update_data = {"name": "Lion"}
#         team = Team.objects.get()
#         response = self.client.patch(
#             reverse('players:team_detail',
#                     kwargs={'pk': team.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_team(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         team = Team.objects.get()
#         response = self.client.delete(
#             reverse('players:team_detail',
#                     kwargs={'pk': team.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_country(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.data = {'name': 'US'}
#         self.response = self.client.post(
#             reverse('players:country_list'),
#             self.data,
#             format="json")
#
#     def test_Create_country(self):
#         url = reverse('players:country_list')
#         data = {'name': 'MRGEDW'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_country(self):
#         """
#             This Function test the Read the user data
#         """
#         country = Country.objects.get()
#         response = self.client.get(
#             reverse('players:country_detail',
#                     kwargs={'pk': country.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_country(self):
#         """
#             This is player is updated
#         """
#         update_data = {"name": "Lion"}
#         country = Country.objects.get()
#         response = self.client.patch(
#             reverse('players:country_detail',
#                     kwargs={'pk': country.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_country(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         country = Country.objects.get()
#         response = self.client.delete(
#             reverse('players:country_detail',
#                     kwargs={'pk': country.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_state(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         redw = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         self.data = {'name': 'Moon', 'country': country_id.id}
#         self.response = self.client.post(
#             reverse('players:state_list'),
#             self.data,
#             format="json")
#
#     def test_Create_state(self):
#         url = reverse('players:state_list')
#         redw = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         data = {'name': 'MRGEDW', 'country': country_id.id}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_state(self):
#         """
#             This Function test the Read the user data
#         """
#         state = State.objects.get()
#         response = self.client.get(
#             reverse('players:state_detail',
#                     kwargs={'pk': state.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_state(self):
#         """
#             This is player is updated
#         """
#         update_data = {"name": "Lion"}
#         state = State.objects.get()
#         response = self.client.patch(
#             reverse('players:state_detail',
#                     kwargs={'pk': state.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_state(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         state = State.objects.get()
#         response = self.client.delete(
#             reverse('players:state_detail',
#                     kwargs={'pk': state.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_City(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         redw = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         stateq = State.objects.create(name='PUN', country=country_id)
#         state = State.objects.get(name='PUN')
#         self.data = {'name': 'Pandharapur', 'state': state.id}
#         self.response = self.client.post(
#             reverse('players:city_list'),
#             self.data,
#             format="json")
#
#     def test_Create_city(self):
#         url = reverse('players:city_list')
#         redw = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         stateq = State.objects.create(name='maharashtra', country=country_id)
#         state = State.objects.get(name='maharashtra')
#         data = {'name': 'Supali', 'state': state.id}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_city(self):
#         """
#             This Function test the Read the user data
#         """
#         city = City.objects.get()
#         response = self.client.get(
#             reverse('players:city_detail',
#                     kwargs={'pk': city.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_city(self):
#         """
#             This is player is updated
#         """
#         update_data = {"name": "Lion"}
#         city = City.objects.get()
#         response = self.client.patch(
#             reverse('players:city_detail',
#                     kwargs={'pk': city.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_city(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         city = City.objects.get()
#         response = self.client.delete(
#             reverse('players:city_detail',
#                     kwargs={'pk': city.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_Year(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.data = {'year': 2003}
#         self.response = self.client.post(
#             reverse('players:year_list'),
#             self.data,
#             format="json")
#
#     def test_Create_year(self):
#         url = reverse('players:year_list')
#         data = {'year': 2300}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_year(self):
#         """
#             This Function test the Read the user data
#         """
#         year = Year.objects.get()
#         response = self.client.get(
#             reverse('players:year_detail',
#                     kwargs={'pk': year.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_year(self):
#         """
#             This is player is updated
#         """
#         update_data = {"year": 2025}
#         year = Year.objects.get()
#         response = self.client.patch(
#             reverse('players:year_detail',
#                     kwargs={'pk': year.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_year(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         year = Year.objects.get()
#         response = self.client.delete(
#             reverse('players:year_detail',
#                     kwargs={'pk': year.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_offer(APITestCase):
#     def setUp(self):
#
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "last_nam"}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
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
#         self.response = self.client.post(
#             reverse('players:offer_list'), offers_id,
#             format="json")
#
#     def test_Create_offer(self):
#         teams = {
#             'https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'NC State',
#             'https://s3media.247sports.com/Uploads/Assets/602/120/8120602.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'North Carolina',
#             'https://s3media.247sports.com/Uploads/Assets/540/76/11076540.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Old Dominion'}
#         for logo, name in teams.items():
#             try:
#                 teams1 = Team.objects.get(name=name)
#             except ObjectDoesNotExist:
#                 teamss = Team(name=name, logo=logo)
#                 teamss.save()
#         sere = []
#         for logo, name in teams.items():
#             teamid = Team.objects.get(name=name)
#             sere.append(teamid.id)
#         offers_id = {'teams': sere}
#         self.response = self.client.post(
#             reverse('players:offer_list'), offers_id,
#             # self.data.id,
#             format="json")
#
#     def test_retrive_offer(self):
#         """
#             This Function test the Read the user data
#         """
#         offer = Offers.objects.get()
#         response = self.client.get(
#             reverse('players:offer_detail',
#                     kwargs={'pk': offer.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_offer(self):
#         """
#             This is player is updated
#         """
#         teams = {
#             'https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'NC State'}
#         for logo, name in teams.items():
#             try:
#                 teams1 = Team.objects.get(name=name)
#             except ObjectDoesNotExist:
#                 teamss = Team(name=name, logo=logo)
#                 teamss.save()
#         sere = []
#         for logo, name in teams.items():
#             teamid = Team.objects.get(name=name)
#             sere.append(teamid.id)
#         update_data = {"teams": sere}
#         offer = Offers.objects.get()
#         response = self.client.patch(
#             reverse('players:offer_detail',
#                     kwargs={'pk': offer.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_offer(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         offer = Offers.objects.get()
#         response = self.client.delete(
#             reverse('players:offer_detail',
#                     kwargs={'pk': offer.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_commited(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.player = {"first_name": "Cor", "last_name": "n11w", "height": "6.54", "weight": "262",
#                        "image": "https://s3media.247sports.com/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
#         self.resp = self.client.post(
#             reverse('players:profile_list'), self.player, format="json")
#
#         player_id = Prospect.objects.filter(last_name='n11w').first()
#
#         createteam = Team.objects.create(name='Alabama',
#                                          logo='https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
#         createteam.save()
#         team_id = Team.objects.get(name='Alabama',
#                                    logo='https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
#         self.data = {'commited': 'Commited', 'requited_by': 'Shubhamraj_lingade', 'team': team_id.id,
#                      'player': player_id.id}
#         self.response = self.client.post(
#             reverse('players:commited_list'),
#             self.data,
#             format="json")
#
#     def test_Create_commited(self):
#         self.player = {"first_name": "Corn", "last_name": "n11eww", "height": "6.24", "weight": "172",
#                        "image": "https://s3media.247sports.com/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
#         self.resp = self.client.post(
#             reverse('players:profile_list'), self.player, format="json")
#
#         player_id = Prospect.objects.filter(last_name='n11w').first()
#
#         createteam = Team.objects.create(name='Alama',
#                                          logo='https://s3media.247sports.com/UAssets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
#         createteam.save()
#         team_id = Team.objects.get(name='Alama',
#                                    logo='https://s3media.247sports.com/UAssets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
#         data = {'commited': 'Commited', 'requited_by': 'Shubhamraj_lingade', 'team': team_id.id,
#                 'player': player_id.id}
#         url = reverse('players:commited_list')
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_commited(self):
#         """
#             This Function test the Read the user data
#         """
#         commited = HardCommited.objects.get()
#         response = self.client.get(
#             reverse('players:commited_detail',
#                     kwargs={'pk': commited.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_commited(self):
#         """
#             This  is updated commited
#         """
#         update_data = {"name": "Lion"}
#         commited = HardCommited.objects.get()
#         response = self.client.patch(
#             reverse('players:commited_detail',
#                     kwargs={'pk': commited.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_commited(self):
#         """
#             This test Case Use  to Delete
#         """
#         commited = HardCommited.objects.get()
#         response = self.client.delete(
#             reverse('players:commited_detail',
#                     kwargs={'pk': commited.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_Player_Twitter(APITestCase):
#     def setUp(self):
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         self.player = {"first_name": "Cor", "last_name": "n11w", "height": "6.54", "weight": "262",
#                        "image": "https://s3media.247sports.com/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
#         self.resp = self.client.post(
#             reverse('players:profile_list'), self.player, format="json")
#
#         player_id = Prospect.objects.filter(last_name='n11w').first()
#
#         self.data = {'username': '@shubhamraj', 'tweets_count': 562, 'followers_count': 1633, 'following_count': 123,
#                      'last_tweet': 7546, 'retweets_count': 8930, 'profile_name': 'shubhamraj', 'location': 'pune',
#                      'player_id': player_id.id}
#         self.response = self.client.post(
#             reverse('players:twitter_list'),
#             self.data,
#             format="json")
#
#     def test_Create_twitter(self):
#         self.player = {"first_name": "Corn", "last_name": "n11eww", "height": "6.24", "weight": "172",
#                        "image": "https://s3media.247sports.com/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
#         self.resp = self.client.post(
#             reverse('players:profile_list'), self.player, format="json")
#
#         player_id = Prospect.objects.filter(last_name='n11w').first()
#         data = {'username': '@shubhamraj', 'tweets_count': 562, 'followers_count': 1633, 'following_count': 123,
#                 'last_tweet': 7546, 'retweets_count': 8930, 'profile_name': 'shubhamraj', 'location': 'pune',
#                 'player_id': player_id.id}
#         url = reverse('players:twitter_list')
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_twitter(self):
#         """
#             This Function test the Read the twitter data
#         """
#         twitter = TwitterInfo.objects.get()
#         response = self.client.get(
#             reverse('players:twitter_detail',
#                     kwargs={'pk': twitter.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_twitter(self):
#         """
#             This  is updated twitter
#         """
#         update_data = {'username': '@Bharat', 'tweets_count': 62, 'followers_count': 33, 'following_count': 23}
#         twitter = TwitterInfo.objects.get()
#         response = self.client.patch(
#             reverse('players:twitter_detail',
#                     kwargs={'pk': twitter.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_twitter(self):
#         """
#             This test Case Use  to Delete
#         """
#         twitter = TwitterInfo.objects.get()
#         response = self.client.delete(
#             reverse('players:twitter_detail',
#                     kwargs={'pk': twitter.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class Test_case_Player(APITestCase):
#     def setUp(self):
#
#         user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
#                 "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#         self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
#         position = Position.objects.create(pos='dRF')
#         teams = {
#             'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Alabama',
#             'https://s3media.247sports.com/Uploads/Assets/201/648/4648201.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Miami',
#             'https://s3media.247sports.com/Uploads/Assets/863/84/11084863.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Florida',
#             'https://s3media.247sports.com/Uploads/Assets/672/698/9698672.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Arkansas',
#             'https://s3media.247sports.com/Uploads/Assets/597/649/4649597.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Auburn',
#             'https://s3media.247sports.com/Uploads/Assets/528/682/4682528.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'BYU'}
#         offersid = Offers.objects.create()
#         for logo, name in teams.items():
#             try:
#                 friend = Team.objects.get(name=name)
#             except ObjectDoesNotExist:
#                 friend = Team(name=name, logo=logo)
#                 friend.save()
#         for logo, name in teams.items():
#             teamid = Team.objects.get(name=name)
#             offersid.teams.add(teamid)
#         offers_id = Offers.objects.get(pk=offersid.id)
#         year = Year.objects.create(year=2024)
#         school = HighSchool.objects.create(name='shubham_lingade')
#         country1 = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         state = State.objects.create(name='eder', country=country_id)
#         state_id = State.objects.get(name='eder')
#         city = City.objects.create(name='supali', state=state_id)
#         self.data = {"first_name": "Corni", "last_name": "McCn11w", "height": "6.5", "weight": "162",
#                      "image": "https://s3media.247sports.com/Uploads/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173",
#                      "position": position.id, "year": year.id, 'school': school.id, 'city': city.id,
#                      'offer': offers_id.id
#                      }
#
#         self.response = self.client.post(
#             reverse('players:profile_list'),
#             self.data,
#             format="json")
#
#     def test_Create_User(self):
#         url = reverse('players:createuser')
#         data = {'password': '123333S@', 'email': 'faugi2@gmail.com', 'is_superuser': '1', 'state': 'marathoner',
#                 "country": "Zimbabwe", "username": "Ala12", "first_name": "first",
#                 "last_name": "last_nam", "is_active": '1'}
#         self.client = APIClient()
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_Create_Player(self):
#         url = reverse('players:profile_list')
#         position = Position.objects.create(pos='dRF')
#         teams = {
#             'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Alabama',
#             'https://s3media.247sports.com/Uploads/Assets/201/648/4648201.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Miami',
#             'https://s3media.247sports.com/Uploads/Assets/863/84/11084863.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Florida',
#             'https://s3media.247sports.com/Uploads/Assets/672/698/9698672.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Arkansas',
#             'https://s3media.247sports.com/Uploads/Assets/597/649/4649597.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Auburn',
#             'https://s3media.247sports.com/Uploads/Assets/528/682/4682528.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'BYU'}
#         offersid = Offers.objects.create()
#         for logo, name in teams.items():
#             try:
#                 friend = Team.objects.get(name=name)
#             except ObjectDoesNotExist:
#                 friend = Team(name=name, logo=logo)
#                 friend.save()
#         for logo, name in teams.items():
#             teamid = Team.objects.get(name=name)
#             offersid.teams.add(teamid)
#         offers_id = Offers.objects.get(pk=offersid.id)
#         year = Year.objects.create(year=2024)
#         school = HighSchool.objects.create(name='shubham_lingade')
#         country1 = Country.objects.get_or_create()
#         country_id = Country.objects.get(name='US')
#         state = State.objects.create(name='edear', country=country_id)
#         state_id = State.objects.get(name='edear')
#         city = City.objects.create(name='supali', state=state_id)
#         data = {"first_name": "Corni22", "last_name": "McCn2111w", "height": "6.15", "weight": "1612",
#                 "image": "https://s3media.247sports.com/Uploads/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173",
#                 "position": position.id, "year": year.id, 'school': school.id, 'city': city.id, 'offer': offers_id.id
#                 }
#
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_retrive_player(self):
#         """
#             This Function test the Read the user data
#         """
#         player = Prospect.objects.filter(last_name='McCn11w').first()
#         response = self.client.get(
#             reverse('players:profile_detail',
#                     kwargs={'pk': player.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_update_a_player(self):
#         """
#             This is player is updated
#         """
#         update_data = {"first_name": "Lion", "last_name": "Hell", }
#         user = Prospect.objects.get()
#         response = self.client.patch(
#             reverse('players:profile_detail',
#                     kwargs={'pk': user.id}), update_data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_can_delete_a_User(self):
#         """
#             This test Case Use  to Delete  user
#         """
#         user = Prospect.objects.get()
#         response = self.client.delete(
#             reverse('players:profile_detail',
#                     kwargs={'pk': user.id}), format="json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class TestUser_login(APITestCase):
#
#     def setUp(self):
#         user = {'password': 'hgt@', 'email': 'fi2@gmail.com', 'is_superuser': '1', 'state': 'mxxehoner',
#                 "country": "Zimbad", "username": "Adlad", "first_name": "fit",
#                 "last_name": "ladst_nam", "is_active": '1'}
#
#         response = self.client.post(
#             reverse('players:createuser'),
#             user,
#             format="json")
#
#     def test_can_login_a_User(self):
#         """
#             This is used to log in Valid-user test
#         """
#         user = {'password': 'hgt@', 'email': 'fi2@gmail.com', "username": "Adlad"}
#         response = self.client.post(
#             reverse('players:login_user'),
#             user,
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_case_for_anonymous_user(self):
#         """
#              This is used to log in inValid-user test
#         """
#         user = {"username": "reallied", "password": "332211", "email": "faugi2@gmail.com"}
#         self.client.force_authenticate(user=None)
#         response = self.client.post(
#             reverse('players:login_user'), user
#             ,
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_can_try_login_invalid_User(self):
#         """
#             This test case for login user
#         """
#         user = {'password': 'hdgt@', 'email': 'fi2@gml.com', "username": "Adlad"}
#         # self.client.force_authenticate(user=None)
#         response = self.client.post(
#             reverse('players:login_user'), user
#             ,
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#

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

