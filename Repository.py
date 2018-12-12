from domain.Base import Session

class Repository():
    #db_string = "postgresql://localhost:5432/postgres?user=postgres&password=Bjk165165!*"

    def __init__(self, domainClass):
        self.session = Session()
        self.domain = domainClass

    def get_all(self, join_query=None):
        customers = self.session.query(self.domain)
        if join_query is not None:
           customers = customers.join(join_query)

        return customers

    def filter(self, query):
        customers = self.session.query(self.domain).filter(query)
        return customers