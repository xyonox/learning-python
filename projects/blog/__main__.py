from src import setup
from src.user import user

if __name__ == "__main__":
    setup.init()
    user.create("xyonox2", "ichbinschlaui2")
    print(user.exists("xyonox"))