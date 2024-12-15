import sys
sys.dont_write_bytecode = True
from app.app import Application

if __name__ == "__main__":
    Application().run()