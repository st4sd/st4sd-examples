#! /usr/bin/env python3
from __future__ import annotations

import sys
from typing import List

import pandas

import pandas as pd
VOWELS = ('a', 'e', 'i', 'o', 'u')


def main(path: str):
    df: pandas.DataFrame =  pandas.read_csv(path, engine="python", sep=None)

    words: List[str] = df['word'].to_list()

    # Maps "word" to its "vowels"
    ret = {}
    for word in words:
        if word not in ret:
            ret[word] = {vowel: 0 for vowel in VOWELS}
        for letter in word.lower():
            try:
                ret[word][letter] += 1
            except KeyError:
                pass
    # Create Dataframe with columns ["word", "a", "e", "i", "o", "u"]
    data = {
        x: [] for x in VOWELS + ('word', 'vowels')
    }
    for word, vowels in ret.items():
        data['word'].append(word)
        for v in VOWELS:
            data[v].append(vowels[v])
        data['vowels'].append(sum(vowels.values()))
    df = pd.DataFrame.from_dict(data)
    df.to_csv("vowels.csv", sep=";", index=False)


if __name__ == "__main__":
    main(sys.argv[1])