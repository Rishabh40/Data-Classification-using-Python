import csv
import re
import shutil
import os
import datetime

# Rishabh Agarwal
# 1801EE40


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if os.path.isdir('./analytics'):
        shutil.rmtree(
            './analytics')
    os.mkdir('./analytics')
    pass


def date_validation(day, month, year):
    isValidDate = True
    try:
        datetime.datetime(int(year),
                          int(month), int(day))
    except ValueError:
        isValidDate = False
    if year < 1995 or year > 2020:
        isValidDate = False
    return isValidDate


def course():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/course'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'course')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'course')
        os.mkdir(final_path)
    path = './analytics/course'
    with open('studentinfo.csv', 'r') as file:
        data = csv.DictReader(file)
        misc = []
        header = ['id', 'full_name', 'country', 'email',
                  'gender', 'dob', 'blood_group', 'state']
        program_code = {'01': "btech", '11': "mtech", '12': "msc", '21': "phd"}
        roll_number = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')

        for row in data:
            roll_no = row['id']
            if not re.match(roll_number, roll_no):
                misc.append(row)
            else:
                year_of_admission = roll_no[0:2]
                course = program_code[roll_no[2:4]]
                branch = (roll_no[4:6]).lower()

                path1 = path
                path1 += "\\"+branch
                if not os.path.isdir(path1):
                    os.mkdir(path1)

                path1 += "\\"+course
                if not os.path.isdir(path1):
                    os.mkdir(path1)

                info_file = path1 + "\\" + year_of_admission + \
                    '_' + branch + '_' + course + ".csv"

                if not os.path.isfile(info_file):
                    with open(info_file, 'a', newline='') as file:
                        data = csv.DictWriter(file, fieldnames=header)
                        data.writeheader()

                with open(info_file, 'a', newline='') as file:
                    data = csv.DictWriter(file, fieldnames=header)
                    data.writerow(row)

        path += '\misc.csv'
        with open(path, 'a', newline='') as file:
            data = csv.DictWriter(file, fieldnames=header)
            data.writeheader()
            data.writerows(misc)
    pass


