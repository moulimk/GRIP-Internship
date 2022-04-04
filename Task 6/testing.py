import time
import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service("C:/Users/mouli/Documents/Selenium/Driver/msedgedriver.exe"))
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
    def test_Home_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # check the title
        self.assertIn("The Sparks Foundation", driver.title)
        print("Title checked\n")

        # check Navbar
        navbar = driver.find_element(By.TAG_NAME, "nav")
        if navbar.is_displayed():
            print("Navbar is displayed\n")

        # Check if logo is displayed
        logo = driver.find_element(By.CSS_SELECTOR, "a.col-md-6 > img:nth-child(1)")
        if logo.is_displayed():
            print("Logo is displayed\n")

        time.sleep(2)
        print("Home Page tested\n")
        print("-----------------------------------------\n")

    def test_About_Us_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # get about us dropdown on main page
        about_us_dropdown = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[1]/a')
        # get Advisors And Patrons element
        a_and_d = driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[1]/ul/li[3]/a')

        # performing chain actions
        action = ActionChains(driver)
        action.move_to_element(about_us_dropdown).click().move_to_element(a_and_d).click().perform()

        # slowly scroll down the page
        y = 250
        for timer in range(0, 5):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 250
            time.sleep(1)
        time.sleep(1)
        go_to_top = driver.find_element(By.XPATH, '//*[@id="toTop"]')
        go_to_top.click()
        time.sleep(2)
        print("About Us(Advisors And Patrons) page tested\n")
        print("-----------------------------------------\n")


    def test_Join_Us_Page(self):
        driver = self.driver
        driver.get("https://www.thesparksfoundationsingapore.org")

        # get join us drop down element
        join_us = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[5]/a')

        # get why join us element inside drop down
        why_join_us = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]/a')

        # performing chain actions
        ActionChains(driver).move_to_element(join_us).click(
        ).move_to_element(why_join_us).click().perform()

        # automated form filling
        name = driver.find_element(By.XPATH, 
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]"
        )

        contact = driver.find_element(By.XPATH, 
            "/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]"
        )

        role = driver.find_element(By.XPATH, 
            "/html/body/div[2]/div/div[2]/div[2]/div/form/select"
        )

        # scroll
        y = 250
        for timer in range(0, 2):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 300
            time.sleep(1)

        # fill form
        name.send_keys("MK")
        time.sleep(2)

        contact.send_keys("mk@sparks.com")
        time.sleep(2)

        drp = Select(role)
        drp.select_by_visible_text("Intern")
        print("Filled Join Us form")

        go_to_top = driver.find_element(By.XPATH, '//*[@id="toTop"]')
        go_to_top.click()
        time.sleep(2)
        print("Join Us Page tested")
        print("-----------------------------------------\n")


    def test_Programs_Page(self):

        driver = self.driver
        driver.get(
            "https://www.thesparksfoundationsingapore.org"
        )

        # get join us drop down element
        programs = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[3]/a')

        # get why join us element inside drop down
        student_scholarship_program = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[3]/ul/li[1]/a')

        # performing chain actions
        ActionChains(driver).move_to_element(programs).click(
        ).move_to_element(student_scholarship_program).click().perform()

        student_mentorship_program = driver.find_element(By.XPATH, 
            '/html/body/div[2]/div/div[2]/div/ul/li[2]/a')

        time.sleep(2)
        student_mentorship_program.click()
        time.sleep(1)

        y = 250
        for timer in range(0, 7):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 200
            time.sleep(1)
        time.sleep(1)
        go_to_top = driver.find_element(By.XPATH, '//*[@id="toTop"]')
        go_to_top.click()
        time.sleep(2)
        print("Test Programs Page tested\n")
        print("-----------------------------------------\n")


    def test_Contact_Us_Page(self):
        driver = self.driver
        driver.get('https://www.thesparksfoundationsingapore.org')

        contact_us = driver.find_element(By.XPATH, 
            '//*[@id="link-effect-3"]/ul/li[6]/a')

        contact_us.click()
        time.sleep(1)

        # check heading
        heading = driver.find_element(By.CLASS_NAME, 'inner-tittle-w3layouts')
        heading_text = heading.text
        # check heading is correct
        self.assertIn("Contact Us", heading_text)
        print("Contact Us tested\n")
        print("-----------------------------------------\n")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()