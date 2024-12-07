import numpy as np
import cv2
import tensorflow as tf
from PySpice.Spice.Netlist import Circuit
import sys
import os

def main():
    print("NumPy version:", np.__version__)
    print("OpenCV version:", cv2.__version__)
    print("TensorFlow version:", tf.__version__)
    
    # Test PySpice
    circuit = Circuit('Test Circuit')
    print("PySpice Circuit created successfully")
    
    # Test PyQt6 (only if not running in a headless environment)
    if 'linux' in sys.platform and not os.environ.get('DISPLAY'):
        print("Skipping PyQt6 test (no display detected)")
    else:
        try:
            from PyQt6.QtWidgets import QApplication, QLabel
            app = QApplication([])
            label = QLabel("Hello, World!")
            print("PyQt6 label created successfully")
        except Exception as e:
            print(f"Error creating PyQt6 label: {e}")

if __name__ == "__main__":
    main()