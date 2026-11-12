"""Второй заход карточек «Особым детям» (выдача вернула дом, а не организацию): запрос «название рубрика улица» (ключи ey<n>-1122e)
+ сайты центров для возраста групп → auto/fetch-queue.txt."""
import json, os, re, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
K = {c["n"]: c for c in json.load(open(os.path.join(ROOT, "tools/edu_1122_keep.json")))}
TAKE = [10, 13, 107, 127, 133, 199, 218, 219, 224, 263, 174, 256, 44, 206, 86, 87, 95, 99, 104, 143, 211, 231, 170, 183, 49, 48]
def street(a):
    p = [x.strip() for x in a.split(",")]
    st = next((x for x in p if re.search(r"(ул\.|пр-т|просп|ш\.|пер\.|бул\.|наб\.|проезд|пр\.)", x)), p[0])
    city = next((x for x in p if x in ("Москва", "Мытищи", "Балашиха", "Подольск")), "Москва")
    return f"{city}, {st}"
urls = [f"https://yandex.ru/maps/1/moscow-and-moscow-oblast/?ey{n}=1122e&text=" + urllib.parse.quote(f'{K[n]["name"]} {K[n]["rubric"].split(" ,")[0].lower()} {street(K[n]["addr"])}') for n in TAKE]
SITES = ["https://behaviorandspeech.ru/", "https://slovo-detyam.ru/", "https://logo-umnitsa.ru/", "https://logoped-clinic.ru/",
         "https://www.elizsad.ru/", "https://autism-family-home.ru/", "https://roditeli-vmeste.ru/"]
if __name__ == "__main__":
    old = open(os.path.join(ROOT, "auto/fetch-queue.txt")).read()
    open(os.path.join(ROOT, "auto/fetch-queue.txt"), "w").write("\n".join(urls + SITES) + "\n" + old)
    print(len(urls) + len(SITES))
