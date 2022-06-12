import application.salary
import application.db.people
import datetime
from dirty_main import *

def main():
    print(datetime.datetime.now())
    application.salary.calculate_salary()
    dirty_main()

if __name__ == '__main__':
    main()
