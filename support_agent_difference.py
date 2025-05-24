# -*- coding: utf-8 -*-
"""Support Agent Difference

Original file is located at
    https://colab.research.google.com/drive/1FLSNOys1ZljpNsNBMHPkk_L38Llf-ECa
"""

import pandas as pd

df = pd.read_csv('Project.csv')

df.info()

df.groupby(['support_agent_experience'])['satisfaction_score'].mean()

df.groupby(['support_agent_experience'])['resolution_time_days'].mean()
