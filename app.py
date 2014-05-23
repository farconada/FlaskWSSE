import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
from application import app


if __name__ == '__main__':
    app.run()
