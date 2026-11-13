import json,sys
T='2026-11-13'
new=[
('meteor-fc-strogino','trial','Первая тренировка — бесплатно','Первое пробное занятие по футболу всегда бесплатно; мяч и инвентарь дают в клубе.','','https://meteorfootball.ru'),
('ska-sergiev-posad','trial','Первая тренировка — бесплатно','Первая тренировка бесплатно — можно прийти познакомиться и посмотреть, как проходят занятия.','','https://ska-sergiev-posad.clients.site'),
('hockey-chance-danilovskaya','trial','Пробная тренировка — 1 000 ₽','Пробная тренировка по хоккею — 1 000 ₽.','','https://hockeychance.ru/stocks/'),
('hockey-montreal-butovo','trial','Пробное занятие — бесплатно, коньки тоже','Пробное занятие по хоккею бесплатно, коньки на пробном выдают бесплатно.','','https://montrealbutovo.ru/'),
('fun-znak-tvorchestva-lobnya','promo','С другом −9% каждому','Приходите с другом — скидка 9% каждому.','','https://znakart.ru'),
('zdorovy-rebenok-kotelniki','discount','−5% на первый абонемент в день консультации','Скидка 5% на первый абонемент на занятия для детей, если оплатить его в день консультации.','','https://zr-kotelniki.ru/skidka-5-na-zanjatija-dlja-detej/'),
('zdorovyi-rebenok-elektrostal','discount','Консультация АВА-терапевта −30%','С 10 по 30 ноября 2026 — скидка 30% на консультацию АВА-терапевта. Скидки не суммируются.','','https://zr-neiro790.ru/konsultacija-ava-terapevta-v-jelektrostali-so-skidkoj-30/'),
('zdorovyi-rebenok-elektrostal','discount','25-го числа — абонементы −10%','Каждый месяц 25-го числа — скидка 10% на абонементы.','','https://zr-neiro790.ru/news/'),
('logodom-dmitrov','discount','Второй курс −5%','Скидка 5% на второй курс по абонементу; при покупке абонемента в день диагностики тоже действуют скидки.','','https://logodom-dmitrov.ru/'),
('mir-skhodnya','trial','Пробное занятие — бесплатно','Пробное занятие в центре бесплатное, запись через сайт.','','https://deti-mir.com/'),
('neyroklass-privolnaya','free','Консультация руководителя — бесплатно','В этом месяце — бесплатная консультация с руководителем центра.','','https://neuro-logo-motion.ru/akcii'),
('semeynaya-akademiya-nezhinskaya','discount','−10% на абонемент в день пробного','Скидка 10% на первый абонемент, если оформить его в день пробного занятия. Не суммируется с индивидуальными занятиями и ментальной арифметикой.','','https://7akadem.ru'),
('semeynaya-akademiya-nezhinskaya','discount','Второй ребёнок −5–10%','Дети из одной семьи: 10% на второй абонемент на ту же программу, 5% — на разные программы.','','https://7akadem.ru'),
('smelost-mechtat-pudovkina','discount','Коммуникативная группа: первый абонемент −30%','Скидка 30% на первый абонемент в коммуникативную группу.','','https://smelostmechtat.ru/'),
('happy-kids-pushkino','discount','Оплата 8+ занятий вперёд — −5%','При предоплате восьми и более занятий — скидка 5%.','','https://hkmed.ru/'),
('iq007-chongarsky','trial','Первое занятие — бесплатно','Первое занятие в IQ007 бесплатно.','','https://school-iq-007.ru'),
('iq007-chongarsky','promo','Приведи друга — 5 000 бонусных ₽','За каждого приведённого друга, который начнёт заниматься, — 5 000 бонусных рублей, другу — 3 000.','','https://school-iq-007.ru'),
('amaklass-khimki','trial','Пробный урок — бесплатно','Пробный урок в «Амаклассе» бесплатный.','','https://amaclass.ru'),
('klass-sovkhoznaya-khimki','trial','Первый урок — бесплатно','Первый урок в центре «Класс» бесплатный.','','https://class-studio.ru'),
('sofia-sport-kronshtadtsky','trial','Первое занятие — бесплатно, абонемент в тот же день −15%','Первое занятие художественной гимнастикой бесплатно; при покупке абонемента в день пробного — скидка 15%.','','https://scsofia.ru/'),
('sofia-sport-kronshtadtsky','discount','Двое детей — −15%','Запишите двух детей — скидка 15% на абонемент. Приведи друга — занятие или форма клуба в подарок.','','https://scsofia.ru/'),
('sparta-rg-domodedovo','trial','Пробное занятие — бесплатно','Пробное занятие художественной гимнастикой бесплатно.','','https://spartarg.ru/'),
('pbk-cska-kronshtadtsky','trial','Пробная тренировка — бесплатно','Бесплатное пробное занятие в школе баскетбола ПБК ЦСКА.','','https://golovinsky.cskabasket.school'),
('barsukova-aerial-skladochnaya','trial','Первое занятие — в подарок','Первое занятие воздушной гимнастикой — в подарок.','','https://barsukova-school.ru'),
('ars-nova-lipovy-park','trial','Пробное занятие в группе — за полцены','Если вы впервые в Ars Nova — пробное занятие в регулярной группе со скидкой 50%.','','https://arsnovamos.ru'),
('chunikhin-musical-khimki','discount','Многодетным и одиноким родителям −10%','Многодетным и одиноким родителям — скидка 10%; есть скидка, если два ребёнка ходят вместе.','','https://musical-school.ru'),
('tennis10is-krasnogorsk','trial','Пробное — 3 000 ₽, с абонементом +1 занятие','Пробное занятие по теннису — 3 000 ₽ (детские группы 4–15 лет); при покупке абонемента после пробного добавят ещё одно занятие бесплатно. Ракетки и мячи на пробном — бесплатно.','','https://10is.ru/trial/'),
('orbita-lva-tolstogo','trial','Первое занятие вокалом — 500 ₽','Первое индивидуальное занятие (55 минут) с диагностикой голоса — 500 ₽ вместо 4 000 ₽.','','https://orbitavoice-school.ru'),
('jswim-dinamo','trial','Пробное занятие — 990 ₽','Пробное занятие в обычной группе с тренером — 990 ₽. Абонемент на месяц в течение 24 часов после пробного — одно занятие в подарок, на 3 месяца — −3 000 ₽.','','https://jswim.ru/'),
('swimteam-roslovka','trial','Первое занятие — бесплатно','Первое занятие плаванием бесплатно.','','https://swim-team-msk.ru/'),
('swimteam-roslovka','promo','Приведи друга — занятие в подарок','Приведите друга на пробное занятие — получите бесплатное занятие в подарок.','','https://swim-team-msk.ru/'),
('triumf-mgpu','trial','Пробное занятие — бесплатно','Школа плавания «Триумф»: бесплатное пробное занятие.','','https://triumfswim.ru/'),
('triumf-lazorevy','trial','Пробное занятие — бесплатно','Школа плавания «Триумф»: бесплатное пробное занятие.','','https://triumfswim.ru/'),
('triumf-korchagina','trial','Пробное занятие — бесплатно','Школа плавания «Триумф»: бесплатное пробное занятие.','','https://triumfswim.ru/'),
('art-impulse-abelmanovskaya','trial','Пробный урок — 700 ₽','Первый пробный урок рисования — 700 ₽, материалы дают.','','https://art-impulse.ru'),
('alya-prima-pokrovka','promo','Вдвоём — по 500 ₽ скидки каждому','Приходите учиться вдвоём — скидка 500 ₽ на курс каждому.','','https://art-55.ru'),
('alya-prima-pokrovka','discount','Промокод −10% на любой курс','Промокод даёт скидку 10% на любой курс — ввести при записи.','Я СДЕЛАЛА ЭТО','https://art-55.ru'),
('airobolab-pushkino-griboedova','trial','Пробное занятие — бесплатно','Бесплатное пробное занятие по робототехнике.','','https://www.airobolab.ru/'),
('airobolab-pushkino-griboedova','promo','Приведи друга — скидка на месяц','Если новый ученик назовёт ваше имя — скидка на следующий месяц обучения (за каждого друга).','','https://www.airobolab.ru/actions/'),
('fk-zvezda-nekrasovka','trial','Первое занятие −50%','Первое занятие фигурным катанием — со скидкой 50%.','','https://star-sport.ru/'),
('fk-ledyanye-krylya-ostafyevskaya','trial','Пробное занятие — бесплатно','Можно записаться на бесплатное занятие по фигурному катанию.','','https://icewings.ru/'),
('fk-led-korolev','trial','Пробное занятие — бесплатно','Бесплатное пробное занятие по фигурному катанию — для новых клиентов, по графику на сайте.','','https://na-ldu.ru/led-news.html'),
('fk-led-korolev','discount','Семейные абонементы — до −30%','Скидки до 30% на семейные абонементы.','','https://na-ldu.ru/led-news.html'),
('yarkova-gym-fryazevskaya','trial','Пробная тренировка — бесплатно','Бесплатное пробное занятие художественной гимнастикой в любом зале школы.','','https://school-rg.ru/'),
('cherryville-profsoyuznaya','discount','Брату/сестре и многодетным — скидка','Скидка на весь курс обучающемуся брату или сестре, а также многодетным семьям (не суммируются). Учебные материалы — бесплатно.','','https://cherryville.ru/'),
('cafe-shu-shu-azovsky','birthday','Имениннику −15%','Скидка 15% в день рождения.','','https://shushurest.ru/'),
('cafe-yaposha-korolev','birthday','День рождения −15%','Скидка 15% на всё меню за 3 дня до и 7 дней после дня рождения, по документу. Не суммируется с другими акциями.','','https://yaposha.com/actions/skidka-15-na-den-rozhdeniya/'),
('cafe-yaposha-shchelkovo','birthday','День рождения −15%','Скидка 15% на всё меню за 3 дня до и 7 дней после дня рождения, по документу. Не суммируется с другими акциями.','','https://yaposha.com/actions/skidka-15-na-den-rozhdeniya/'),
('bylinkino-goat-farm','free','Детям до 7 лет — бесплатно','На экоферму «Былинкино» дети до 7 лет — бесплатно.','','https://www.bylinkino.ru'),
('karting-miks-electro-smolenskaya','trial','Пробное занятие в академии картинга','Пробное занятие для ребёнка в академии картинга — 5 000 ₽, экипировка и шлем бесплатно.','','https://miks-electrokarting.ru'),
('london-excellence-shchelkovo','trial','Бесплатный урок и −10% по заявке','Бесплатный пробный урок и бесплатное тестирование; оставившим заявку на сайте — скидка 10%.','','https://londonese.ru/'),
('interyes-lyublinskaya','trial','Пробный урок — бесплатно','Пробный урок английского — бесплатно.','','https://inter-yes.ru/'),
('linguariki-izmaylovsky','trial','Пробное занятие — бесплатно, новым — до −25%','Бесплатное пробное занятие; для новых клиентов — скидки до 25%.','','https://linguariki.ru/'),
('big-ben-miklukho-maklaya','trial','Пробное занятие — бесплатно','Бесплатное пробное занятие по английскому.','','https://www.big-ben-online.com/'),
('mir-yazykov-domodedovo','trial','Первое занятие — бесплатно','Первое пробное занятие бесплатно.','','https://languageworld.ru/'),
('engdefrance-domodedovo','trial','Первый урок — бесплатно','Первый урок бесплатно, тестирование тоже бесплатное.','','https://engdefrance.ru/'),
]
d=json.load(open('deals.json')); L=d['deals']; ids={x['id'] for x in L}
have={(x['place_id'],x['kind']) for x in L}
sfx={'trial':'trial','free':'free','birthday':'bday','promo':'friend','discount':'disc'}
n=0
for pid,k,t,det,code,url in new:
    if k=='trial' and (pid,k) in have: print('skip dup',pid); continue
    i=f'{pid}-{sfx[k]}'; j=2
    while i in ids: i=f'{pid}-{sfx[k]}{j}'; j+=1
    ids.add(i); x=dict(id=i,place_id=pid,kind=k,title=t,details=det,code=code,until='',url=url,checked=T)
    if pid=='zdorovyi-rebenok-elektrostal' and 'АВА' in t: x['until']='2026-11-30'
    L.append(x); n+=1
d['version']=T; json.dump(d,open('deals.json','w'),ensure_ascii=False,indent=1); print('added',n,len(L))
