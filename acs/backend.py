from bs4 import BeautifulSoup
import requests


def is_td_and_has_no_class(tag):
    return tag.name == 'td' and not tag.has_attr('class')


class OfferingAH:
    WEBSITE_URL = "http://www.ah-wohnen.at"
    WEBSITE_QUERY = "/freie-objekte.57.html"

    def __init__(self):
        self.title = ""
        self.address = ""
        self.plz = ""
        self.rooms = ""
        self.area = ""
        self.link = ""
        self.pic = ""

    def __repr__(self):
        return "Title:%s Address:%s Plz:%s Rooms:%s Area:%s Link:%s Pic:%s" % (
            self.title, self.address, self.plz, self.rooms, self.area, self.link, self.pic)

    def get_all_offerings(self):
        page = requests.get(self.WEBSITE_URL + self.WEBSITE_QUERY)

        soup = BeautifulSoup(page.content, 'html.parser')

        objektliste = soup.find(class_="objektliste")
        offerings = objektliste.find_all("tr")

        offeringlist = []

        for offering in offerings:
            objectoffering = OfferingAH()
            objectoffering.pic = self.WEBSITE_URL + offering.find(class_="pic").a.img['src']
            objectoffering.link = self.WEBSITE_URL + offering.find(class_="details").a['href']

            for idx, classlessColumn in enumerate(offering.find_all(is_td_and_has_no_class)):
                content = classlessColumn.contents

                if idx == 0:
                    objectoffering.title = content[0]
                    objectoffering.address = content[2]
                    objectoffering.plz = content[4]
                elif idx == 1:
                    objectoffering.rooms = content[0]
                    objectoffering.area = content[2]
                else:
                    print('Unknown Column')

            offeringlist.append(objectoffering)

        return offeringlist
