import time

from datetime import datetime as dt

#hosts file path
hosts_path = "/etc/hosts"



redirect = "127.0.0.1"

#list of websites which you want to block
website_list =["www.facebook.com","facebook.com","instagram.com","www.instagram.com"]

while True:
    #time which you want to block the websites, here it is from 9 am to 10 PM daily
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):
        print("Working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"  "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


        print("Fun hours:")
    #time to check the script
    time.sleep(60)