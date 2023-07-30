score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    i = 1
    for x in score:
        print(f"{i}번, 평균 : {sum(x)/2}")
        i += 1
        
get_avg(score)