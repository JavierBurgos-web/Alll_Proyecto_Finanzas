# Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargando datos
expuestos = pd.read_csv('https://raw.githubusercontent.com/JavierBurgos-web/Alll_Proyecto_Finanzas/main/2_data/BD_Expuestos.txt', sep='\t')
sociodemograficos = pd.read_csv('https://raw.githubusercontent.com/JavierBurgos-web/Alll_Proyecto_Finanzas/main/2_data/BD_Sociodemograficas.txt', sep='\t')
siniestros = pd.read_csv('https://media.githubusercontent.com/media/JavierBurgos-web/Alll_Proyecto_Finanzas/main/2_data/DB_Siniestros.txt', sep=',')
