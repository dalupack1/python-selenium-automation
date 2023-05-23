#amazon locator

1. Amazon logo link
driver.find_element(By.Css_selector, 'i.a-icon.a-icon-logo')

2.Create Account link
driver.find_element(By.Css_selector, 'h1.a-spacing-small')

3.Your name box
driver.find_element(By.Css_selector, 'input#ap_customer_name')

4.Email or Phone number box
driver.find_element(By.Css_selector, 'input#ap_email')

5.Password input box
driver.find_element(By.Css_selector, 'input#ap_password')

6.Password info icon
driver.find_element(By.Css_selector, "div[class*='a-box a-alert-inline a-alert-inline-info']"

7.Re-enter password box
driver.find_element(By.Css_selector, '#ap_password_check'

8.Create your Amazon account tab
NA

9.Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

10.Privacy Notice link
driver.find_element(By.Css_selector, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']"

11.Signin link
driver.find_element(By.Css_selector, "a[href*='/ap/signin']"