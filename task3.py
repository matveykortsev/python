class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, worker_income):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income = worker_income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


worker = Position('Matvey', 'Kortsev', 'Lead system engineer', {"wage": 2400, "bonus": 500})
print(f'Worker: {worker.get_full_name()}\nTotal income: {worker.get_total_income()}')
print(worker.name)
