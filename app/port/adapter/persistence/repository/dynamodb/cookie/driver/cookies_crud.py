from port.adapter.persistence.repository.dynamodb.cookie.driver import CookiesTableRow


class CookiesCrud:
    def __init__(self):
        if not CookiesTableRow.exists():
            CookiesTableRow.create_table()
