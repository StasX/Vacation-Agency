from utils.dal import DAL
from utils.image_handler import ImageHandler
from models.vacation_model import VacationModel


class VacationsLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self, user_id):
        sql = "CALL get_all_vacations(%s)"
        params = (user_id, )
        return self.dal.get_table(sql, params)
    
    def get_one_vacation(self, id):
        sql = """SELECT vacation_id AS id, C.country as country, C.country_id AS country_id, description, start_date, end_date,price, image FROM vacations AS V JOIN countries AS C ON V.country_id = C.country_id WHERE V.vacation_id = %s ORDER BY start_date"""
        result = self.dal.get_scalar(sql, (id,))
        return result

    def add_vacation(self, vacation):
        # Add image
        image_name = ImageHandler.save_image(vacation.image)
        # Add vacation
        sql = "CALL add_vacation(%s,%s,%s,%s,%s,%s)"
        params = (vacation.country, vacation.description, vacation.start_date,
                  vacation.end_date, vacation.price, image_name)
        last_row_id = self.dal.insert(sql, params)

    def update_vacation(self, vacation):
        # Update image
        old_image = self.get_old_image_name(vacation.id)
        image_name = ImageHandler.update_image(old_image,vacation.image)
        # Update vacation
        sql = "CALL update_vacation(%s,%s,%s,%s,%s,%s,%s)"
        params = (vacation.id, vacation.country, vacation.description,
                  vacation.start_date, vacation.end_date, vacation.price, image_name)
        row_count = self.dal.update(sql, params)

    def delete_vacation(self, id):
        # Delete image
        old_image = self.get_old_image_name(id)
        ImageHandler.delete_image(old_image)
        # Delete vacation
        sql = "CALL remove_vacation(%s)"
        params = (id,)
        row_count = self.dal.delete(sql, params)

    def get_old_image_name(self,id):
        sql = "SELECT image FROM vacations WHERE vacation_id=%s"
        params = (id,)
        old_image_name=self.dal.get_scalar(sql,params)
        return old_image_name["image"]


    def close(self):
        self.dal.close()
