# thaiaddress: A Parser for Thai Address

Parser for Thai address. ไลบรารี่เพื่อแยกแยะชื่อ/ที่อยู่/รหัสไปรษณีย์/เบอร์โทรศัพท์

สำหรับรายละเอียดเพิ่มเติมสามารถดูได้จาก [Data Science meetup, BKK #11](https://www.youtube.com/watch?v=0tPkQR_vXwc)

## Installation

You can install a recent development (recommended) using `pip` directly
from the repository

```sh
pip install git+git://github.com/425degree-developers/thaiaddress.git
```

or stable version from [PyPi](https://pypi.org/project/thaiaddress/) using

```sh
pip install thaiaddress
```

## Example Usage

```py
import thaiaddress
thaiaddress.parse("นายปรายุ้ด จันทร์กะเพรา 099-999-9999 25/25 ถ.พุทธมณฑล สาย 4 ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม 73170")

>>> {
    'text': 'นายปรายุ้ด จันทร์กะเพรา 25/25 ถ.พุทธมณฑล สาย 4 ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม 73170',
    'name': 'นายปรายุ้ด จันทร์กะเพรา',
    'address': '25/25 ถ.พุทธมณฑล สาย 4',
    'location': 'ต. ศาลายา อ.พุทธมณฑล จ.นครปฐม',
    'province': 'นครปฐม',
    'district': 'พุทธมณฑล',
    'subdistrict': 'ศาลายา',
    'postal_code': '73170',
    'phone_number': '0999999999',
    'email': ''
}
```

### Model Performance

We don't have an exact performance yet. So far, we got flat F1-score = 0.9414 (excluding "O" class),
on our validation set.

### Display output on Jupyter notebook

<img src="https://raw.githubusercontent.com/425degree-developers/thaiaddress/master/images/example-usage.png" />

## Development Plan

- This is an early version of our parser with very little data. We will make a better model relatively soon.

## Developers

This repository is developed at [425 Degree Co., Bangkok, Thailand](https://www.425degree.com/)

<img src="https://raw.githubusercontent.com/425degree-developers/thaiaddress/master/images/425degree-logo.png" />
