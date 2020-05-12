#!/usr/bin/env python 
""" Retrieve all line from a movie script with given url and print
one line at a time to friend/group on fb messenger with given uid.
    
Usage:

    python3 scrip.py

"""
# Feference https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
# fbchat usage reference from https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/


import sys
from urllib.request import urlopen
from fbchat.models import *
import fbchat
import time
from fbchat import Client
from fbchat.models import Message
from getpass import getpass 
from bs4 import BeautifulSoup


def fetch_lines(url: str) -> list: 
    """Get the all words from given url without "script" and "style"
        
        Args:
            url of the given website 
        
        Returns:
            A string that contains all lines of the movie with given URL
    """
    #import using the given url
    urlusing = url
    html = urlopen(urlusing).read()
    soup = BeautifulSoup(html, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style",]):
        script.extract()  

    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    #split the words by spaces
    words = text.split()
    return words


def print_lines_to_friends(words: str, uid: str):
    """print the given string one word at a time to fb friend
        Args: 
            a string that contain multiple words, the uid of the fb friend
            user input: username and password
    """
    username = str(input("Username: ")) 
    client = fbchat.Client(username, getpass()) 
    for word in words:
        client.send(fbchat.models.Message(word),
                uid)
        time.sleep(1)
    client.logout()



def print_lines_to_group(words: str, uid: str):
    """print the given string one word at a time to fb grounp
    
        Args:
            a string that contain multiple words, the uid of the fb group
            user input: username and password
    """
    username = str(input("Username: ")) 
    client = fbchat.Client(username, getpass()) 
    Thread_id = str
    Thread_type = ThreadType.GROUP
    for word in words:
        client.send(fbchat.models.Message(word),
                thread_id=Thread_id, thread_type=Thread_type)
        time.sleep(1)
    client.logout()


def fetch_lines_keep_headers(url: str) -> list:
    """Get the all words from given url as a list keeping headers and styles
        
        Args:
            url of the given website 
        
        Returns:
            A string that contains all lines on the website with given url
    """
    story = urlopen(url)
    story_words = []    
    for line in story:
        line_words = line.decode("utf8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def check_behaviour(lst: list):
    """ Output one word at a time from given list to consoel

        Args: 
            a list of strings
    """
    for word in lst[:5]:
        print(word)
        time.sleep(1)

def main():  
    """print movie script with given url one word at a time to fb friend or group with given uid

        Args:
            url of the script
            uid of the fried/group
            string indicate where it is a group or individaul uid
    """
    url = input("what is the website url?")
    uid = input("what is the uid of your friend/group?")
    friend_or_group = input("Is it for a 'friend' or 'group'")
    text = fetch_lines(url)
    if friend_or_group.lower() == "friend":
        print_lines_to_friends(url, uid)
    elif friend_or_group.lower() == "group":
        print_lines_to_group(url, uid)
    else:
        print("Invalid input start over")
        return 
    

if __name__ == "__main__":
    main()