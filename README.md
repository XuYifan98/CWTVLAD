# CWTVLAD for Visual Place Recognition

## Introduction
`CWTVLAD` is a PyTorch implementation for our TMM paper "CWTVLAD: Multi-Scale Clustering-based ...".

## Installation
We test this repo with Python 3.8, PyTorch 1.9.0, and CUDA 11.1. However, it should be runnable with recent PyTorch versions (Pytorch >= 1.1.0).
```shell
python setup.py develop
```
In addition, need to install KNN_CUDA from wheel.
```shell
pip install --upgrade https://github.com/unlimblue/KNN_CUDA/releases/download/0.2/KNN_CUDA-0.2-py3-none-any.whl
```
