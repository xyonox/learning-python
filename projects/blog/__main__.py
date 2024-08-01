from src import setup
from src.user import User

if __name__ == "__main__":

    #testing == fun?
    setup.init()
    User.create("xyonox2", "ichbinschlaui2")
    print(User.exists("xyonox"))