def country():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/country'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'country')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'country')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        pattern = re.compile(r'^$')
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                if not re.match(pattern, row[2]):
                    country_path = os.path.join(
                        './analytics/country', row[2]+'.csv')
                    if not os.path.isfile(country_path):
                        with open(country_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(country_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
                else:
                    country_path = os.path.join(
                        './analytics/country', 'misc.csv')
                    if not os.path.isfile(country_path):
                        with open(country_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(country_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


def email_domain_extract():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/email_domain'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'email_domain')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'email_domain')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        pattern = re.compile(
            r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$')
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                if re.match(pattern, row[3]):
                    temp = row[3][row[3].index('@')+1:]
                    domain = temp[:temp.index('.')]
                    domain_path = os.path.join(
                        './analytics/email_domain', domain+'.csv')
                    if not os.path.isfile(domain_path):
                        with open(domain_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(domain_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
                else:
                    domain_path = os.path.join(
                        './analytics/email_domain', 'misc.csv')
                    if not os.path.isfile(domain_path):
                        with open(domain_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(domain_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


def gender():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/gender'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'gender')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'gender')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "gender":
                with open('./analytics/gender/female.csv', 'a', newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
                with open('./analytics/gender/male.csv', 'a', newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
            elif row[4] == "Female":
                with open('./analytics/gender/female.csv', 'a', newline='') as female:
                    writer = csv.writer(female)
                    writer.writerow(row)
            elif row[4] == "Male":
                with open('./analytics/gender/male.csv', 'a', newline='') as male:
                    writer = csv.writer(male)
                    writer.writerow(row)
            else:
                with open('./analytics/gender/misc.csv', 'a', newline='') as misc:
                    writer = csv.writer(misc)
                    writer.writerow(row)
    pass


def dob():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/dob'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'dob')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'dob')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                pattern = row[5].split('-')
                day = int(pattern[0])
                month = int(pattern[1])
                year = int(pattern[2])
                if date_validation(day, month, year):
                    range1_path = os.path.join(
                        './analytics/dob', 'bday_1995_1999.csv')
                    range2_path = os.path.join(
                        './analytics/dob', 'bday_2000_2004.csv')
                    range3_path = os.path.join(
                        './analytics/dob', 'bday_2005_2009.csv')
                    range4_path = os.path.join(
                        './analytics/dob', 'bday_2010_2014.csv')
                    range5_path = os.path.join(
                        './analytics/dob', 'bday_2015_2020.csv')
                    if year >= 1995 and year <= 1999:
                        if not os.path.isfile(range1_path):
                            with open(range1_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range1_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2000 and year <= 2004:
                        if not os.path.isfile(range2_path):
                            with open(range2_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range2_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2005 and year <= 2009:
                        if not os.path.isfile(range3_path):
                            with open(range3_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range3_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2010 and year <= 2014:
                        if not os.path.isfile(range4_path):
                            with open(range4_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range4_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                    if year >= 2015 and year <= 2020:
                        if not os.path.isfile(range5_path):
                            with open(range5_path, 'a', newline='') as file:
                                head = csv.writer(file)
                                head.writerow(header)
                        with open(range5_path, 'a', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(row)
                else:
                    mics_path = os.path.join(
                        './analytics/dob', 'misc.csv')
                    if not os.path.isfile(mics_path):
                        with open(mics_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(mics_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


def state():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/state'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'state')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'state')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        pattern = re.compile(r'^$')
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                if not re.match(pattern, row[7]):
                    state_path = os.path.join(
                        './analytics/state', row[7]+'.csv')
                    if not os.path.isfile(state_path):
                        with open(state_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(state_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
                else:
                    state_path = os.path.join(
                        './analytics/state', 'mics.csv')
                    if not os.path.isfile(state_path):
                        with open(state_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(state_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


def blood_group():
    # Read csv and process
    path = './analytics'
    if os.path.isdir(path):
        spe_path = './analytics/blood_group'
        if os.path.isdir(spe_path):
            shutil.rmtree(spe_path)
        curr_path = os.path.join(path, 'blood_group')
        os.mkdir(curr_path)
    else:
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
        final_path = os.path.join(curr_path, 'blood_group')
        os.mkdir(final_path)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        pattern = re.compile(r'^(A|B|AB|O)[+-]$', re.IGNORECASE)
        for row in reader:
            if(row[0] == 'id'):
                header = row
            else:
                if re.match(pattern, row[6]):
                    blood_path = os.path.join(
                        './analytics/blood_group', row[6].lower()+'.csv')
                    if not os.path.isfile(blood_path):
                        with open(blood_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(blood_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
                else:
                    blood_path = os.path.join(
                        './analytics/blood_group', 'misc.csv')
                    if not os.path.isfile(blood_path):
                        with open(blood_path, 'a', newline='') as file:
                            head = csv.writer(file)
                            head.writerow(header)
                    with open(blood_path, 'a', newline='') as file:
                        data = csv.writer(file)
                        data.writerow(row)
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    path = './analytics'
    if not os.path.isdir(path):
        parent_dir = '.'
        curr_path = os.path.join(parent_dir, 'analytics')
        os.mkdir(curr_path)
    temp = ['id', 'first_name', 'last_name', 'country',
            'email', 'gender', 'dob', 'blood_group', 'state']
    header = temp
    with open('./analytics/studentinfo_names_split.csv', 'a', newline='') as file:
        head = csv.writer(file)
        head.writerow(temp)
    with open('./studentinfo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != 'id':
                name_split = row[1].split(' ')
                first_name = name_split[0]
                l_name = name_split[1:]
                last_name = ''
                for name in l_name:
                    last_name += name+' '
                temp = [row[0], first_name, last_name, row[2],
                        row[3], row[4], row[5], row[6], row[7]]
                with open('./analytics/studentinfo_names_split.csv', 'a', newline='') as file:
                    head = csv.writer(file)
                    head.writerow(temp)
    unsorted_list = []
    with open('./analytics/studentinfo_names_split.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] != 'id'):
                unsorted_list.append(row)
    with open('./analytics/studentinfo_names_split_sorted_first_name.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    sorted_list = sorted(unsorted_list, key=lambda l: l[1])
    with open('./analytics/studentinfo_names_split_sorted_first_name.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for row in sorted_list:
            writer.writerow(row)
    pass
