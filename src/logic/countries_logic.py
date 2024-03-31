from utils.dal import DAL

class CountriesLogic:
    def __init__(self):
        self.dal=DAL()
    def get_all_countries(self):
        return self.dal.get_table("SELECT * FROM countries")