from utils.date_handler import DateHandler
class Logger:
    __path="./crashes.log"
    @staticmethod
    def write_log(message):
        with open(Logger.__path,"a") as file:
            file.write(str(DateHandler.now())+":\n")
            file.write(str(message)+"\n")
            file.write("-----------------------------------------------------------------------------------\n")