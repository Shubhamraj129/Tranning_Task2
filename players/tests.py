from django.core.exceptions import ObjectDoesNotExist
from .models import *
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status


class Test_class_setup(APITestCase):
    def setUp(self):
        """
            These are functions to be executed before (setUp) and after (tearDown) each unit test. These are very useful
             for fixtures.
        """
        """
            setup to test the User creation endpoint. In the method, we create a self. data containing
            all the data required to create a User and then make a POST request to the user/create endpoint with
             the payload.
        """
        user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', 'is_superuser': '1', 'state': 'maratxxehoner',
                "country": "Zimbadebwe", "username": "Adla12", "first_name": "fidrst",
                "last_name": "ladst_nam", "is_active": '1'}

        response = self.client.post(
            reverse('players:createuser'),
            user,
            format="json")
        self.client.login(username="Adla12", email="fgi2@gmail.com", password='see22W@')
        data = {'name': 'Alabama',
                'logo':
                    'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop',
                }
        self.response = self.client.post(
            reverse('players:team_list'), data, format="json")
        self.school = {'name': 'arin'}
        self.response = self.client.post(reverse('players:school_list'), self.school, format="json")
        self.position = {'pos': 'DAR'}
        self.response = self.client.post(reverse('players:position_list'), self.position, format="json")
        self.country = {'name': 'US'}
        self.response = self.client.post(reverse('players:country_list'), self.country, format="json")
        country_id = Country.objects.get(name='US')
        self.state = {'name': 'Moon', 'country': country_id.id}
        self.response = self.client.post(reverse('players:state_list'), self.state, format="json")
        state = State.objects.get(name='Moon')
        self.city = {'name': 'Pandharapur', 'state': state.id}
        self.response = self.client.post(reverse('players:city_list'), self.city, format="json")
        self.year = {'year': 2003}
        self.response = self.client.post(reverse('players:year_list'), self.year, format="json")
        teams = {
            'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Alabama', }
        sere = []
        for logo, name in teams.items():
            teamid = Team.objects.get(name=name)
            sere.append(teamid.id)
        offers_id = {'teams': sere}
        self.response = self.client.post(reverse('players:offer_list'), offers_id, format="json")
        position = Position.objects.get(pos='DAR')
        # offers_id = Offers.objects.get(pk=offers_id1.id)
        year = Year.objects.get(year=2003)
        city = City.objects.get(name='Pandharapur')
        school = HighSchool.objects.get(name='arin')
        offer = Offers.objects.get()
        self.player = {"first_name": "Corni", "last_name": "McCn11w", "height": "6.5", "weight": "162",
                       "image": "https://s3media.247sports.com/Uploads/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173",
                       "position": position.id, "year": year.id, 'school': school.id, 'city': city.id,
                       'offer': offer.id
                       }

        self.response = self.client.post(
            reverse('players:profile_list'),
            self.player,
            format="json")
        player_id = Prospect.objects.filter(last_name='McCn11w', first_name='Corni').first()
        team = Team.objects.filter(name='Alabama').first()
        self.data = {'commited': 'Commited', 'requited_by': 'Shubhamraj_lingade', 'team': team.id,
                     'player': player_id.id}
        self.response = self.client.post(
            reverse('players:commited_list'), self.data, format="json")
        self.twitter = {'username': '@shubhamraj', 'tweets_count': 562, 'followers_count': 1633, 'following_count': 123,
                        'last_tweet': 7546, 'retweets_count': 8930, 'profile_name': 'shubhamraj', 'location': 'pune',
                        'player_id': player_id.id}
        self.response = self.client.post(reverse('players:twitter_list'), self.twitter, format="json")


