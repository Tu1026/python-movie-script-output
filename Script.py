from urllib.request import urlopen
from fbchat.models import *
import fbchat
import time
from fbchat import Client
from fbchat.models import Message
from getpass import getpass 
import urllib
from bs4 import BeautifulSoup
# fbchat usage reference from https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/
# Find UID got to page source and search for entity_id
## impot movie script
# Feference https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
url = "https://web.njit.edu/~cm395/theBeeMovieScript/"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

# username = str(input("Username: ")) 
# client = fbchat.Client(username, getpass()) 
# story = urllib.request.urlopen("https://web.njit.edu/~cm395/theBeeMovieScript/")
# story_words = []
# for line in story:
#     line_words = line.decode("utf8").split()
#     for word in line_words:
#         story_words.append(word)

# story.close()

# only iterate the first 5 lines
# send to friends

# for word in story_words[:30]:
#     client.send(fbchat.models.Message(word),
#             100007996267897)
#     time.sleep(0.5)


#send to group
#iterate the whole script with 0.5 second interval between each line
# Thread_id = "2924605430988816"
# Thread_type = ThreadType.GROUP
# for word in story_words[:5]:
#     client.send(fbchat.models.Message(word),
#             thread_id=Thread_id, thread_type=Thread_type)
#     time.sleep(0.5)



# for word in story_words[:10]:
#     print(word)
#     time.sleep(0.5)



client.logout()
