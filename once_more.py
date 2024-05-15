import pickle
import json
import gzip

import datetime
from collections import deque

# task = {
#     "id": 1,
#     "author_id": 2,
#     "approved": True,
#     "created_at": datetime.datetime.today(),
#     "assignee": deque([3, 12, 7])
# }

# tasks = [task for _ in range(100000)]

# fp = open('serial_raw', 'w')
# fp.write(str(tasks))
# fp.close()


# class Encoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, datetime.datetime):
#             return str(o)
#         if isinstance(o, deque):
#             return list(o)
#         return super().default(o)
    

# fp = open('serial_json.json', 'w')
# json.dump(tasks, fp, cls=Encoder)
# fp.close()

# самый минимальный объем дает
# fp = open('serial_pkl.pkl', 'wb')
# pickled_ = pickle.dumps(tasks)
# compressed_ = gzip.compress(pickled_)
# fp.write(compressed_)
# fp.close()


fp = open('serial_pkl.pkl', 'rb')
raw_data = gzip.decompress(fp.read())
data = pickle.loads(raw_data)
print(data[0])

