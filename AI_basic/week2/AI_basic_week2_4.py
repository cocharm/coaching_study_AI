class ReadCSV():
    def __init__(self, file_path) :
        self.file_path = file_path
        # merge_list에서 self.lines 없어서 오류 뜨는 것 방지
        self.lines = []

    def read_file(self):
        f = open(self.file_path, 'r')
		    # EOF가 나오기 전까지 전부 받음
		    self.lines = f.readlines()
        return lines

    def merge_list(self):
        return [line.strip().split(',') for line in self.lines]
    
file_path = "data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())
