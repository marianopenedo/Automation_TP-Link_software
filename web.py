from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


def web(login, passw, res, ssid, senhaW, model, cwd):
    logins = ["administrador", "", "admin"]
    passws = ["administrador", "", "admin"]

    if model == "1":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # opening browser
        service = Service(executable_path="%s\msedgedriver.exe" %cwd)
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
        # driver.get(res)
        url = "https://emulator.tp-link.com/EMULATOR_wr940nv6_eu_Router/userRpm/LoginRpm.htm"
        driver.get(url)

        time.sleep(3)

        if login == None and not passw == None:
            for i in logins:
                element = driver.find_element(By.XPATH, '//*[@id="userName"]')
                element.send_keys(i)
                element = driver.find_element(By.XPATH, '//*[@id="pcPassword"]')
                element.send_keys(passw)
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                time.sleep(3)
                check_url = driver.current_url
                if check_url == url: # res
                    continue
                else:
                    break

        elif passw == None and not login == None:
            for i in passws:
                element = driver.find_element(By.XPATH, '//*[@id="userName"]')
                element.send_keys(login)
                element = driver.find_element(By.XPATH, '//*[@id="pcPassword"]')
                element.send_keys(i)
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                time.sleep(3)
                check_url = driver.current_url
                if check_url == url: # res
                    continue
                else:
                    break

        elif passw == None and login == None:
            for i in logins:
                for x in passws:
                    element = driver.find_element(By.XPATH, '//*[@id="userName"]')
                    element.clear()
                    element.send_keys(i)
                    element = driver.find_element(By.XPATH, '//*[@id="pcPassword"]')
                    element.clear()
                    element.send_keys(x)
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                    time.sleep(10)
                    check_url = driver.current_url
                    if check_url == url: # res
                        continue
                    else:
                        break
                if check_url != url: # res
                    break

        time.sleep(5)
        driver.switch_to.frame(1)
        driver.find_element(By.ID, "a1").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame(2)
        driver.find_element(By.NAME, "Next").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "t_dhcp_opt").click()
        time.sleep(3)
        driver.find_element(By.ID, "dhcp_opt").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").click()
        time.sleep(3)
        element = driver.find_element(By.ID, "ssid1")
        time.sleep(3)
        actions = ActionChains(driver)
        time.sleep(3)
        actions.double_click(element).perform()
        driver.find_element(By.ID, "ssid1").click()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").clear()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").send_keys(ssid)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) #secType").click()
        time.sleep(3)
        driver.find_element(By.ID, "pskSecret").click()
        time.sleep(3)
        driver.find_element(By.ID, "pskSecret").click()
        time.sleep(3)
        element = driver.find_element(By.ID, "pskSecret")
        time.sleep(3)
        actions = ActionChains(driver)
        time.sleep(3)
        actions.double_click(element).perform()
        time.sleep(3)
        driver.find_element(By.ID, "pskSecret").clear()
        time.sleep(3)
        driver.find_element(By.ID, "pskSecret").send_keys(senhaW)
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        driver.quit()

    if model == "2":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = Service(executable_path="%s\msedgedriver.exe" %cwd)
        driver = webdriver.Edge(service=service, options=options)
        time.sleep(3)
        driver.maximize_window()
        # driver.get(res)
        url = "https://emulator.tp-link.com/EMULATOR_wr845nv1_en/userRpm/LoginRpm.htm"
        driver.get(url)

        time.sleep(7)
        
        if login == None and not passw == None:
            for i in logins:
                element = driver.find_element(By.XPATH, '//*[@id="userName"]')
                element.clear()
                element.send_keys(i)
                element = driver.find_element(By.ID, "pcPassword")
                element.clear()
                element.send_keys(passw)
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                time.sleep(10)
                check_url = driver.current_url
                if check_url == url: # res
                    continue
                else:
                    break

        elif passw == None and not login == None:
            for i in passws:
                element = driver.find_element(By.ID, "userName")
                element.clear()
                element.send_keys(login)
                element = driver.find_element(By.ID, "pcPassword")
                element.clear()
                element.send_keys(i)
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                time.sleep(10)
                check_url = driver.current_url
                if check_url == url: # res
                    continue
                else:
                    break

        elif passw == None and login == None:
            for i in logins:
                for x in passws:
                    element = driver.find_element(By.XPATH, '//*[@id="userName"]')
                    element.clear()
                    element.send_keys(i)
                    element = driver.find_element(By.ID, "pcPassword")
                    element.clear()
                    element.send_keys(x)
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
                    time.sleep(10)
                    check_url = driver.current_url
                    if check_url == url: # res
                        continue
                    else:
                        break
                if check_url != url: # res
                    break

        driver.switch_to.frame(1)
        driver.find_element(By.ID, "a1").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame(2)
        driver.find_element(By.NAME, "Next").click()
        time.sleep(3)
        driver.find_element(By.ID, "dhcp_opt").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").click()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").click()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").clear()
        time.sleep(3)
        element = driver.find_element(By.ID, "ssid1")
        element.clear()
        time.sleep(3)
        driver.find_element(By.ID, "ssid1").send_keys(ssid)
        driver.find_element(By.ID, "pskSecret").click()
        driver.find_element(By.ID, "pskSecret").click()
        time.sleep(3)
        element = driver.find_element(By.ID, "pskSecret")
        element.clear()
        driver.find_element(By.ID, "pskSecret").send_keys(senhaW)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) > .Item").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) #secType").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) #secType").click()
        time.sleep(3)
        element = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) #secType")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(3)
        driver.quit()
    
    # Em manutenção
    '''
    if model == "3":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        service = Service(executable_path="%s\msedgedriver.exe" %cwd)
        driver = webdriver.Edge(service=service, options=options)
        time.sleep(3)
        driver.maximize_window()
        # driver.get(res)
        url = "https://emulator.tp-link.com/ArcherC60v2_Emulator/index.html"
        driver.get(url)

        time.sleep(7)

        # driver.find_element(By.ID, "cloud-login-username").click()
        # element = driver.find_element(By.ID, "cloud-login-username")
        # if passw == None:
        #     for i in passws:
        #         elemnent = driver.find_element(By.ID, "cloud-login-username")
        #         element.clear()
        #         element.send_keys(login)
        #         element = driver.find_element(By.CSS_SELECTOR, "#cloud-form-login > .login-field:nth-child(2) .text-text:nth-child(1)")
        #         element.clear()
        #         element.send_keys(i)
        #         time.sleep(3)
        #         driver.find_element(By.XPATH, '//*[@id="cloud-login-btn"]').click()
        #         time.sleep(10)
        #         check_url = driver.current_url
        #         if check_url == url:
        #             continue
        #         else:
        #             break

        driver.switch_to.frame(0)
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".fst:nth-child(1) > .nav-wrap span").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id=\'quicksetup-language-setting\']/div[2]/div[2]/div/a/span").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id=\'quicksetup-language-setting\']/div[2]/div[2]/div/div/div[3]/div/div/ul/li[10]/label/span[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//button[@type=\'button\'])[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="quick-setup-wizard"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(3)
        # driver.find_element(By.CSS_SELECTOR, ".form-step:nth-child(2) .button-next > .text").click()
        driver.find_element(By.XPATH, '//*[@id="quick-setup-wizard"]/div[2]/div[3]/div[2]/div[2]/div/div[1]/button').click()
        time.sleep(3)
        driver.find_element(By.ID, "txt-wireless-name-ssid-2g").click()
        time.sleep(3)
        driver.find_element(By.ID, "txt-wireless-name-ssid-2g").click()
        time.sleep(3)
        element = driver.find_element(By.ID, "txt-wireless-name-ssid-2g")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        driver.find_element(By.ID, "txt-wireless-name-ssid-2g").clear()
        driver.find_element(By.ID, "txt-wireless-name-ssid-2g").send_keys(ssid)
        time.sleep(3)
        driver.find_element(By.ID, "txt-wireless-password-2g").clear()
        driver.find_element(By.ID, "txt-wireless-password-2g").send_keys(senhaW)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".form-step:nth-child(4) .button-next > .text").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".form-step:nth-child(5) .button-next").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".form-step:nth-child(6) .button-next > .text").click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,0)")
        '''
