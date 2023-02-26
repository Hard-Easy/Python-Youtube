#Code Adhyayana

import re
data = "John Doe LNU"

pattern1 = re.compile(r"(?<=John).+(?=LNU)")

print(pattern1.findall(data))
new_data = pattern1.sub(' ', data)
print(new_data)