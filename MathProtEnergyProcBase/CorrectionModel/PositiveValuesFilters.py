import numpy as np

from MathProtEnergyProcBase.CorrectionModel.HelpFunctions import ScaleFun


# Положительность велиин
def ReluFilter(x):
    ax = np.abs(x)  # Модуль аргументов

    # Обнуление отрицательных аргументов и вывод результата
    return (x + ax) / 2


# Линейный в положительной области фильтр
def PosLinearFilter(x, lam=1000, xmin=0, scy=1):
    # Рассчитываем составляющие
    ax = np.abs(x)  # Модуль аргументов
    px = (ax + x) / 2  # Обнуление отрицательных аргументов

    # Получаем и возвращаем результат
    rez = np.log(1 + np.exp(-lam * ax)) / lam + px
    return ScaleFun(xmin, scy, rez)


# Экспоннциальный фильтр
def ExpFilter(x, lam=0.1, xmin=0, scy=1):
    # Получаем и возвращаем результат
    rez = np.exp(lam * x)
    return ScaleFun(xmin, scy, rez)
