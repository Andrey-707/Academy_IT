# Модуль инициализации. Для тестирования пакета модулей в списке __all__ отключена функция square_area.

from .circle import circle_perimeter, circle_area
from .triangle import triangle_perimeter, triangle_area
from .square import square_perimeter, square_area


__all__ = [
	"circle_perimeter",
	"triangle_perimeter",
	"square_perimeter",
	"circle_area",
	"triangle_area"
	]
