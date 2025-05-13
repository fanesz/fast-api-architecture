import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
    
from app.backend import run_app

if __name__ == "__main__":
    run_app()