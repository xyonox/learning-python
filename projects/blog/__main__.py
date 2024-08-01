from src import setup
from src.blog import Blog
from src.user import User

if __name__ == "__main__":

    #testing == fun?
    setup.init()
    User.create("xyonox2", "ichbinschlaui2")
    print(User.exists("xyonox"))

    Blog.create("xyonox", "Python lernen", "ich lerne hier py\n"
                                           "du?\n"
                                           "nein? weg mit dir D:")