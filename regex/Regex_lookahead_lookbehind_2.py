#Code Adhyayana
import re
data = "Thank%%%%you$$$$all !!!!!!"

pattern1 = re.compile(r"(?<=[A-Za-z])[\s!@#$%&]+(?=[A-Za-z])")

print(pattern1.findall(data))
new_data = pattern1.sub(' ', data)
print(new_data)