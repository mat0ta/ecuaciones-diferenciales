from modules import edo
from totareadme import readme
import os

if __name__ == "__main__":
    actual_path = os.path.dirname(os.path.abspath(__file__))
    readme(str(actual_path))
    edo.EDO.e1()
    edo.EDO.e2()
    edo.EDO.e3()
    edo.EDO.e4()