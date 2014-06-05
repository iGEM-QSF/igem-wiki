import sys                          #for command-line arguments
import urllib.request               #for http
import http.cookiejar as cookielib  #for cookies and session
from urllib import parse            #for urlencode
import getpass                      #password reading from commandline
#import urllib
#------ SETTINGS -------#
LOGIN_URL = "http://igem.org/Login"
#DO NOT end base url with "/"
BASE_URL = "http://2014.igem.org/wiki/index.php?title=Team:Aalto-Helsinki"
AUTO_PAGES = ["index","testpreview"]
#-----------------------#

# Wrangler class - parser object which parses HTML
from html.parser import HTMLParser
class Wrangler(HTMLParser):
    #The tags, a.k.a. id's are stored here. For example wpEditToken
    ids = {}
    #Method which handles every start tag eg. <input>
    def handle_starttag(self, tag, attrs):
        if (tag == 'input'):
            for i in attrs:
                if (i[0] == 'name'):
                    if (i[1] == 'wpAutoSummary' or i[1] == 'wpEditToken' or i[1] == 'wpSave' or i[1] == 'wpSection' or i[1] == 'wpStarttime' or i[1] == 'wpEdittime' or i[1] == 'oldid'):
                        name = i[1]
                        value = [c for c in attrs if c[0]=='value'][0][1]
                        self.ids[name]=value
                 

            

#http://stackoverflow.com/questions/189555/how-to-use-python-to-login-to-a-webpage-and-retrieve-cookies-for-later-usage                   
#def main(argv=sys.argv):
def upload(page, file, headerfooter = False):                        
    global opener 
    #-------- get edit id --------#
    try:
        if (page == "index"):
            resp = opener.open(BASE_URL+"&action=edit")
        else:
            resp = opener.open(BASE_URL+"/"+page+"&action=edit")
        content = resp.read()
        parser = Wrangler()
        parser.feed(content.decode('utf8'))
        data = parser.ids #stores wpEditToken and wp AutoSummary
    #except NameError:
    except:
        print("Error:", sys.exc_info()[0])
        return 3
    
    #---- read requested file ----#
    try:
        with open (file, "r") as myfile:
            file_data=myfile.read().replace('\n', '')
    except FileNotFoundError:
        #print("File {:s} not found".format(file))
        return 2
     
    #---- read header & footer ---#
    if (headerfooter == True):
        try:
            with open ("include/header.html", "r") as myfile:
                header_data=myfile.read().replace('\n', '')
        except FileNotFoundError:
            print("no include/header.html found. Not including")
            header_data = ""

        try:
            with open ("include/footer.html", "r") as myfile:
                footer_data=myfile.read().replace('\n', '')
        except FileNotFoundError:
            print("no include/footer.html found. Not including")
            footer_data = ""
        file_data = header_data+file_data+footer_data
    #------- post new edit -------#
    try:
        data['wpTextbox1'] = file_data
        #data['wpSave'] = 'Save page'
            
        encoded_data = parse.urlencode(data)
        resp = opener.open("http://2014.igem.org/wiki/index.php?title=Team:Aalto-Helsinki/testpreview&action=submit", encoded_data.encode('utf8'))
        #print (resp.read())
        #headers = {"Content-type": "multipart/form-data;",
    except:
        print("Error:", sys.exc_info()[0])
        return 3
    #print('No errors encountered. Although i cannot verify the success :)')
    return 0


def login( username, password):
    global opener
    #---------- log in------------#
    try:
        login_data = {'id':'0','new_user_center':'','new_user_right':'','hidden_new_user':'','return_to':'http://2014.igem.org/wiki/index.php?title=Team:Aalto-Helsinki/testpreview&action=edit','username':username,'password':password,'Login':'Log+in','search_text':''}
        cookie = cookielib.CookieJar()
        opener = urllib.request.build_opener( urllib.request.HTTPCookieProcessor(cookie))
        encoded_data = parse.urlencode(login_data)
        resp = opener.open(LOGIN_URL, encoded_data.encode('utf8'))
    except urllib.error.URLError:
        print("Login server not found. Perhaps the URL is wrong in the code?")
        return 1
    except:
        print("Error:", sys.exc_info()[0])
        return 1
    return 0


def main(argv=sys.argv):
    #----- arguments -------------#
    try:
        if (argv[1] != '-auto'):
            page = argv[1]
            file = argv[2]
    except IndexError:
        print("Usage: upload.py wikipage filename\n\nwikipage\tThe subpage in the wiki.\n\t\teg. in igem.org/wiki/index.php?title=Team:teamname/members\n\t\twikipage=members\n\nfile\t\tfilename in current directory")
        return

    #------- read input ----------#    
    try:
        print("-- iGEM wiki quickify --\ncmd + d to abort.")
        username = input("Username: ")
        password = getpass.getpass('Password: ')
        #input("Password: ")
    except EOFError:
        print("Aborting...")
        return 1
    print("Logging in")
    if (login(username, password) != 0):
        print("Server error when logging in")
        return 1
    #------- automation ---------#
    if (argv[1] == '-auto'):
        print("Auto updating pages: ",",".join(AUTO_PAGES))
        for p in AUTO_PAGES:
            r=upload(p,p+".html", True)
            if (r == 2):
                print("{:s}.html\t\tFile not found".format(p))
            elif (r== 1):
                print("{:s}.html\t\tServer error".format(p))
            elif (r== 3):
                print("{:s}.html\t\tUnknown error".format(p))
            else:
                print("{:s}.html\t\tUploaded".format(p))
    else:
        print("Uploading contents of \"{:s}\" to \"{:s}\"".format(file, page))
        upload( page, file)
    print("Done")
        
                
main()
