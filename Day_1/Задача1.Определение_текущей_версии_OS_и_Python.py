# Задача1. Определение текущей версии OS и Python.

# Напишите программу Python, чтобы получить версию Python, которую вы испольуете.

import sys
import platform

print("На данном устройстве c операционной системой", platform.platform(),
    "\nустановлен Python версии {}.{}.{}.".format(sys.version_info.major,
        sys.version_info.minor, sys.version_info.micro))
