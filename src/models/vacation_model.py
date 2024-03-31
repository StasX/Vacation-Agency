from utils.date_handler import DateHandler


class VacationModel:
    def __init__(self, id, country, description, start_date, end_date, price, image):
        self.id = id
        self.country = country
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.image = image

    def validate_insert(self):
        if not self.country:
            return "Country not set."
        if not self.description:
            return "Missing description."
        if not self.start_date:
            return "Missing start date."
        if not self.end_date:
            return "Missing end date."
        if not self.price:
            return "Missing price."
        if not self.image:
            return "Missing image."

        if not (isinstance(self.country, str) and self.country.isnumeric()):
            return "Country is invalid"
        if len(self.description) == 0:
            return "Description can't be empty"
        if DateHandler.to_date(self.start_date) <= DateHandler.now():
            return "Start of vacation should be in future"
        if DateHandler.to_date(self.start_date) > DateHandler.to_date(self.end_date):
            return "Start of vacation can't be before vacation end"
        if not 0 <= float(self.price) <= 10000:
            return "Price is invalid."
        return None

    def validate_update(self):
        if not self.country:
            return "Country not set."
        if not self.description:
            return "Missing description."
        if not self.start_date:
            return "Missing start date."
        if not self.end_date:
            return "Missing end date."
        if not self.price:
            return "Missing price."
        
        if not self.country.isnumeric():
            return "Country is invalid"
        if len(self.description) == 0:
            return "Description can't be empty"
        if DateHandler.to_date(self.start_date) > DateHandler.to_date(self.end_date):
            return "Start of vacation can't be before vacation end"
        if not 0 <= float(self.price) <= 10000:
            return "Price is invalid."
        return None

