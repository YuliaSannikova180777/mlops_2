import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

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
        arr_age.append(line[3])
        arr_education.append(line[4])
        arr_marital_status.append(line[5])

    for i in range(len(arr_sex)):
        if arr_sex[i] == 'Male':
            arr_sex[i] = 1
        else:
            arr_sex[i] = 0

    for p_education_num, p_capital_gain, p_sex, p_age, p_education, p_marital_status in zip(arr_education_num, arr_capital_gain, arr_sex, arr_age, arr_education, arr_marital_status):
        fd_out.write("{},{},{},{},{},{}\n".format(p_education_num, p_capital_gain, p_sex, p_age, p_education, p_marital_status))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
