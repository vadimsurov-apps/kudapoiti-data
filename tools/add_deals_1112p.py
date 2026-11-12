import json
T='2026-11-12'
new=[
('iq007-shvernika','trial','Пробный урок — бесплатно','Первый пробный урок бесплатный, родитель присутствует вместе с ребёнком; после урока педагог подберёт группу.','','https://schooliq007.ru/'),
('smartikids-solntsevo','trial','Первое групповое занятие — бесплатно','Для тех, кто пришёл впервые: одно групповое занятие бесплатно, заявка через форму на сайте.','','https://smartysolntcevo.ru'),
('fun-tainy-samotsvetov-stroiteley','free','Арт-шоу с минералами — бесплатно','Экскурсия и мастер-класс с редкими минералами — вход бесплатный, по предварительной записи; каждый гость получает подарок.','','https://www.artshowgems.ru'),
('inkubo-galushkina','birthday','Праздник: трэш-коробка и секретный подарок имениннику','При заказе праздника с пакетом ОПТИМА+, ПРЕМИУМ или ПРЕМИУМ+ — трэш-коробка в подарок и секретный подарок имениннику.','','https://xn----9sbemlmcul8ale.xn--p1ai'),
('sovyonok-zashchitnikov','promo','Приведи друга — скидка вам и другу','Приведите друга: вам до 20% скидки на следующую такую же покупку, другу — до 20% на первый абонемент или разовое занятие (групповые 20%+20%, индивидуальные 15%+15%).','','https://sovenok-dc.ru/'),
('olimp-boevye-reutov','trial','Первое занятие — 0 ₽','Карате, бокс, борьба и гимнастика для детей: первое пробное занятие бесплатно.','','https://olzal.ru/'),
('malysharium-klin','discount','«Няня на час»: −20% семье с двумя детьми','Семейная скидка 20% на присмотр, если одновременно оставляете двух и более детей из одной семьи.','','https://maliysharium.ru/'),
('rink-ld-sokolniki','trial','Первая тренировка — бесплатно','В Ледовом дворце «Сокольники» первая тренировка бесплатная.','','https://ld-sokolniki.ru/'),
('fort-boyard-balashikha','discount','По будням −10% с 10:00 до 16:00','Скидка 10% на квест-шоу по будним дням с 10:00 до 16:00. Скидки не суммируются.','','https://fortboyard-vao.ru'),
('fort-boyard-balashikha','discount','Многодетным семьям −5%','Скидка 5% многодетным семьям.','','https://fortboyard-vao.ru'),
('pogruzhenie-riviera','discount','Онлайн −10%, весь сеанс −30%','При покупке онлайн — скидка 10%, при выкупе всего сеанса — 30%.','','https://www.pogruzhenye.ru'),
('nikuchadze-tushinskaya','trial','Пробное занятие дзюдо и самбо — бесплатно','Первое пробное занятие в клубе бесплатно.','','https://www.nhfjudo.ru/'),
('karate-yasenevo-yasnogorskaya','trial','Первая тренировка по карате — бесплатно','Пробная тренировка в клубе «Ясенево» бесплатно.','','https://www.nskf-moscow.ru/'),
('polet-kommunarka','trial','Пробное занятие — 500 ₽','Любой тариф начинается с пробного занятия («пробный полёт») за 500 ₽.','','https://www.studiopolet.ru'),
]
d=json.load(open('deals.json')); L=d['deals']; ids={x['id'] for x in L}
sfx={'trial':'trial','free':'free','birthday':'bday','promo':'friend','discount':'disc'}
n=0
for pid,k,t,det,code,url in new:
    i=f'{pid}-{sfx[k]}'; j=2
    while i in ids: i=f'{pid}-{sfx[k]}{j}'; j+=1
    ids.add(i); L.append(dict(id=i,place_id=pid,kind=k,title=t,details=det,code=code,until='',url=url,checked=T)); n+=1
# weekday discount fort boyard ends 30.11
for x in L:
    if x['place_id']=='fort-boyard-balashikha' and x['title'].startswith('По будням'): x['until']='2026-11-30'
d['version']=T; json.dump(d,open('deals.json','w'),ensure_ascii=False,indent=1); print('added',n,len(L))
q=json.load(open('/tmp/claude-0/q.json')); r=json.load(open('auto/promo-reviewed.json'))
for v in q: r[v['ref']]=v['hash']
json.dump(r,open('auto/promo-reviewed.json','w'),ensure_ascii=False,indent=1); print('reviewed',len(q))
