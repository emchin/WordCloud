"""A collection of function for doing my project."""
def gathering_words(messenger_json):
    '''Loads Messenger chat data as a dictionary, and iterates over each object to pull the messages.
    I learned how to load JSON documents using this source:
       https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
       However, everything (EXCEPT the first block of code)
       is mine.
    Parameters:
    messenger_json: json file
        JSON file that contains the facebook messanger chat history

    Returns:  
    --------
    input_words: string
        String that contains all the words in the chat messages
    '''
    import json
    with open(messenger_json) as raw_data:
        message_dict = json.load(raw_data)

    input_words = ""
    input_list = []

    #Apparently, Messenger stores 'This poll is no longer available' as a 'message'
    #so we need to filter it out on a sentence-by-sentence basis.
    for sentence in message_dict['messages']:
        if 'content' in sentence:
            if sentence['content'] != 'This poll is no longer available.':
                input_list.append(sentence['content'])

    #JSON sometimes mixes up " 's" with "â" (for example, "it's" becomes "itâ")
    #so we need to filter that out on a word-by-word basis
    for word in input_list:
        if 'â' not in word:
            input_words = input_words + word + " "
    return input_words

def clean_words():
    '''Takes the words above and removes the stopwords.

    Returns:
    --------
    clean_text: list
        List that stores all of the words that are not stopwords
    '''
    from wordcloud import STOPWORDS
    clean_text = []
    unclean = gathering_words('/Users/emily/Desktop/ProjectTemplate/my_module/message_1.json')
    add_stops = ["I", "the", "to", "a", "i", "a", "like", "your", "it's", "also", 
    "of", "the", "on", "up", "was", "really", "too", "But", "how", "like", "if", "do", "or"
	"and", "but", "are", "don't", "can't", "them", "go", "It's", "And", "that", "we", "they"
	"my", "also", "he", "It", "then", "for", "that's", "as", "all", "time", "can", "its",
	"would", "okay", "got", "too", "maybe", "I'm", "oh", "bad", "say", "thought", "someone",
	"look", "taking", "remember", "come", "And", "day", "well", "making", "getting", "apparently",
	"make", "made", "hi", "hate", "though", "Yeah", "yeah", "Oh", "Okay", "You", "take", "one", "good",
	"Wait", "thing", "makes", "think", "going", "Its", "now", "My", "I've", "The", "im", "What", "That",
	'THE', "If", "Not", "Also", "Or", "She", "might", "Well", "dont", "No", "Like ", "You", "You "]
    stopwords =  add_stops + list(STOPWORDS)
    for word in unclean.split():
        if word not in stopwords:
            clean_text.append(word)

    return clean_text

def word_frequencies():
    '''Takes the raw input of words (from above) and sorts by frequency.

	   I used this source to sort the words by frequency: 
	   https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
	   I then reformatted it into a dictionary called "frequencies."

	   Returns:
	   --------
	   frequencies: dictionary
	   	   Dictionary that stores a word as its key, and the word's
	   	   frequency as its value.
	'''
    frequencies = {}
    from collections import Counter
    raw_words = clean_words()
    Counter = Counter(raw_words)
    most_common = Counter.most_common(200)

    for word, freq in most_common:
        frequencies[word] = freq
    return frequencies

def choosing_color():
    '''Asks for an input color and, after checking that it's an int, returns it

    Returns:
    --------
    input_color: integer
        Integer corresponding to a certain color
    '''
    question = """What color would you like your wordcloud to be?
    For grey, input 0
    For red, input 1
    For orange, input 2
    For yellow, input 3
    For green, input 4
    For blue, input 5
    For purple, input 6
    Input: """
    while True:
        num = input(question)
        if num not in ['0', '1', '2', '3', '4', '5', '6']:
            print("Sorry! That isn't a valid number. Please try again!")
            continue
        else:
            break

    input_color = int(num)
    return input_color

def choosing_shape():
    '''Asks for an input shape and, after checking that it's an int, returns it

    Returns:
    --------
    input_shape: string
        String URL path to an image. This image determines the shape of the
        wordcloud.
    '''

    question = """What shape would you like your wordcloud to be?
    For a rectangle/tapestry, input 0
    For heart, input 1
    For star, input 2
    For flower, input 3
    Input: """
    while True:
        num = input(question)
        if num not in ['0', '1', '2', '3']:
            print("Sorry! That isn't a valid number. Please try again!")
        else:
            break
    input_shape = int(num)

    if input_shape == 0:
        mask_url = '../my_module/masks/black.jpg'
    elif input_shape == 1:
        mask_url = '../my_module/masks/heart.png'
    elif input_shape == 2:
        mask_url = '../my_module/masks/star.jpg'
    elif input_shape == 3:
        mask_url = '../my_module/masks/flower.png'
    return mask_url

def changing_hue(word, font_size, position, orientation, random_state=None, input_color=choosing_color(), **kwargs):
    '''Takes the input color (ex: blue) and returns a hue (ex: sky, aqua, navy, etc.)

    I used this source: https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html
    to reference for HSL formatting and how to add the kwargs.
    However, I added different colors (other than grey), which was NOT in the source material.

    Parameters:
    ----------
    word, font_size, position, orientation: kwargs
        These are key word arguments that need to be passed 
        by the wordcloud function. We don't need to give it input.
        This just represents that every word on the wordcloud will/
        should have a different word, font size, position, etc.

    random_state=None: kwarg
        This is another key word argument that requires no input.
        This is necessary to pass to the wordcloud so that it knows
        that the color of each word will be randomly changing as well.

    input_color = input_color(): integer
        Integer generated by changing_color(). This determines what
        colors that the code is going to generate shades of.

    Returns:
    --------
    color_range: string
        String containing the HSL of a shade of the input_color.
    '''
    import random

    if input_color == 0:
        color_range = "hsl(0, 0%%, %d%%)" % random.randint(20,55)
    else:
        if input_color == 1:
            hue = 0
        elif input_color == 2:
            hue = 30
        elif input_color == 3:
            hue = 50
        elif input_color == 4:
            hue = 125
        elif input_color == 5:
            hue = 235
        elif input_color == 6:
            hue = 300
        color_range = "hsl(%d, 100%%, %d%%)" % (hue, random.randint(20, 63))

    return color_range

def create_cloud(mask_url=choosing_shape()):
    '''Takes gathered words into a wordcloud.
        Also generates different hues of color for each word in the cloud.
        These words are put into a wordcloud in the shape of a heart.

        I used these sources to form the wordcloud:
        https://blog.goodaudience.com/how-to-generate-a-word-cloud-of-any-shape-in-python-7bce27a55f6e
        https://amueller.github.io/word_cloud/auto_examples/a_new_hope.html

        Parameters:
        ----------
        mask_url: string
            String URL generated by choosing_shape that is a path to an
            image. This image determines what shape the wordcloud
            will be.

        Almost everything in this code (save for substitutions
        for urls, different heights, different masks, etc.) is NOT mine.
    '''
    from wordcloud import WordCloud
    from PIL import Image
    import urllib
    import numpy as np
    import matplotlib.pyplot as plt

    words = word_frequencies()
    mask = np.array(Image.open(mask_url))

    word_cloud = WordCloud(width=512, height=512, margin=10, 
        background_color='white', mask=mask)
    word_cloud = word_cloud.generate_from_frequencies(words)

    plt.figure(figsize=(10, 8), facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud.recolor(color_func=changing_hue), interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()