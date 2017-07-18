"""Test for the autocomplete function."""
import pytest


def test_autocomplete():
    """Test that output is correct given list of vocab."""
    from autocomplete import AutoCompleter
    vocab = ['fae', 'faerie', 'fox', 'fir', 'forest', 'favorite', 'favored']
    completer = AutoCompleter(vocab)
    assert sorted((completer('fae'))) == sorted(['fae', 'faerie'])
    assert sorted(completer('fa')) == sorted(['fae', 'faerie', 'favorite', 'favored'])
    assert sorted(completer('f')) == sorted(['fox', 'fir', 'forest', 'favored', 'favorite'])


def test_autocomplete_word_limit():
    """Test that output is correct given list of vocab and a word limit."""
    from autocomplete import AutoCompleter
    vocab = ['fae', 'faerie', 'fox', 'fir', 'forest', 'fern', 'favorite', 'favored']
    completer = AutoCompleter(vocab, 1)
    assert(completer('fae')) == ['fae']


def test_autocompleter_loads_from_file():
    """Test that the autocompleter can load from a file."""
    from autocomplete import AutoCompleter
    completer = AutoCompleter('/usr/share/dict/words')
    assert 'dinosaur' in completer('dinosa')
