import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from instapy import InstaPy
from instapy import smart_run
import schedule

class LoginPage:
    def __init__(self, browser):
        #self.get_session()
        self.browser = browser
        #self.browser.get('https://www.instagram.com/')

    def login(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        # Select the corresponding tag 
        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']" )
        # pass the credentials to log in
        username_input.send_keys(usuario)
        password_input.send_keys(contraseña)
        # Log in
        login_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)

    def get_session(self):
        session = InstaPy(username='username',
                      password='password')
                      #headless_browser=True,
                      #nogui=True,
                      #ulti_logs=False)

        return session

        # Definir unas tareas para comprobar la funcionalidad del bot
    def automate_task(self):
            # start session with Instapy
            #session = InstaPy(bypass_security_challenge_using='sms', disable_image_load=True) 
          
            session = self.get_session()
            with smart_run(session):
                session.set_do_comment(enabled=True, percentage=50)
                session.set_comments(['Aww!', 'bebittoooooooo', 'caramelooooo', 'firuuuulaiimor', 'mas lndo', 'rmoso', 'preciosiii', 'mamorr', 'bebe', 'ayyy xd', 'tierni', 'hermosuraaaa', 'que lindooo', 'se te come a besoss', 'besoss', 'besitoo', 'muaaak', 't amo'])
                session.set_do_follow(enabled=True, percentage=5, times=2)
                session.like_by_tags(['gatitos', 'gatitosbebes', 'gatitostiernos', 'gatitosfelices', 'gatitosnegros', 'perrosfelices','perrosalchicha', 'perrosfelicesdueñosfelices', 'perritolindo', 'perrofeliz', 'perroinfluencer', 'perrodeldia', 'perroloco' ], amount=100, media='Photo')
                session.like_by_locations(['c2727993', 'c87974', 'c83693', 'c87145', 'c89886', 'c89027', 'c88108', 'c88406', 'c84695', 'c85853', 'c90205'], amount=100, skip_top_posts=False, randomize=True)
                session.set_user_interact(amount=1, randomize=True, percentage=20, media='Photo')
                session.follow_user_followers(['santi_vegaok'], amount=10, randomize=False, sleep_delay=60)
                session.follow_user_following(['santi_vegaok', 'luciiacamiila'], amount=10, randomize=False, sleep_delay=60)
                # For 50% of the 30 newly followed, move to their profile
                # and randomly choose  pictures to be liked.
                session.set_user_interact(amount=1, randomize=True, percentage=50, media='Photo')

                session.follow_likers(['santi_vegaok' , 'luciiacamiila'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=6000, interact=False)
                session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=900*60*60, sleep_delay=501)

                session.set_do_reply_to_comments(enabled=True, percentage=14)
                session.set_comment_replies(replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊", u"😁😁😁", u"😂",  u"🎉",  u"😎", u"🤓🤓🤓🤓🤓", u"👏🏼😉"],
                                media=None)

                # watch story
                session.set_do_story(enabled=True, percentage = 70, simulate = True)

                # avoid those profiles
                session.set_skip_users(skip_private=True,
                        private_percentage=100,
                        skip_no_profile_pic=True,
                        no_profile_pic_percentage=100,
                        skip_business=True,
                        skip_non_business=False,
                        business_percentage=100,
                        #skip_business_categories=[],
                        #dont_skip_business_categories=[],
                        skip_bio_keyword=['onlyfans', 'cafecito', 'vendo contenido', 'cafeccito', 'only fans'],
                        mandatory_bio_keywords=[],
                        skip_public=False,
                        public_percentage=0)


            
                session.set_delimit_liking(enabled=True, max_likes=500, min_likes=20)
                session.set_delimit_commenting(enabled=True, comments_mandatory_words=['gatito', 'perro', 'gato', 'perrito', 'peludito', 'michi', 'cuatro patas', 'mi perro amor eterno ', 'firulais', 'firulai'], max_comments=15, min_comments=4)
                #session.set_delimit_commenting(ena, bled=True, )

                session.set_action_delays(enabled=True,
                            like=100,
                            comment=500,
                            follow=100,
                            unfollow=280,
                            story=10)



    def run_task(self):
            #session.login()
            schedule.every(10).seconds.do(self.automate_task)
            

            while True:
                schedule.run_pending()
                time.sleep(5) 
  

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element(By.TAG_NAME , "button")
        sleep(2)
        return LoginPage(self.browser)




def main():
    # open a browser
    browser = webdriver.Firefox()
    browser.implicitly_wait(15)

    #sesion = LoginPage()
    #sesion.login('username', 'password')
    #sesion.run_task()

    # load the home page and connect
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login('username', 'password')
    login_page.run_task()

    # close the browse
    browser.close()

if __name__ == '__main__':
    main()

