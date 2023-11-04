import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_education_num = []
    arr_capital_gain = []
    arr_sex = []
    arr_age = []
    arr_education = []
    arr_marital_status = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_education_num.append(line[0])
        arr_capital_gain.append(line[1])
        arr_sex.append(line[2])
        if line[3].isdigit():
            arr_age.append(float(line[3]))
        else:
            arr_age.append(0)
        arr_education.append(line[4])
        arr_marital_status.append(line[5])

    age_sum = sum(arr_age)
    age_count = len([age for age in arr_age if age > 0])
    average_age = age_sum / age_count if age_count > 0 else 0

    for i in range(len(arr_age)):
        if arr_age[i] == 0:
            arr_age[i] = round(average_age, 2)

    for p_education_num, p_capital_gain, p_sex, p_age, p_education, p_marital_status in zip(arr_education_num, arr_capital_gain, arr_sex, arr_age, arr_education, arr_marital_status):
        fd_out.write("{},{},{},{},{},{}\n".format(p_education_num, p_capital_gain, p_sex, p_age, p_education, p_marital_status))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
