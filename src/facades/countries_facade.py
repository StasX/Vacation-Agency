from logic.countries_logic import CountriesLogic
class CountriesFacade:
    def __init__(self):
        self.logic = CountriesLogic()
    def get_all_countries(self):
        return self.logic.get_all_countries()