from distutils.core import setup

# Функция установки
setup(name="MathProtEnergyProcBase",
      version="1.0",
      author="Igor Starostin",
      author_email="starostinigo@yandex.ru",
      description="System modeling by mathematical prototiping method base functional",
      packages=["MathProtEnergyProcBase",
                "MathProtEnergyProcBase.CorrectionModel",
                "MathProtEnergyProcBase.CorrectionModel.KineticMatrix",
                "MathProtEnergyProcBase.HeatPowerValues",
                "MathProtEnergyProcBase.HeatPowerValues.Base",
                "MathProtEnergyProcBase.HeatPowerValues.Output",
                "MathProtEnergyProcBase.NonEqProcess",
                "MathProtEnergyProcBase.tests",
                "MathProtEnergyProcBase.tests.UnitTestExamples"],
      scripts=["testMathProtEnergyProcBase.py"]
      )
