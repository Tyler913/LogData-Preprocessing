import csv

def separate(file_path, date, time, PID_name, process, sign, temp):
    order = [date, time, PID_name, process, sign, temp]
    with open(file_path, 'r') as file:
        line = file.readline()
        while line != '':
            start = 0
            end = 0
            flag = 0
            for i in range(len(line)):
                if line[i] == ' ':
                    end = i
                    order[flag%6].append(line[start:end])
                    start = end + 1
                    flag += 1
                    if flag == 5:
                        temp.append(line[start:])
                        break
            line = file.readline()
    return date, time, PID_name, process, sign, temp

date = []
time = []
PID_num = []
process = []
sign = []
name = []
info = []
temp = []

date, time, PID_num, process, sign, temp = separate("/Users/tyler/Desktop/Development/smart/haveATry.txt", date, time, PID_num, process, sign, temp)
# print(temp)

def temp_to_info_name(temp, name, info):
    for i in range(len(temp)):
        length = len(temp[i])
        for j in range(length):
            if temp[i][j] == ':':
                name.append(temp[i][0:j])
                info.append(temp[i][j+2:len(temp[i])])
                break
    return name, info

name, info = temp_to_info_name(temp, name, info)

# print(info)

def delete_newline(info):
    for i in range(len(info)):
        for j in range(len(info[i])):
            if info[i][j] == '\n':
                info[i] = info[i][0:j]
                break
    return info

info = delete_newline(info)
# print(info)

def arrays_to_csv(file_path, arrays):
    # 使用zip函数将数组按列对齐
    rows = zip(*arrays)

    # 打开CSV文件并准备写入
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # 写入每行数据
        for row in rows:
            writer.writerow(row)


# 要保存为CSV的数组列表
arrays = [date, time, PID_num, process, sign, name, info]

# 将数组保存为CSV文件
arrays_to_csv('/Users/tyler/Desktop/Development/smart/finalCSV.csv', arrays)