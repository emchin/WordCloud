"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import gathering_words, choosing_color, changing_hue, create_cloud

def test_gathering_words():
	assert isinstance(gathering_words('message_1.json'), str)
	assert "â" not in input_words
	assert isinstance(message_dict, dict)

def test_choosing_color():
	assert isinstance(x, str)
	assert isinstance(input_color, int)
	assert 0 <= input_color <= 6

def test_word_frequencies():
	assert isinstance(frequencies, dict)

def test_create_cloud():
	assert isinstance(mask_url, str)

                 
    