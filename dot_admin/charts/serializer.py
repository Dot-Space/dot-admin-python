from abc import ABC
import seaborn as sns


class BaseChartSerializer(ABC):
    """
    Базовый сериализатор для графиков
    """
    name: str
    chart: dict

    def __init__(self, chart, name):
        self.chart = chart
        self.name = name

    def to_json(self):
        return {
            'name': self.name,
            'chart': self.chart
        }

    def to_image(self):
        pass

    def to_html(self):
        pass


