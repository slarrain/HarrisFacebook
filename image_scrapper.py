__author__ = 'Santiago Larrain'

import urlparse
import requests
import os
import bs4
import json
import urllib

list_url = 'http://harris.uchicago.edu/directory/students/name'
download_path = "C:\Users\Santiago\PycharmProjects\HarrisFacebook"

######### CODIGO COPIADO DE CS122 - UNIVERSITY OF CHICAGO - PA1  #########

def get_request(url):
    '''
    Open a connection to the specified URL and if successful
    read the data.
    Inputs:
        url: must be an absolute URL
    Outputs:
        request object or None
    Examples:
        get_request(&quot;http://www.cs.uchicago.edu&quot;)
    '''
    try:
        html = requests.get(url)
        return html
    except:
        # fail on any kind of error
        print 'Error'
        return None

def read_request(request):

    try:
        return request.text.encode('utf-8')
    except:
        print 'read failed: ' + request.url
        return ''
####### END OF COPIED CODE  ########


def read(url):
    req = get_request(url)
    htmlstring = read_request(req)
    htmlsoup = bs4.BeautifulSoup(htmlstring)
    return htmlsoup

def img_url_list(htmlsoup):
    image_list = []
    #print htmlsoup
    souptable = htmlsoup.find(id="content-area")
    #print souptable
    images = souptable.find_all('img')
    #print images
    for x in images:
        a = x['src']
        print a[-12:]
        if (a[-12:]!= 'gargoyle.jpg'):
            b = a[:70]+'large'+a[75:]
            image_list.append(b)
    #print image_list
    return image_list

def retrieve_picture(url):
    filename = url.split('/')[-1]
    print filename
    filename = download_path+'\\'+filename
    urllib.urlretrieve(url, filename)

def retrieve_list(image_list):
    for x in image_list:
        retrieve_picture(x)

if __name__ == "__main__":
    x = read(list_url)
    y = img_url_list(x)
    #for n in y:
        #print n

    retrieve_list(y)
    print 'Done'

