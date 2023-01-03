import os
import sys
import requests
import time
import math
from types import NoneType
from io import BytesIO
from PIL import Image
from datetime import datetime
from pprint import pprint
import tweepy
from pixoo import Channel, ImageResampleMode, Pixoo, SimulatorConfig, TextScrollDirection

ipAdd = 'Pixoo 64 IP Connection Address Goes Here'
bearerToken = 'Twitter Bearer Token Goes Here (go to developer.twitter.com to get one)'
twitterListId = 1 #Twitter List ID Goes Here as a int (replace the 1)

twitterBlueColor = (38, 167, 222)
whiteColor = (255, 255, 255)
goldColor = (255, 215, 0)
blackColor = (0, 0, 0)

client = tweepy.Client(bearerToken)

#pixoo = Pixoo(ipAdd, simulated=True, simulation_config=SimulatorConfig(10))
pixoo = Pixoo(ipAdd, 64, False)

pixoo.clear()

def printTweet(strText, userStr, userPic):
    if len(strText) > 16:
        chunks = [strText[i:i+16] for i in range(0, len(strText), 16)]
        if len(chunks) > 7:
            pages = math.ceil(len(chunks) / 7)

            for f in range(pages):
                for j in range((f * 7), ((f + 1) * 7)):
                    if j >= len(chunks):
                        pass
                    else:
                        pixoo.draw_text(chunks[j], (0, 9 + ((j - (f * 7)) * 6)))

                printScreen(15, userStr, userPic, str(f + 1))
        else:
            for j in range(len(chunks)):
                pixoo.draw_text(chunks[j], (0, 9 + (j * 6)))

            printScreen(15, userStr, userPic)
    else:
        pixoo.draw_text(str, (0, 9))

        printScreen(15, userStr, userPic)

def printUsername(str, imgUrl):
    if len(str) > 12:
        chunks = [str[i:i+12] for i in range(0, len(str), 12)]

        for j in range(len(chunks)):
            pixoo.draw_text(chunks[j], (15, 51 + (j * 6)))
    else:
        pixoo.draw_text(str, (15, 51))

    imgResponse = requests.get(imgUrl)
    img = Image.open(BytesIO(imgResponse.content))
    imgResized = img.resize((12, 12))
    pixoo.draw_image(imgResized, (1, 51))

def printTwitterIcon():
    pixoo.draw_filled_rectangle((0, 0), (7, 7), twitterBlueColor)
    pixoo.draw_filled_rectangle((2, 1), (3, 5), whiteColor)
    pixoo.draw_filled_rectangle((3, 5), (5, 6), whiteColor)
    pixoo.draw_filled_rectangle((4, 2), (5, 3), whiteColor)

def printMultiPageIcon(char):
    if char is None:
        pass
    else:
        pixoo.draw_line((10, 1), (16, 1), goldColor)
        pixoo.draw_line((10, 3), (16, 3), goldColor)
        pixoo.draw_line((10, 5), (13, 5), goldColor)
        pixoo.draw_character(char, (18, 1), goldColor)

def printScreen(num, stri, pict, char=None):
    printTwitterIcon()
    printMultiPageIcon(char)
    printUsername(stri, pict)
    pushTimeout(num)

def printTime():
    pixoo.draw_filled_rectangle((46, 1), (62, 5), blackColor)
    pixoo.draw_pixel((54, 2), (255, 255, 255))
    pixoo.draw_pixel((54, 4), (255, 255, 255))

    now = datetime.today()
    currtimeh = now.strftime("%I")
    currtimem = now.strftime("%M")
    pixoo.draw_text(currtimeh, (46, 1), (255, 255, 255))
    pixoo.draw_text(currtimem, (56, 1), (255, 255, 255))

def pushTimeout(num):
    for h in range(num):
        printTime()
        pixoo.push()

        time.sleep(1)
    pixoo.clear()

def main():
    tweetResponse = client.get_list_tweets(twitterListId, max_results = 100, expansions=['author_id'])
    for tweet in tweetResponse.data:
        userResponse = client.get_user(id=tweet.author_id, user_fields=['profile_image_url'])
        printTweet(tweet.text, userResponse.data.name, userResponse.data.profile_image_url)

        time.sleep(0.1)

if __name__ == '__main__':
    main()