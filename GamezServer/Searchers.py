import GamezServer
import urllib
import urllib2
from GamezServer.UsenetCrawler import UsenetCrawler
from GamezServer.DAO import DAO
class Searchers(object):
    """description of class"""
    

    def GetSearcher(self,searcherName,forceNew):
        if(searcherName == "usenetCrawler"):
            return UsenetCrawler(forceNew)
        return None

    def SendToSab(self,sabnzbdBaseUrl,sabnzbdApiKey,nzbLink,nzbTitle, wantedGameId):
        dao = DAO()
        nzbTitle = "[" + str(wantedGameId) + "] - " + nzbTitle
        category = dao.GetSiteMasterData('sabnzbdCategory')
        sabUrl = sabnzbdBaseUrl
        if(sabUrl.endswith('/') == False):
            sabUrl = sabUrl + "/"
        sabUrl = sabUrl + "sabnzbd/api"
        sabUrl = sabUrl + "?apikey=" + sabnzbdApiKey
        sabUrl = sabUrl + "&mode=addurl&name=" + urllib.quote_plus(nzbLink)
        sabUrl = sabUrl + "&nzbname=" + urllib.quote_plus(nzbTitle)
        if(category != None and category != ""):
            sabUrl = sabUrl + "&cat=" + category
        sabRequest = urllib2.Request(sabUrl, headers={'User-Agent' : "GamezServer"})
        response = urllib2.urlopen(sabRequest)
        sabRespData = response.read()
        return sabRespData

        # Request should look like this:
        # http://192.168.2.101:8080/sabnzbd/api?apikey=7a79d445c6264af9a1c45eeeb2107e83&mode=addurl&name=https%3A%2F%2Fapi%2Enzbgeek%2Einfo%2Fapi%3Ft%3Dget%26id%3Dd68d460b98a01224fc1ac39a38782210%26apikey%3D2241b43033d3336cac268c8775fa1993&nzbname=&cat=games
