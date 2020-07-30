from itertools import groupby
import numpy as np
import deepcut
from pythainlp.util import isthai
from pythainlp.corpus import thai_stopwords


def preprocess(text):
    """
    Generalized function to preprocess an input
    """
    text = text.strip()
    text = text.replace('จัดส่ง', '')
    text = text.replace('ชื่อ ', '')
    text = text.replace('ผู้รับ', '')
    text = text.replace('\n-', ' ')
    text = text.replace('\n', ' ')
    text = text.replace(': ', ' ')
    text = ' '.join([t for t in text.strip().split(' ') if t.strip() != ''])
    return text


def is_stopword(word: str) -> bool:  # เช็คว่าเป็นคำฟุ่มเฟือย
    """
    Reference
    ----------
    Pythainlp, https://github.com/PyThaiNLP/pythainlp
    """
    return word in thai_stopwords()


def range_intersect(r1: range, r2: range):
    """
    Check if range is intersected

    References
    ----------
    Stack Overflow, https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
    """
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def merge_labels(preds: list):
    """
    Get merged labels and merge tuple to merge tokens
    """
    preds = list(np.ravel(preds))
    merge, labels = [], []
    s = 0
    for label, g in groupby(preds):
        g = list(g)
        labels.append(label)
        if len(g) > 1:
            merge.append((s, s + len(g)))
        s += len(g)
    return merge, labels


def merge_tokens(tokens: list, merge: list) -> list:
    """
    Merge tokens with 
    """
    for t in merge[::-1]:
        merged = "".join(tokens[t[0] : t[1]])  # merging values within a range
        tokens[t[0] : t[1]] = [merged]  # slice replacement
    return tokens