class Test_player_teams(Test_class_setup):

    def test_Create_team(self):
        """
            This check Create team Test
        """

        url = reverse('players:team_list')
        data = {'name': 'Rajaram',
                'logo': 'https://s3media.247sports.com/Uploads/Assets/592/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_team(self):
        """
            This Function test the Read the team data
        """
        team = Team.objects.get()
        response = self.client.get(
            reverse('players:team_detail',
                    kwargs={'pk': team.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_team(self):
        """
            This is team is updated
        """
        update_data = {"name": "Lion"}
        team = Team.objects.get()
        response = self.client.patch(
            reverse('players:team_detail',
                    kwargs={'pk': team.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_team(self):
        """
            This test Case Use  to Delete  team
        """
        team = Team.objects.get()
        response = self.client.delete(
            reverse('players:team_detail',
                    kwargs={'pk': team.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUser_login(Test_class_setup):

    def test_can_login_a_User(self):
        """
            This is used to log in Valid-user test
        """
        user = {'password': 'see22W@', 'email': 'fgi2@gmail.com', "username": "Adla12"}
        response = self.client.post(
            reverse('players:login_user'),
            user,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case_for_anonymous_user(self):
        """
             This is used to log in anonymous-user test
        """
        user = {"username": "reallied", "password": "332211", "email": "faugi2@gmail.com"}
        self.client.force_authenticate(user=None)
        response = self.client.post(
            reverse('players:login_user'), user
            ,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_try_login_invalid_User(self):
        """
            This test case for login user
        """
        user = {'password': 'hdgt@', 'email': 'fi2@gml.com', "username": "Adlad"}
        # self.client.force_authenticate(user=None)
        response = self.client.post(
            reverse('players:login_user'), user
            ,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class Test_school(Test_class_setup):

    def test_Create_school(self):
        url = reverse('players:school_list')
        data = {'name': 'Rajaram'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_school(self):
        """
            This Function test the Read the school data
        """
        school = HighSchool.objects.filter(name='arin').first()
        response = self.client.get(
            reverse('players:school_detail',
                    kwargs={'pk': school.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_school(self):
        """
            This is school is updated
        """
        update_data = {"name": "Lion"}
        school = HighSchool.objects.get()
        response = self.client.patch(
            reverse('players:school_detail',
                    kwargs={'pk': school.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_school(self):
        """
            This test Case Use  to Delete  school
        """
        user = HighSchool.objects.get()
        response = self.client.delete(
            reverse('players:school_detail',
                    kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_player_Position(Test_class_setup):

    def test_Create_position(self):
        url = reverse('players:position_list')
        data = {'pos': 'Raja'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_position(self):
        """
            This Function test the Read the position data
        """
        posit = Position.objects.filter(pos='DAR').first()
        response = self.client.get(
            reverse('players:position_detail',
                    kwargs={'pk': posit.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_position(self):
        """
            This is position is updated
        """
        update_data = {"pos": "Lion"}
        position = Position.objects.get()
        response = self.client.patch(
            reverse('players:position_detail',
                    kwargs={'pk': position.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_position(self):
        """
            This test Case Use  to Delete  position
        """
        posi = Position.objects.get()
        response = self.client.delete(
            reverse('players:position_detail',
                    kwargs={'pk': posi.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_country(Test_class_setup):
    def test_Create_country(self):
        url = reverse('players:country_list')
        data = {'name': 'MRGEDW'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_country(self):
        """
            This Function test the Read the country data
        """
        country = Country.objects.get()
        response = self.client.get(
            reverse('players:country_detail',
                    kwargs={'pk': country.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_country(self):
        """
            This is country is updated
        """
        update_data = {"name": "Lion"}
        country = Country.objects.get()
        response = self.client.patch(
            reverse('players:country_detail',
                    kwargs={'pk': country.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_country(self):
        """
            This test Case Use  to Delete  country
        """
        country = Country.objects.get()
        response = self.client.delete(
            reverse('players:country_detail',
                    kwargs={'pk': country.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_state(Test_class_setup):

    def test_Create_state(self):
        url = reverse('players:state_list')
        redw = Country.objects.get_or_create()
        country_id = Country.objects.get(name='US')
        data = {'name': 'MRGEDW', 'country': country_id.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_state(self):
        """
            This Function test the Read the state data
        """
        state = State.objects.get()
        response = self.client.get(
            reverse('players:state_detail',
                    kwargs={'pk': state.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_state(self):
        """
            This is state is updated
        """
        update_data = {"name": "Lion"}
        state = State.objects.get()
        response = self.client.patch(
            reverse('players:state_detail',
                    kwargs={'pk': state.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_state(self):
        """
            This test Case Use  to Delete  state
        """
        state = State.objects.get()
        response = self.client.delete(
            reverse('players:state_detail',
                    kwargs={'pk': state.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_City(Test_class_setup):

    def test_Create_city(self):
        url = reverse('players:city_list')
        redw = Country.objects.get_or_create()
        country_id = Country.objects.get(name='US')
        stateq = State.objects.create(name='maharashtra', country=country_id)
        state = State.objects.get(name='maharashtra')
        data = {'name': 'Supali', 'state': state.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_city(self):
        """
            This Function test the Read the city data
        """
        city = City.objects.get()
        response = self.client.get(
            reverse('players:city_detail',
                    kwargs={'pk': city.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_city(self):
        """
            This is city is updated
        """
        update_data = {"name": "Pune"}
        city = City.objects.get()
        response = self.client.patch(
            reverse('players:city_detail',
                    kwargs={'pk': city.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_city(self):
        """
            This test Case Use  to Delete  city
        """
        city = City.objects.get()
        response = self.client.delete(
            reverse('players:city_detail',
                    kwargs={'pk': city.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_Year(Test_class_setup):

    def test_Create_year(self):
        url = reverse('players:year_list')
        data = {'year': 2300}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_year(self):
        """
            This Function test the Read the Year data
        """
        year = Year.objects.get()
        response = self.client.get(
            reverse('players:year_detail',
                    kwargs={'pk': year.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_year(self):
        """
            This is Year is updated
        """
        update_data = {"year": 2025}
        year = Year.objects.get()
        response = self.client.patch(
            reverse('players:year_detail',
                    kwargs={'pk': year.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_year(self):
        """
            This test Case Use  to Delete  Year
        """
        year = Year.objects.get()
        response = self.client.delete(
            reverse('players:year_detail',
                    kwargs={'pk': year.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_offer(Test_class_setup):

    def test_Create_offer(self):
        teams = {
            'https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'NC State',
            'https://s3media.247sports.com/Uploads/Assets/602/120/8120602.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'North Carolina',
            'https://s3media.247sports.com/Uploads/Assets/540/76/11076540.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Old Dominion'}
        for logo, name in teams.items():
            try:
                teams1 = Team.objects.get(name=name)
            except ObjectDoesNotExist:
                teamss = Team(name=name, logo=logo)
                teamss.save()
        sere = []
        for logo, name in teams.items():
            teamid = Team.objects.get(name=name)
            sere.append(teamid.id)
        offers_id = {'teams': sere}
        self.response = self.client.post(
            reverse('players:offer_list'), offers_id, format="json")

    def test_retrive_offer(self):
        """
            This Function test the Read the offer data
        """
        offer = Offers.objects.get()
        response = self.client.get(
            reverse('players:offer_detail',
                    kwargs={'pk': offer.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_offer(self):
        """
            This is offer is updated
        """
        teams = {
            'https://s3media.247sports.com/Uploads/Assets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'NC State'}
        for logo, name in teams.items():
            try:
                teams1 = Team.objects.get(name=name)
            except ObjectDoesNotExist:
                teamss = Team(name=name, logo=logo)
                teamss.save()
        sere = []
        for logo, name in teams.items():
            teamid = Team.objects.get(name=name)
            sere.append(teamid.id)
        update_data = {"teams": sere}
        offer = Offers.objects.get()
        response = self.client.patch(
            reverse('players:offer_detail',
                    kwargs={'pk': offer.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_offer(self):
        """
            This test Case Use  to Delete  offer
        """
        offer = Offers.objects.get()
        response = self.client.delete(
            reverse('players:offer_detail',
                    kwargs={'pk': offer.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_case_Player(Test_class_setup):

    def test_Create_Player(self):
        url = reverse('players:profile_list')
        position = Position.objects.create(pos='dRF')
        teams = {
            'https://s3media.247sports.com/Uploads/Assets/592/649/4649592.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Alabama',
            'https://s3media.247sports.com/Uploads/Assets/201/648/4648201.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Miami',
            'https://s3media.247sports.com/Uploads/Assets/863/84/11084863.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Florida',
            'https://s3media.247sports.com/Uploads/Assets/672/698/9698672.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Arkansas',
            'https://s3media.247sports.com/Uploads/Assets/597/649/4649597.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'Auburn',
            'https://s3media.247sports.com/Uploads/Assets/528/682/4682528.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop': 'BYU'}
        offersid = Offers.objects.create()
        for logo, name in teams.items():
            try:
                friend = Team.objects.get(name=name)
            except ObjectDoesNotExist:
                friend = Team(name=name, logo=logo)
                friend.save()
        for logo, name in teams.items():
            teamid = Team.objects.get(name=name)
            offersid.teams.add(teamid)
        offers_id = Offers.objects.get(pk=offersid.id)
        year = Year.objects.create(year=2024)
        school = HighSchool.objects.create(name='shubham_lingade')
        country1 = Country.objects.get_or_create()
        country_id = Country.objects.get(name='US')
        state = State.objects.create(name='edear', country=country_id)
        state_id = State.objects.get(name='edear')
        city = City.objects.create(name='supali', state=state_id)
        data = {"first_name": "Corni22", "last_name": "McCn2111w", "height": "6.15", "weight": "1612",
                "image": "https://s3media.247sports.com/Uploads/Assets/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173",
                "position": position.id, "year": year.id, 'school': school.id, 'city': city.id, 'offer': offers_id.id
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_player(self):
        """
            This Function test the Read the player data
        """
        player = Prospect.objects.filter(last_name='McCn11w').first()
        response = self.client.get(
            reverse('players:profile_detail',
                    kwargs={'pk': player.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_player(self):
        """
            This is player is updated
        """
        update_data = {"first_name": "Lion", "last_name": "Hell", }
        user = Prospect.objects.get()
        response = self.client.patch(
            reverse('players:profile_detail',
                    kwargs={'pk': user.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_User(self):
        """
            This test Case Use  to Delete  player
        """
        user = Prospect.objects.get()
        response = self.client.delete(
            reverse('players:profile_detail',
                    kwargs={'pk': user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_commited(Test_class_setup):

    def test_Create_commited(self):
        self.player = {"first_name": "Corn", "last_name": "n11eww", "height": "6.24", "weight": "172",
                       "image": "https://s3media.247sports.com/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
        self.resp = self.client.post(
            reverse('players:profile_list'), self.player, format="json")

        player_id = Prospect.objects.filter(last_name='n11eww').first()

        createteam = Team.objects.create(name='Alama',
                                         logo='https://s3media.247sports.com/UAssets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
        createteam.save()
        team_id = Team.objects.get(name='Alama',
                                   logo='https://s3media.247sports.com/UAssets/728/975/7975728.png?fit=bounds&crop=50:50,offset-y0.50&width=50&height=50&fit=crop')
        data = {'commited': 'Commited', 'requited_by': 'Shubhamraj_lingade', 'team': team_id.id,
                'player': player_id.id}
        url = reverse('players:commited_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_commited(self):
        """
            This Function test the Read the commited data
        """
        commited = HardCommited.objects.get()
        response = self.client.get(
            reverse('players:commited_detail',
                    kwargs={'pk': commited.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_commited(self):
        """
            This  is commited commited
        """
        update_data = {"name": "Lion"}
        commited = HardCommited.objects.get()
        response = self.client.patch(
            reverse('players:commited_detail',
                    kwargs={'pk': commited.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_commited(self):
        """
            This test Case Use  to Delete commited
        """
        commited = HardCommited.objects.get()
        response = self.client.delete(
            reverse('players:commited_detail',
                    kwargs={'pk': commited.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class Test_Player_Twitter(Test_class_setup):
    def test_Create_twitter(self):
        self.player = {"first_name": "Corn", "last_name": "n11eww", "height": "6.24", "weight": "172",
                       "image": "https://s3media.247sports.com/225/280/11280225.jpg?fit=bounds&width=310&height=173&crop=310:173"}
        self.resp = self.client.post(
            reverse('players:profile_list'), self.player, format="json")

        player_id = Prospect.objects.filter(last_name='n11eww').first()
        data = {'username': '@shubhamraj', 'tweets_count': 562, 'followers_count': 1633, 'following_count': 123,
                'last_tweet': 7546, 'retweets_count': 8930, 'profile_name': 'shubhamraj', 'location': 'pune',
                'player_id': player_id.id}
        url = reverse('players:twitter_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_twitter(self):
        """
            This Function test the Read the twitter data
        """
        twitter = TwitterInfo.objects.get()
        response = self.client.get(
            reverse('players:twitter_detail',
                    kwargs={'pk': twitter.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_twitter(self):
        """
            This  is updated twitter
        """
        update_data = {'username': '@Bharat', 'tweets_count': 62, 'followers_count': 33, 'following_count': 23}
        twitter = TwitterInfo.objects.get()
        response = self.client.patch(
            reverse('players:twitter_detail',
                    kwargs={'pk': twitter.id}), update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_a_twitter(self):
        """
            This test Case Use  to Delete twitter
        """
        twitter = TwitterInfo.objects.get()
        response = self.client.delete(
            reverse('players:twitter_detail',
                    kwargs={'pk': twitter.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
