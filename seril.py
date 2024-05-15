# pickle - выгружаем в бинарный вид (уменьш размер массива данных)

import pickle
import datetime
from collections import deque

task = {
    "id": 1,
    "author_id": 2,
    "approved": True,
    "created_at": datetime.datetime.today(),
    "assignee": deque([3, 12, 7])
}

# 1 способ сериализации (перевода в бинарный вид, маршаллинг)
pickeled_ = pickle.dumps(task)
print(pickeled_)

# не использовали энкодеров для deque и datetime


# 2 способ сериализации (перевода в бинарный вид, маршаллинг)
f = open('task.pkl', 'wb')
# wb - бинарная запись
pickeled_ = pickle.dump(task, f)
f.close()


# 1 способ десериализации (восстановление из бинарного вида)
f = open('task.pkl', 'rb')
task = pickle.load(f)
f.close()
print(task)