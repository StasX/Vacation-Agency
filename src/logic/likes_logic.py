from utils.dal import DAL

class LikesLogic:
    def __init__(self):
        self.dal = DAL()

    def like(self, user_id, vacation_id):
        sql = "CALL like_vacation(%s,%s)"
        params = (user_id, vacation_id)
        return self.dal.insert(sql, params)