'laba3'

# '1'
# def reader(file, type_of_reading):
#     with open(file, 'r') as f:
#         if type_of_reading == 'full':
#             print(f.read())
#         elif type_of_reading == 'line':
#             for line in f:
#                 print(line)
#
# reader('example.txt', 'line')


# '2'
# def fl(file):
#     with open(file, 'a+') as f:
#         line = input()
#         f.write(line + '\n')
#         f.seek(0)
#         print(f.read())
#
#
# fl('user_input.txt')


'3'
def reader(file, type_of_reading):
    try:
        with open(file, 'r') as f:
            if type_of_reading == 'full':
                print(f.read())
            elif type_of_reading == 'line':
                for line in f:
                    print(line, end='')
    except FileNotFoundError:
        print('Такого файла не существует')
        exit()


reader('example.txt', 'line')

