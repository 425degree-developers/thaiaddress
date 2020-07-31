import joblib
import deepcut
import jsonlines

from sklearn_crfsuite import metrics, CRF
from sklearn.model_selection import train_test_split

from .parser import tokens_to_features
from .utils import range_intersect


LABELS_MAP = {
    "ชื่อ": "NAME",
    "ที่อยู่ย่อย": "ADDR",
    "ที่อยู่ - พื้นที่": "LOC",
    "รหัสไปรษณีย์": "POST",
    "เบอร์โทร": "PHONE",
    "อีเมล์": "EMAIL",
}
LABELS = list(LABELS_MAP.values())


def address_to_token(address: dict):
    """
    Transform address dictionary to a list of tokens

    Input
    -----
    >>> address = {
        "text": ...,
        "labels": [[start1, stop1, label1], [start2, stop2, label2]]
    }

    Output
    ------
    >>> [(token1, label1), (token2, label2), ...]
    """
    if address["labels"] != []:
        tokens = []
        s = 0
        for token in deepcut.tokenize(address["text"]):
            start = s
            stop = s + len(token)

            label = "O"
            for s, st, c in address["labels"]:
                if range_intersect(range(start, stop), range(s, st)):
                    label = c
            tokens.append((token, label))
            s = stop
        return tokens
    else:
        return None


def address_to_feature(address: dict):
    """
    Transform address dictionary to features and labels
    """
    tokens = address_to_token(address)
    features = [tokens_to_features(tokens, i) for i in range(len(tokens))]
    labels = [LABELS_MAP.get(label, "O") for _, label in tokens]
    return features, labels


def addresses_to_features(addresses: list):
    """
    Transform list of addresses to features and labels
    """
    X, y = [], []
    for address in addresses:
        # check if already labeled
        if len(address["labels"]) > 0:
            features, labels = address_to_feature(address)
            X.append(features)
            y.append(labels)
    return X, y


def train(file_path: str):
    """
    Training CRF model from a given ``file_path``
    """
    addresses = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            addresses.append(obj)
    addresses_train, addresses_val = train_test_split(
        addresses, test_size=0.25, random_state=42
    )

    X_train, y_train = addresses_to_features(addresses_train)
    X_val, y_val = addresses_to_features(addresses_val)

    crf = CRF(c1=0.2, c2=0.2, max_iterations=100, all_possible_transitions=True)
    crf.fit(X_train, y_train)

    # prediction score on validation set
    y_pred = crf.predict(X_val)
    metrics.flat_f1_score(
        y_val, y_pred, average="weighted", labels=[l for l in LABELS if l != "O"]
    )
    return crf
