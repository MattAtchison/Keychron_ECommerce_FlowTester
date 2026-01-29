from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# calling in the manual input definition from manual_input.py
from manual_input import manual_input

EMAIL = 'test_user@gmail.com'
PASSWORD = 'Test_User_Password'


class EcommerceTesting:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)   # store on self



    def clicking_custom_keyboard(self, url):
        self.driver.get(url)

        custom_keyboards_link = self.wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.card-link[href*='custom-keyboards']")
            )
        )
        custom_keyboards_link.click()

    def adding_product_to_cart(self):

        # testing the carousel, clicking it three times
        for n in range(3):
            slider = self.wait.until(
                ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[name=next]')
                )
            )


            slider.click()

        # actually clicking on the product to go to the landing page

        product = self.wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'a.js-prod-link'))
        )

        self.driver.execute_script("arguments[0].click();", product)


        # clicking the actual add to cart link
        add_to_cart = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[name=add]')
        ))

        add_to_cart.click()


        # when prompted to go the cart click
        checkout = self.wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[name=checkout]')
            )
        )

        checkout.click()

    def signing_in(self):
        print('Using automated email/password login')

        sign_in = self.wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href*='customer_authentication/login']")
            )
        )

        sign_in.click()

        email_input = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']"))
        )
        password_input = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
        )

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)

        submit = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit.click()


    def manual_login(self):
        print('Using manual login')
        manual_input(self.driver, self.wait)


    def login(self, mode='manual'):
        if mode == 'manual':
            self.manual_login()

        elif mode == 'auto':
            self.signing_in()




    def quit(self):
        self.driver.quit()




def main():
    bot = EcommerceTesting()
    bot.clicking_custom_keyboard("https://www.keychron.com/?mai_source=google&mai_medium=paid&mai_campaign=19623609308&mai_adgroup=142470448021&mai_term=keychron&mai_content={adid}&mai_click_id=Cj0KCQiAx8PKBhD1ARIsAKsmGbcYTrDT9R4USZlGvtmbR72L0d7WMRGUMSVBKCQ2wJPhwwqcoUdy7cgaAsXgEALw_wcB&tw_source=google&tw_adid=646395086831&tw_campaign=19623609308&tw_kwdid=aud-1391923251796:kwd-754557381071&gad_source=1&gad_campaignid=19623609308&gbraid=0AAAAABen0Lc8p2UsFYO5j6qSYOdHqXxGR&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbcYTrDT9R4USZlGvtmbR72L0d7WMRGUMSVBKCQ2wJPhwwqcoUdy7cgaAsXgEALw_wcB")
    bot.adding_product_to_cart()

    # choosing login style here
    bot.login(mode='manual')
    
    bot.quit()


if __name__ == '__main__':
    main()