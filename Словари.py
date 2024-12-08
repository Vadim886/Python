# Вариант 5
# Задание 1
'''pred = [
    ["Лента", 100000, 85000],
    ["Слата", 150000, 160000],
    ["Пятерочка", 200000, 170000],
    ["Удача", 120000, 108000],
]

x_count = 0

for name, planned, actual in pred:
    y = (actual / planned) * 100
    print(f"{name}:{y:.2f}% выполнения плана")

    if actual < planned * 0.9:
        x_count += 1

print(f"Количество предприятий, недовыполнивших план на 10% и более: {x_count}")'''

#Задание 1(2 вариант)
'''class Enterprise:
    def __init__(self, name, planned_turnover, actual_turnover):
        self.name = name
        self.planned_turnover = planned_turnover
        self.actual_turnover = actual_turnover

    def performance_percentage(self):
        return (self.actual_turnover / self.planned_turnover) * 100

def main():
    enterprises = []
    num_enterprises = int(input("Введите количество предприятий: "))

    for _ in range(num_enterprises):
        name = input("Введите название предприятия: ")
        planned_turnover = float(input("Введите плановый объем розничного товарооборота: "))
        actual_turnover = float(input("Введите фактический объем розничного товарооборота: "))
        enterprises.append(Enterprise(name, planned_turnover, actual_turnover))

    underperforming_count = 0

    for enterprise in enterprises:
        percentage = enterprise.performance_percentage()
        print(f"{enterprise.name}: {percentage:.2f}% выполнения плана")
        if enterprise.actual_turnover < 0.9 * enterprise.planned_turnover:
            underperforming_count += 1

    print(f"Количество предприятий, недовыполнивших план на 10% и более: {underperforming_count}")

if __name__ == "__main__":
    main()'''

# Задача 2

'''def main():
    num_lines = int(input())
    word_count = {}

    for _ in range(num_lines):
        line = input().strip()
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    sorted_words = [(count, word) for word, count in word_count.items()]

    sorted_words.sort(key=lambda x: (-x[0], x[1]))

    for count, word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()'''


