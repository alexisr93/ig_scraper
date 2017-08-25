import urllib2
import json
import os

def createDir(ig_username):
    os.mkdir(ig_username + "_scrape")
    os.chdir(ig_username + "_scrape")
    return
def saveImages(url_list):
    num = 1
    for s in url_list:
        image = open(ig_username + '_' + str(num) + 'jpg','wb')
        image.write(urllib2.urlopen(s).read())
        image.close()
        num = num + 1

    return
def tw_geUrls():

    return

def ig_getUrls(ig_username, ig_id):
    if(ig_id == '0'):
        page = urllib2.urlopen('https://www.instagram.com/' + ig_username + '/media')
    else:
        page = urllib2.urlopen('https://www.instagram.com/' + ig_username + '/media/' + '?&max_id=' + str(ig_id))
    page_content = page.read()
    page.close()

    parsed_page = json.loads(page_content)

    num = 0
    while (num < len(parsed_page['items'])):
        url_list.append(str(parsed_page['items'][num]['images']['standard_resolution']['url']))
        num = num + 1

    if(parsed_page['more_available']):
        ig_getUrls(ig_username, str(parsed_page['items'][-1]['id']))
    else:
        return

##Starts heres##
ig_username = raw_input('Instagram username: ')
url_list = []
ig_getUrls(ig_username, '0')
createDir(ig_username)
saveImages(url_list)

print "Done."


# TODO add ability to choose change folder name, and or no folder
# TODO error checking
