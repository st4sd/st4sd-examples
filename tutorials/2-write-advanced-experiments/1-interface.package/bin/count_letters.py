#! /usr/bin/env python3
from __future__ import annotations

import sys
from typing import List

import pandas

import pandas as pd
import string


def main(path: str):
    df: pandas.DataFrame =  pandas.read_csv(path, engine="python", sep=None)

    words: List[str] = df['word'].to_list()

    # Create Dataframe with columns ["word", "letters"]
    data = {
        x: [] for x in ('word', 'letters')
    }

    for word in words:
        data['word'].append(word)
        data['letters'].append(sum((1 for x in word if x in string.ascii_letters)))

    df = pd.DataFrame.from_dict(data)
    df.to_csv("letters.csv", sep=";", index=False)


if __name__ == "__main__":
    main(sys.argv[1])