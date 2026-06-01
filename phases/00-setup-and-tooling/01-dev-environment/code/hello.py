# Lesson: Dev Environment (phase 00 / lesson 01)
# Path: phases/00-setup-and-tooling/01-dev-environment/docs/en.md
# Description: Python Hello World demonstrating runtime and PyTorch library availability.

import sys
import numpy as np
import torch

def main():
    print("Hello World from Python!")
    print(f"Python Version: {sys.version}")
    print(f"NumPy version: {np.__version__}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device Name: {torch.cuda.get_device_name(0)}")

if __name__ == "__main__":
    main()
