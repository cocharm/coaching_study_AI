file_path = "data-01-test-score.csv"


def read_file():
    f = open(file_path, 'r')
    # EOF가 나오기 전까지 전부 받음
    lines = f.readlines()
    return [line.strip().split(',') for line in lines]

print(read_file())