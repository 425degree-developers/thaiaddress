# thaiaddress: A Parser for Thai Address

Parser for Thai address.

## Installing

```sh
git clone https://github.com/425degree-developers/thaiaddress
pip install .
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
    'postal_code': '73170',
    'phone_number': '0999999999',
    'email': ''
}
```
