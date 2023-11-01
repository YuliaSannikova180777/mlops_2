import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        p_education_num = line[1]
        p_capital_gain = line[2]
        if line[3][0] == '"':
            p_sex = line[5]
            p_age = line[6]
            p_education = line[3]
            p_marital_status = line[7]
        else:
            p_sex = line[4]
            p_age = line[5]
            p_education = line[2]
            p_marital_status = line[6]
        fd_out.write("{},{},{},{},{},{}\n".format(p_education_num, p_capital_gain, p_sex, p_age, p_education, p_marital_status))

with open(f_input, encoding="utf8") as fd_in:
    with open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
