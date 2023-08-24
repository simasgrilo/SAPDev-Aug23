
from requisition import Requisition
from SAPDevTask3 import TaskThree

class Main:

    @staticmethod
    def main():
        req = Requisition()
        print(req.getHash('this-is-the-year-of-the-api'))
        #print(req.getHash("hello"))

        #task3
        task_three = TaskThree()
        print(task_three.getHashForProducts())



if __name__ == "__main__":

    Main.main()