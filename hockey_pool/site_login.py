from selenium import webdriver

driver = webdriver.Edge(
    executable_path=r"C:\Users\marti\Downloads\edgedriver_win641\msedgedriver.exe"
)


def site_login(url, username, password, idun, idpw, idbutton):
    """Login to site of given url.

    :param url: url of the website's login page
    :type url: str
    :param username: username used for registration
    :type username: str
    :param password: password used for registration
    :type password: str
    :param idun: html id of the username field
    :type idun: str
    :param idpw: html id of the password field
    :type idpw: str
    :param idbutton: html id of the login form submission button
    :type idbutton: str
    """

    driver.get(url)
    driver.find_element_by_id(idun).send_keys(username)
    driver.find_element_by_id(idpw).send_keys(password)
    driver.find_element_by_name(idbutton).click()
