#Sorting the contents by a member
#Designed By (soo@in-datalab.com)

f = open('predicted_WannaOne_Final_v2.txt', 'r', 1, 'utf-8')
kd = open("kangdaniel.txt", 'w', 1, 'utf-8')
pjh = open("parkjihoon.txt", 'w', 1, 'utf-8')
ldh = open("leedaehui.txt", 'w', 1, 'utf-8')
kjh = open("kimjaehwan.txt", 'w', 1, 'utf-8')
osw = open ("ongseongwoo.txt", 'w', 1, 'utf-8')
pwj = open ("parkwoojin.txt", 'w', 1, 'utf-8')
lkl = open ("laikwanlin.txt", 'w', 1, 'utf-8')
yjs = open ("yoonjisung.txt", 'w', 1, 'utf-8')
hmh = open ("hwangminhyun.txt", 'w', 1, 'utf-8')
bjy = open ("baejinyoung.txt", 'w', 1, 'utf-8')
hsw = open ("haseongwoon.txt", 'w', 1, 'utf-8')

n_kd = ['강다니엘', '녤', '녜리', '다녤', '다니엘']
n_pjh = ['박지훈', '지훈','윙깅']
n_ldh = ['이대휘', '머휘','머랑둥', '사랑둥이', '대휘']
n_kjh = ['김재환','킹','킹황','환', '재환']
n_osw = ['옹성우', '옹', '성우']
n_pwj = ['박우진','윽진', '우진']
n_lkl = ['라이관린', '판린', '라이', ' 라판린', '관린']
n_yjs = ['윤지성', '굥', '지성']
n_hmh = ['황민현', '황미년', '미년', '민현']
n_bjy = ['배진영', '영단즈', '진영']
n_hsw = ['하성운', '셍', '셍언', '성운','위드']


for line in f:
    if any(word in line for word in n_kd):
        kd.write('강다니엘'+'\t'+ line)
        continue

    elif any(word in line for word in n_pjh):
        pjh.write('박지훈'+ '\t'+ line)
        continue

    elif any(word in line for word in n_ldh):
        ldh.write('이대휘'+ '\t'+ line)
        continue

    elif any(word in line for word in n_kjh):
        kjh.write('김재환'+ '\t'+ line)
        continue

    elif any(word in line for word in n_osw):
        osw.write('옹성우'+ '\t'+ line)
        continue

    elif any(word in line for word in n_pwj):
        pwj.write('박우진'+ '\t'+ line)
        continue

    elif any(word in line for word in n_lkl):
        lkl.write('라이관린'+'\t'+ line)
        continue

    elif any(word in line for word in n_yjs):
        yjs.write('윤지성'+'\t'+ line)
        continue

    elif any(word in line for word in n_hmh):
        hmh.write('황민현'+'\t'+ line)
        continue

    elif any(word in line for word in n_bjy):
        bjy.write('배진영'+ '\t'+ line)
        continue

    elif any(word in line for word in n_hsw):
        hsw.write('하성운'+ '\t'+ line)
        continue

f.close()
kd.close()
pjh.close()
ldh.close()
kjh.close()
osw.close()
pwj.close()
lkl.close()
yjs.close()
hmh.close()
bjy.close()
hsw.close()
