#!/usr/bin/env python3
import skilstak.colors as c

import json
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)

print(jsonToPython)
