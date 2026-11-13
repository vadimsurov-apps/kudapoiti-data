"""Робот rare 13.11 (1113h), шаг 3: сайты школ и карточки → fetch-queue; справка OSM (rare13m-*). python3 tools/rare_1113h_step3.py"""
import json
p='auto/fetch-queue.txt'
old=open(p).read().rstrip("\n").split("\n")
new=["https://myway-skatingschool.ru","https://lmstn.ru","https://figskating.ru","https://squashclub.moscow","https://motorinschool.ru","https://na-ldu.ru",
"https://yandex.ru/maps/org/sportivnyye_linii/6211483349/","https://yandex.ru/maps/org/ledovy_dvorets/1062470155/","https://yandex.ru/maps/org/monster_hockey/11054832904/",
"https://yandex.ru/maps/org/biryukov_a_v_hockey_academy/83185725964/"]
open(p,'w').write("\n".join(old+[l for l in new if l not in old])+"\n")
q=[x for x in json.load(open('auto/osm-queries.json')) if not x["id"].startswith("rare13m-")]
for k,la,lo,r,nm,st in [("na-ldu-khimki",55.9121,37.4589,500,"Лёд","Мичурина"),("sport-lines-ivanteevskaya",55.818028,37.726098,400,"Спортивные","Ивантеевская"),
                        ("squash-moskva-luzhniki",55.7155,37.5560,900,"Сквош",""),("salyut-dolgoprudny",55.9282,37.5205,500,"Салют","Ракетостроителей"),
                        ("champion-bitsa",55.64408,37.58153,400,"Чемпион",""),("limestone-dobroslobodskaya",55.7712,37.6765,500,"Лайм","Доброслободская"),
                        ("pegas-domodedovo",55.4318,37.752,900,"Пегас","Кирова")]:
    x={"id":"rare13m-"+k,"lat":la,"lon":lo,"radius":r,"name":nm,"geom":True}
    if st:x["street"]=st
    q.append(x)
json.dump(q,open('auto/osm-queries.json','w'),ensure_ascii=False,indent=1)
