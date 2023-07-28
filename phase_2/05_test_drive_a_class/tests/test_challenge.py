from lib.challenge import *
import pytest
"""
def test_check_valid_text()
check("The dog jumped over the fence.")
assert True 

def test_check_missing_capital_letter()
check("the dog jumped over the fence.")
assert False

def test_check_missing_punctuation()
check("The dog jumped over the fence")
assert False

def test_check_missing_punctuation_and_capital()
check("the dog jumped over the fence")
assert False


def test_percentage_good_100_percent()
assert 100

def test_percentage_good_50_percent()
assert 50

def test_percentage_good_33_percent()
assert 33

def test_percentage_good_0_percent()
assert 0
"""

def test_check_valid_text():
    grammar_stats = GrammarStats()
    is_valid = grammar_stats.check("The dog jumped over the fence.")
    assert is_valid == True

def test_text_with_no_grammar_mistakes():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hi, my name is Bob." )
    assert result == True

def test_text_with_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hi my name is bob")
    assert result == False

def test_text_with_no_capitalised_letter():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hi my name is bob.")
    assert result == False
    
def test_text_with_no_punctuation_or_capitalised_letter():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hi my name is bob")
    assert result == False


def test_text_with_no_punctuation_or_capitalised_letter():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
       grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "No text input provided"

def test_percentage_good_100_percent():
    grammar_stats = GrammarStats()
    check1 = grammar_stats.check("Hi, my name is Bob." )
    check2 = grammar_stats.check("Hi, my name is Bob." )
    check3 = grammar_stats.check("Hi, my name is Bob." )
    check4 = grammar_stats.check("Hi, my name is Bob." )
    result = grammar_stats.percentage_good()
    assert result == 100

def test_percentage_good_50_percent():
    grammar_stats = GrammarStats()
    check1 = grammar_stats.check("Hi, my name is Bob." )
    check2 = grammar_stats.check("hi, my name is Bob." )
    check3 = grammar_stats.check("Hi, my name is Bob." )
    check4 = grammar_stats.check("hi, my name is Bob" )
    result = grammar_stats.percentage_good()
    assert result == 50
    
def test_percentage_good_33_percent():
    grammar_stats = GrammarStats()
    check1 = grammar_stats.check("Hi, my name is Bob." )
    check2 = grammar_stats.check("hi, my name is Bob." )
    check3 = grammar_stats.check("Hi, my name is Bob" )
    result = grammar_stats.percentage_good()
    assert result == 33

def test_percentage_good_0_percent():
    grammar_stats = GrammarStats()
    check1 = grammar_stats.check("hi, my name is Bob." )
    check2 = grammar_stats.check("hi, my name is Bob." )
    check3 = grammar_stats.check("Hi, my name is Bob" )
    result = grammar_stats.percentage_good()
    assert result == 0