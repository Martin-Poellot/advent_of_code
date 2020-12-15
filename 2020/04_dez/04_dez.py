import re
import time
passports = []
with open("04_dez_input.txt", 'r') as f:
    lines = f.readlines()
    new_passport = ""
    for line in lines:
        if line == "\n":
            passports.append(new_passport)
            new_passport = ""
        else:
            contents = line.split("\n")[0]
            new_passport += f'{contents} '
    passports.append(new_passport)


passports_list = []
for passport in passports:
    entries = passport.split(' ')
    pp = {}
    for entry in entries[:-1]:
        idf, content = entry.split(':')
        pp[idf] = content
    passports_list.append(pp)

start_1 = time.time()
valid = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for pp in passports_list:
    something_missing = False
    for req_field in required_fields:
        if req_field not in pp.keys():
            something_missing = True
            break
    if not something_missing:
        valid += 1

elapsed1 = time.time() - start_1
print(f'Result 1: {valid}')
print(f'Elapsed Time: {elapsed1:.6f}s')

start_2 = time.time()
valid = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for pp in passports_list:
    something_missing = False
    for req_field in required_fields:
        if req_field not in pp.keys():
            something_missing = True
            break
        if req_field == 'byr':
            if not 1920 <= int(pp[req_field]) <= 2002:
                something_missing = True
                break
        elif req_field == 'iyr':
            if not 2010 <= int(pp[req_field]) <= 2020:
                something_missing = True
                break
        elif req_field == 'eyr':
            if not 2020 <= int(pp[req_field]) <= 2030:
                something_missing = True
                break
        elif req_field == 'hgt':
            if 'cm' in pp[req_field]:
                if not 150 <= int(pp[req_field].split('cm')[0]) <= 193:
                    something_missing = True
                    break
            elif 'in' in pp[req_field]:
                if not 59 <= int(pp[req_field].split('in')[0]) <= 76:
                    something_missing = True
                    break
            else:
                something_missing = True
                break
        elif req_field == 'hcl':
            regex_res = re.match('^#[0-9a-f]{6}$', pp[req_field])
            if not regex_res:
                something_missing = True
                break
        elif req_field == 'ecl':
            if pp[req_field] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                something_missing = True
                break
        elif req_field == 'pid':
            regex_res = re.match('^[0-9]{9}$', pp['pid'])
            if not regex_res:
                something_missing = True
                break
    if not something_missing:
        valid += 1
elapsed2 = time.time() - start_2
print(f'Result 2: {len(passports_list)}')
print(f'Elapsed Time: {elapsed2:.6f}s')
