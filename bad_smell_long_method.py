csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users():
    data = _read(csv)
    data = _sort(data)
    return _filter(data)


def _read(csv):
    return [user.split(';') for user in csv.split('\n')]


def _sort(data):
    return sorted(data, key=lambda user: int(user[1]))


def _filter(data):
    return [user for user in data if int(user[1]) > 10]

if __name__ == "__main__":
    print(get_users())