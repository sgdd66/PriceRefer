#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Kriging 模型，用于数据拟合"""


import numpy as np
import KrigingPackage.ADE as ADE
import matplotlib.pyplot as plt
import KrigingPackage.DOE as DOE
import mayavi.mlab as mlab
import os
os.environ['QT_API']='pyside'