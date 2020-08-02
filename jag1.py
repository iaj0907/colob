import random

# global total
# global route  #input()
route = 1000000 #
big = 312 #獲得枚数 1/250
reg = 104 #獲得枚数 1/300
total = 0 #総差枚数

reply = 3
cherry = 2
grape = 7
# グラフ描画
x = []
for i in range(0,8000,1):
  x.append(i)
y = []

def start(route,total):
    bigtotal =0
    regtotal =0
    grapetotal = 0
    replytotal = 0
    cherrytotal = 0
    no = 0
    gassan = 0

    for i in range(1,route):
        get = random.randint(1,57600*7.3) #420480
        
        #bigBonusフラグ成立
        if get <= 240*7.3: 
            total = total + big -3 -1
            bigtotal = bigtotal + 1
            y.append(total)

        #RegBonusフラグ成立
        elif 241*7.3 <= get and get <= 480*7.3:
            total = total + reg -3 -1
            regtotal = regtotal + 1
            y.append(total)

        #Replyフラグ成立
        elif 73580 <= get and get <= 131184:
            total = total + 3 - 3
            replytotal = replytotal + 1
            y.append(total)

        # #Cherryフラグ成立
        # elif 12 <= get and get <= 21:
        #     total = total + 2
        #     cherrytotal = cherrytotal + 1

        #Grapeフラグ成立
        elif 481*7.3 <= get and get <= 10080*7.3: #73584
            total = total + 7 - 3
            grapetotal = grapetotal + 1
            y.append(total)

        #外れ
        else:
            total = total-3 #1.92 #5032回転
            y.append(total)
            no = no+1
    #print(replytotal,grapetotal)
    gassan = route / (bigtotal + regtotal)
    #print(y)
    #print(route/grapetotal)
    #print(grapetotal*6.07)
    
    return int(total),bigtotal,regtotal,grapetotal,int(gassan),y

win=0
#print(y)
word="  差枚数  "+"  BIG回数  "+"  REG回数  "+"  葡萄回数  "+"  合算  "
print(word)

for i in range(100):
    result = start(route,total)
    # print(len(x))
    # print(len(y))
    if result[0] >= 0:
        win = win +1
        print(result[0],result[1],result[2],result[3],result[4])
    elif result[0] <= 0:
        print(result[0],result[1],result[2],result[3],result[4])


print("100台中で勝った台数は・・・")
print(win)

    #print(result[0]+int("a"))
    # if total<=0:
    #     count()


# 子役確率メモ

# rep=1/7.3
# cherry=1/34

# grape 
# 1:6.35
# 2:6.29
# 3:6.25
# 4:6.23
# 5:6.18
# 6:6.07

# big
# 1:287
# 2:283
# 3:273
# 4:264
# 5:252
# 6:240

# reg
# 1:431
# 2:364
# 3:341
# 4:292
# 5:277
# 6:240

# 外れ
# 1:(1-1/287)*(1-1/431)*(1-1/6.35)*(1-1/7.3)*(1-1/34)=0.7
# 2:(1-1/283)*(1-1/364)*(1-1/6.29)*(1-1/7.3)*(1-1/34)=0.7
# 3:(1-1/273)*(1-1/341)*(1-1/6.25)*(1-1/7.3)*(1-1/34)=0.69
# 4:(1-1/264)*(1-1/292)*(1-1/6.23)*(1-1/7.3)*(1-1/34)=0.69
# 5:(1-1/252)*(1-1/277)*(1-1/6.18)*(1-1/7.3)*(1-1/34)=0.69
# 6:(1-1/240)*(1-1/240)*(1-1/6.07)*(1-1/7.3)*(1-1/34)=0.69

# 6:7.3*34*6.07*240*240 = 86778662
