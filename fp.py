# serilize

import json
import datetime
from collections import deque

# fp = open('w.json')
# content = fp.read()
# content = json.loads(content)

# f = open('w.json')
# content = json.load(f)
# f.close()
# print(content)


task = {
    "id": 1,
    "author_id": 2,
    "approved": True,
    "created_at": datetime.datetime.today(),
    "assignee": deque([3, 12, 7])
}
# serialized = json.dumps(task)
# print(serialized)



# для обработки datetime
# для обработки deque
class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        if isinstance(o, deque):
            return list(o)
        return super().default(o)


fp = open('new.json', 'w')
json.dump(task, fp, indent=4, cls=Encoder)
fp.close()


