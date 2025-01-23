from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


login_url = "https://loginv2.lpl.com/verify/rb_bf57182ppy?type=js3&sn=v_4_srv_21_sn_2DE7C7DB7458F997F71DF2E7A711742F_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1_app-3A89abd5935a22c7ad_1_app-3A11a128e5e0782157_1_app-3A3c8a4ceefcbbdbcd_1_app-3Ad6a1db4be768f98c_1_app-3Abaa94e4c2bc010a0_1_rcs-3Acss_0&svrid=21&flavor=post&vi=ACOMDHVLMENFHUARAKFRFMHLFMMRRPSR-0&modifiedSince=1737648379577&rf=https%3A%2F%2Floginv2.lpl.com%2Fverify%2F%3FspEntityID%3Dhttps%3A%252F%252Flogin.lpl.com%26goto%3Dhttps%3A%252F%252Fauth.advisor.lpl.com%252Fam%252Fsaml2%252Fjsp%252FidpSSOInit.jsp%253F%2526metaAlias%253D%252Falpha%252Fadvisorfridcprodidp%2526spEntityID%253Dhttps%25253A%25252F%25252Flogin.lpl.com%2526RelayState%253Dhttps%3A%252F%252Fclientworks.lpl.com%252F%2526redirected%253Dtrue&bp=3&app=baa94e4c2bc010a0&crc=4047637975&en=qg5x242m&end=1"
data_url = "https://webapi.lpl.com/activityqueryservicewebapi/api/InHouseActivity/QueryServiceProcess"  

payload = {
    "username": "ian.ritchie",
    "password": "Eagles@2019"
}

response = requests.post(login_url, data = payload)

print(f"Status Code: {response.status_code}")

driver = webdriver.Chrome()
driver.get("https://loginv2.lpl.com/verify/?spEntityID=https:%2F%2Flogin.lpl.com&goto=https:%2F%2Fauth.advisor.lpl.com%2Fam%2Fsaml2%2Fjsp%2FidpSSOInit.jsp%3F%26metaAlias%3D%2Falpha%2Fadvisorfridcprodidp%26spEntityID%3Dhttps%253A%252F%252Flogin.lpl.com%26RelayState%3Dhttps:%2F%2Fclientworks.lpl.com%2F%26redirected%3Dtrue")



button = driver.find_element_by_id("button-id")
button.click()
