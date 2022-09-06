from selenium.webdriver.support import expected_conditions as EC
from players.models import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
from selenium.webdriver.common.by import By
import time
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand


# from Players.Player_Scrapping.models import Player


class Command(BaseCommand):

    def handle(self, *args, **options):
        for x in Prospect.objects.values('first_name', 'last_name', 'height', 'weight', 'image', 'city', 'school',
                                         'position', 'offer', 'year'):
            frist_name = x.get('first_name')
            last_name = x.get('last_name')
            height = x.get('height')
            weight = x.get('weight')
            image = x.get('image')
            city = x.get('city')
            city1 = City.objects.get(id=city)
            city_name = city1.name
            school = x.get('school')
            school = HighSchool.objects.get(id=school)
            school_name = school.name
            position = x.get('position')
            pos = Position.objects.get(id=position)
            position_name = pos.pos
            offer = x.get('offer')
            year_id = x.get('year')
            years = Year.objects.get(id=year_id)
            year = years.year
            print(frist_name, last_name, height, weight, image, city_name, school_name, position_name, offer, year)
            if year == 2022:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.maximize_window()
                driver.get("https://247sports.com/Season/2022-Football/Recruits/")
            else:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.maximize_window()
                driver.get("https://247sports.com/Season/2023-Football/Recruits/")
            fnameplayer = driver.find_element(By.XPATH, "//section/form/input[@ name='name']")
            fnameplayer.send_keys(frist_name, " ", last_name)
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '/html/body/section[1]/section/div/section[2]/section/section/section/div/section[1]/form/button').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//ul[@class="results "]/li/ul/li[2]/a').click()
            time.sleep(3)
            try:
                teamslist = driver.find_element(By.XPATH, '//a[@class="view-profile-link"]')
                teamslist.click()
                time.sleep(2)
            except (NoSuchElementException, NoSuchFrameException):
                time.sleep(2)
            commits = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='college-comp__view-all']")))
            commits.click()
            time.sleep(2)
            current_scroll_position, new_height = 0, 1
            speed = 3
            while current_scroll_position <= new_height:
                current_scroll_position += speed
                driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
                new_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            offers = driver.find_elements(By.XPATH, "//span[@class='offer']")
            commitslogo = driver.find_elements(By.XPATH, "//ul[@class='recruit-interest-index_lst']/li/img")
            commitname = driver.find_elements(By.XPATH, "//ul[@class='recruit-interest-index_lst']/li/div/div/a[1]")
            time.sleep(1)
            locallinks = []
            localclub = []
            clublogolink = []
            clubname = []
            my_string1 = []
            for i in offers:
                das = i.text
                my_string1.append(das)
            for logolink in commitslogo:
                locallinks.append(logolink.get_attribute("src"))
                length = len(locallinks)
                if 'Offer:\nYes' in my_string1[length - 1]:
                    clublogolink.append(logolink.get_attribute("src"))
            for teamname in commitname:
                localclub.append(teamname.text)
                length = len(localclub)
                if 'Offer:\nYes' in my_string1[length - 1]:
                    clubname.append(teamname.text)
            dictionary = dict(zip(clublogolink, clubname))
            print(dictionary)
            ofreerid= Offers.objects.get(pk=offer)
            for logo, name in dictionary.items():
                try:
                    team = Team.objects.get(name=name)
                except ObjectDoesNotExist:
                    team = Team(name=name, logo=logo)
                    team.save()
            for logo, name in dictionary.items():
                teamid = Team.objects.get(name=name)

            driver.back()
            time.sleep(3)
            nameplayer = driver.find_element(By.XPATH,
                                             "/html/body/section[1]/section/div/section/header/div[1]/h1").text
            print("player_Name:", nameplayer)

            pos = driver.find_element(By.XPATH, "//ul[@class='metrics-list']/li[1]/span[2]").text
            print("Pos :", pos)
            try:
                posi = Position.objects.get(pos=pos)
            except ObjectDoesNotExist:
                friend = Position(pos=pos)
                friend.save()
            position_id = Position.objects.get(pos=pos)
            Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(position=position_id)
            height1 = driver.find_element(By.XPATH,
                                          "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[2]/span[2]").text
            print(height1)
            Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(height=height1)
            weight = driver.find_element(By.XPATH,
                                         "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[3]/span[2]").text
            print(weight)
            Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(weight=weight)
            try:
                highschool = driver.find_element(By.XPATH, '//ul[@class="details "]/li[1]/span[2]').text
                print("Highschool :", highschool)
                try:
                    school = HighSchool.objects.get(name=highschool)
                except ObjectDoesNotExist:
                    friend = HighSchool(name=highschool)
                    friend.save()
                highSchool_id = HighSchool.objects.get(name=highschool)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(school=highSchool_id)
                city = driver.find_element(By.XPATH, "//ul[@class='details ']/li[2]/span[2]").text
                print("city :", city)
                country_id = Country.objects.get(name='US')
                csvalue = city.split(',')
                state = (csvalue[1])
                statename = State.objects.get_or_create(name=state, country=country_id)
                city = (csvalue[0])
                state_id = State.objects.get(name=state)
                cityname = City.objects.get_or_create(name=city, state=state_id)
                city_id = City.objects.get(name=city, state=state_id)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(city=city_id)
                classname = driver.find_element(By.XPATH, "//ul[@class='details ']/li[3]/span[2]").text
                print("Classname ::", classname)
                try:
                    years = Year.objects.get(year=classname)
                except ObjectDoesNotExist:
                    friend = Year(year=classname)
                    friend.save()
                class_id = Year.objects.get(year=classname)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(year=class_id)
            except NoSuchElementException:
                highschool = driver.find_element(By.XPATH,
                                                 '//ul[@class="details is-juco"]/li[@class="juco"]/div/span[2]').text
                print("Highschool :", highschool)
                try:
                    school = HighSchool.objects.get(name=highschool)
                except ObjectDoesNotExist:
                    friend = HighSchool(name=highschool)
                    friend.save()
                highSchool_id = HighSchool.objects.get(name=highschool)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(school=highSchool_id)
                city = driver.find_element(By.XPATH, '//ul[@class="details is-juco"]/li[2]/span[2]').text
                print("city :", city)
                country_id = Country.objects.get(name='US')
                csvalue = city.split(',')
                state = (csvalue[1])
                statename = State.objects.get_or_create(name=state, country=country_id)
                city = (csvalue[0])
                state_id = State.objects.get(name=state)
                cityname = City.objects.get_or_create(name=city, state=state_id)
                # print(city)
                city_id = City.objects.get(name=city, state=state_id)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(city=city_id)
                classname = driver.find_element(By.XPATH, '//ul[@class="details is-juco"]/li[3]/span[2]').text
                print("Classname ::", classname)
                try:
                    years = Year.objects.get(year=classname)
                except ObjectDoesNotExist:
                    year1 = Year(year=classname)
                    year1.save()
                class_id = Year.objects.get(year=classname)
                Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(year=class_id)

            imagesrc = driver.find_element(By.XPATH, "//img[@class='jsonly']").get_attribute("src")
            print("image link", imagesrc)
            Prospect.objects.filter(first_name=frist_name, last_name=last_name).update(image=imagesrc)
            player_id = Prospect.objects.get(first_name=frist_name, last_name=last_name, image=imagesrc)

            try:
                commited = driver.find_element(By.XPATH,
                                               '//span[@class="college-comp__interest-level college-comp__interest-level--committed-bg"]').text
                print(commited)
                requritedby = driver.find_elements(By.XPATH,
                                                   "/html/body/section[1]/section/div/section/section/div/ul/li[1]/div[3]/div/a")
                requirted = []
                for requir in requritedby:
                    print(requir.text)
                    requirted.append(requir.text)
                commitedcollage = driver.find_element(By.XPATH,
                                                      "/html/body/section[1]/section/div/section/section/div/ul/li[1]/div[1]/a[1]").text
                print(commitedcollage)
                team_id = Team.objects.get(name=commitedcollage)
                HardCommited.objects.filter(player=player_id).update_or_create(commited=commited, requited_by=requirted,
                                                                               team=team_id)
            except NoSuchElementException:
                print(" ")
            driver.execute_script("window.scrollTo(0, 1500);")
            time.sleep(2)
            try:
                driver.switch_to.frame('twitter-widget-0')
                twitter = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/a/div/a/span"))).text
                value = twitter.split('@')
                twittername = ("@" + value[1])
                print("Account_Name", twittername)
            except (NoSuchElementException, NoSuchFrameException):
                try:
                    time.sleep(1)
                    twitter = driver.find_element(By.XPATH, "//span[@class='timeline-Header-byline']/a").text
                    print("Account Name:", twitter)
                    TwitterInfo.objects.filter(player_id=player_id).update_or_create(username=twitter)
                except (NoSuchElementException, NoSuchFrameException):
                    try:
                        exement = TwitterInfo.objects.filter(player_id=player_id)
                        TwitterInfo.objects.filter(player_id=player_id).update_or_create(username=' ')
                    except ObjectDoesNotExist:
                        print(" No Account")
            driver.close()
