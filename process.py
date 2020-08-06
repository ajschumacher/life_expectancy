"""`bltper_5x10.txt` -> `data.csv`"""

import csv


input_filename = 'bltper_5x10.txt'

with open(input_filename) as f:
    lines = [line for line in f]

lines = lines[2:]  # drop preamble (Sweden, etc.)
lines = [line.strip().split() for line in lines]
assert all(len(line) == 10 for line in lines)

header = lines.pop(0)
assert len(lines) == 648  # 24 rows for each of 27 periods

death = {}
for line in lines:
    year = death.setdefault(line[header.index('Year')], {})
    year[line[header.index('Age')]] = int(line[header.index('dx')])

sums = {year: sum(ages.values()) for year, ages in death.items()}
assert min(sums.values()) == 99997
assert max(sums.values()) == 100001
# Must be due to rounding to get integer values (after modeling)...

for year, ages in death.items():
    ages['0-4'] = ages['0'] + ages['1-4']
    del ages['0']
    del ages['1-4']

age_keys = sorted(death['1751-1759'].keys(),
                  key=lambda x: int(x.split('-')[0][:3]))
year_keys = sorted(death.keys())

data = []
for age_key in reversed(age_keys):
    age_data = ['ages ' + age_key]
    for year_key in year_keys:
        age_data.append(death[year_key][age_key] / float(sums[year_key]))
    data.append(age_data)

data.append(['Years'] + year_keys)

exps = [line[header.index('ex')] for line in lines
        if line[header.index('Age')] == '0']
data.append(['Life expectancy at 0'] + exps)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
