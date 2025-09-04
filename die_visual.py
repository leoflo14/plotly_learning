from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = [die.roll() for _ in range(1000)]

# Анализ результатов.
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Визуализация результатов.
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequencs of Result"}
my_layout = Layout(
    title="Results of rolling one D6 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
