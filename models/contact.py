from models.person_name import PersonName
from models.address import Address
from models.contact_info import ContactInfo


class Contact(object):

    db_cols = [
        'last_name', 'first_name', 'middle_name', 'name_suffix',
        'nickname', 'last_name_meta', 'first_name_meta', 'nickname_meta',
        'birth_year', 'gender', 'email', 'phone1', 'phone2',
        'house_number', 'pre_direction', 'street_name', 'street_type',
        'suf_direction', 'unit', 'street_name_meta', 'city', 'zipcode',
        'precinct_id', 'voter_id', 'reg_date'
    ]

    def __init__(self, d=None):
        self.id = None
        self.name = None
        self.birth_year = None
        self.gender = ''
        self.info = None
        self.address = None
        self.voter_id = None
        self.reg_date = ''
        if d:
            for attr in self.__dict__:
                if attr in d:
                    setattr(self, attr, d[attr])
            self.name = PersonName(d)
            self.address = Address(d)
            self.info = ContactInfo(d)

    def __str__(self):
        return str(self.name)

    def serialize(self):
        return {
            'name': self.name.serialize(),
            'whole_name': str(self.name),
            'birth_year': self.birth_year,
            'gender': self.gender,
            'contact': self.info.serialize(),
            'address': self.address.serialize(),
            'voter_id': self.voter_id,
            'reg_date': self.reg_date,
            'id': self.id,
        }

    def get_values(self):
        return (
            self.name.last,
            self.name.first,
            self.name.middle,
            self.name.suffix,
            self.name.nickname,
            self.name.last_meta,
            self.name.first_meta,
            self.name.nickname_meta,
            self.birth_year,
            self.gender,
            self.info.email,
            self.info.phone1,
            self.info.phone2,
            self.address.house_number,
            self.address.pre_direction,
            self.address.street_name,
            self.address.street_type,
            self.address.suf_direction,
            self.address.unit,
            self.address.metaphone,
            self.address.city,
            self.address.zipcode,
            self.address.precinct_id,
            self.voter_id,
            self.reg_date
        )
