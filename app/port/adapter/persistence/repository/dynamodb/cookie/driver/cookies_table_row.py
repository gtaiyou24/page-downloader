from pynamodb.attributes import UnicodeAttribute, JSONAttribute
from pynamodb.models import Model


class CookiesTableRow(Model):
    class Meta:
        table_name = 'cookies'
        region = 'ap-northeast-1'
        read_capacity_units = 1
        write_capacity_units = 1

    cookie_id = UnicodeAttribute(hash_key=True)
    contents = JSONAttribute()
