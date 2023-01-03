# pixoo64-twitter-integration
Gets Tweets from a specified Twitter List ID (found in the link of the Twitter List)
(Ex: List ID = 1609653853804441600, https://twitter.com/i/lists/1609653853804441600)

The Following is Shown for each Tweet on the Pixoo Screen:
- Tweet Text (middle)
- Tweet Author Profile Picture (bottom left)
- Tweet Author Name (bottom)
- Current Time in AM/PM (top right)
- If the Tweet Text takes up multiple pages, a Yellow Icon (top) will be shown along with the currently displayed Page Number in Yellow (also top)

![IMG_2303](https://user-images.githubusercontent.com/69360468/210299979-5305ca68-2aa2-4a99-a702-2c4afff192a9.jpeg)

Known Limitations:
- Tweet Text will not display emojis (not currently in the font used for displaying text)
- Tweet Author Names over 24 characters will be cut off (displays names of max 24 characters)
- Some other symbols will not be shown in Tweet Text (again limitation of font being used)
- Tweet Text cannot display tweets with new line formatting correctly (example of new line formatting below)

<img width="596" alt="Screenshot 2023-01-02 at 8 41 37 PM" src="https://user-images.githubusercontent.com/69360468/210301117-35b17b8f-2f27-4f07-bcb7-e9cd8f6c09c9.png">

Credits:
- Tweepy Twitter Python API Library (https://github.com/tweepy/tweepy)
- Pixoo 64 Python API Library (https://github.com/SomethingWithComputers/pixoo)
