// Проба: открываются ли карты из GitHub Actions без капчи (одна страница с каждой, ничего не сохраняем в данные)
const { chromium } = require('playwright');
const fs = require('fs'); fs.mkdirSync('probe', { recursive: true });
const urls = {
  yandex: 'https://yandex.ru/maps/213/moscow/search/Winners%20Шмитовский%2039%20к6/',
  dgis: 'https://2gis.ru/moscow/search/Winners%20Шмитовский%2039%20к6',
  google: 'https://www.google.com/maps/search/Winners+Шмитовский+39+к6+Москва',
};
(async () => {
  const b = await chromium.launch();
  for (const [k, u] of Object.entries(urls)) {
    const p = await b.newPage({ locale: 'ru-RU', viewport: { width: 1280, height: 900 } });
    try {
      await p.goto(u, { timeout: 45000, waitUntil: 'domcontentloaded' });
      await p.waitForTimeout(8000);
      const t = (await p.innerText('body')).slice(0, 3000);
      fs.writeFileSync(`probe/${k}.txt`, p.url() + '\n' + t);
      await p.screenshot({ path: `probe/${k}.png` });
      console.log(k, p.url(), /captcha|робот|не робот|unusual traffic/i.test(t) ? 'CAPTCHA' : 'ok', t.slice(0, 300).replace(/\n/g, ' | '));
    } catch (e) { console.log(k, 'ERR', e.message); }
  }
  await b.close();
})();
