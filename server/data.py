from uuid import uuid4 as uuid
from datetime import date

data = [
    {
        "id": uuid(),
        "address_name": "98 Albert Road, Coventry, CV65 4BP",
        "country": "United Kingdom",
        "from_date": date(year=2004, month=2, day=1),
        "to_date": date(year=2008, month=11, day=1)
    },
    {
        "id": uuid(),
        "address_name": "50 Bt Batok East Ave 5 #17-01, Singapore, 659801",
        "country": "",
        "from_date": date(year=2008, month=11, day=1),
        "to_date": date(year=2013, month=4, day=1)
    },
    {
        "id": uuid(),
        "address_name": "Strada Gh.Ionescu Sisesti 256-260, Bucuresti",
        "country": "Romania",
        "from_date": date(year=2013, month=4, day=1),
        "to_date": date(year=2015, month=1, day=1)
    },
    {
        "id": uuid(),
        "address_name": "Extramuros 94, Valdilecha, Madrid, 28511",
        "country": "Spain",
        "from_date": date(year=2015, month=1, day=1),
        "to_date": None
    },
]

def get_data():
    return data