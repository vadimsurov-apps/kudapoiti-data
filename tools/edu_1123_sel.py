"""Робот edu, 2026-11-12/13 (тринадцатый запуск): отбор по карточкам организаций Яндекс Карт (auto/pages *-ev<N>-1123e* — «23:N»).
Поиск по районам (выдачи *-eu<N>-1123e*): Лубянка, Лужники, Новомосковская, Октябрьская, Ольховая, Охотный ряд, Парк культуры,
Петровский парк, Петровско-Разумовская, Печатники, Пионерская, Планерная, Площадь Гагарина, Площадь Ильича, Полежаевская;
второй заход «Особым детям» (*-ew<N>-1123e*): Площадь Революции … Рассказовка.
Возраст — только из названий групп/услуг карточки и сайтов.
pid: (ключ карточки, название, тип, категории, от, до, цена, пояснение к цене, плюс, теги, пробное бесплатно)"""
T = "творчество"
# Отложенные запусками 1120–1122 (карточки и точки готовы, иконки — tools/icons_edu_1123.py)
DEFERRED = ["puteshestvie-rechi-lavrinenko", "kiberone-nekrasovka", "golovolomka-reutov", "bukvaryonok-novocheryomushkinskaya", "vivi-fryazino", "doverie-lytkarino", "poslushayka-elektrolitny", "yarkie-deti-nagatinskaya", "sovushka-vorontsovskie", "plastilin-tamoykina", "plastilin-rekintso", "kak-zdorovo-zhulebino", "baby-club-khodynsky", "kiberone-novatorov", "kiberone-lobachevskogo", "iq007-grizodubovoy", "bambino-erudito-korabelnaya", "kosmos-montessori-novorogozhskaya", "uh-ty-kub-mikhaylova", "luchik-sokol", "milgrad-vladimirskaya", "vershina-mytishchi", "kubik-sokolovskogo", "ladushki-kuchino", "talantika-mytishchi", "mamin-chasik-shipilovskaya"]
SEL = {
}
SITE_SRC = {}
HOW_FIX = {}
TAKE = set(SEL)
# «Особым детям»: что продумано (поле access.programs) — фактами из карточки/сайта
PROG = {}
SENS = {}
ACCESS_EXTRA = {}
CATAGES = {}
DEALS = {}
