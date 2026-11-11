# Codex по подписке ChatGPT — проверка карточек без оплаты API (настройка один раз, ~15 минут)

Как работает: каждый час робот GitHub (gpt-codex.yml) готовит пачки мест и в pull request пишет от твоего имени
«@codex проверь». Codex в облаке OpenAI (по твоей подписке ChatGPT, отдельно не платится) читает AGENTS.md и наш свод
правил gpt/RULES.md, проверяет места в интернете и кладёт отчёт. Отчёт вливается и применяется к карте сам.
Компьютер включённым держать не нужно.

## Шаг 1. Подключить Codex к репозиторию
1. Открыть **chatgpt.com/codex** (тот же аккаунт ChatGPT, за который платишь).
2. Подключить GitHub, если ещё не подключён: дать доступ к репозиторию **vadimsurov-apps/kudapoiti-data**.
3. **Settings → Environments → Create environment** → репозиторий `vadimsurov-apps/kudapoiti-data`.
   - **Agent internet access: On**, Domain allowlist: **All (unrestricted)**, HTTP methods: **GET, HEAD, OPTIONS**
     (ему нужно читать сайты мест, Яндекс Карты, 2ГИС; отправлять что-то в интернет не нужно).
   - Сохранить.

## Шаг 2. Ключ, чтобы робот мог писать «@codex» от твоего имени
Codex отвечает только на комментарии владельца подписки, поэтому комментарий должен быть от тебя.
1. github.com → аватар → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Name: `codex-trigger`; Expiration: 1 год; Repository access: **Only select repositories → kudapoiti-data**.
3. Permissions → Repository permissions: **Contents — Read and write**, **Pull requests — Read and write**.
4. Generate → скопировать токен (никому не присылать, в чат тоже).
5. github.com/vadimsurov-apps/kudapoiti-data → **Settings → Secrets and variables → Actions → New repository secret**:
   Name `CODEX_PAT`, Secret — вставить токен → Add secret.

## Шаг 3. Пробный запуск
Actions → «Codex-проверяющий …» → Run workflow (можно оставить пусто). Через 1–2 минуты появится pull request
«Проверка карточек Codex: …» с комментарием @codex; Codex поставит 👀 и начнёт работу (её видно и на chatgpt.com/codex).
Через 10–40 минут в PR появится отчёт, PR вольётся сам. Написать роботу (Claude), что запустил, — он посмотрит
результат и настроит, сколько пачек держать.

## Сколько проверяет
Переменные репозитория (Settings → Secrets and variables → Actions → Variables): `CODEX_SLICES` — сколько пачек
в работе одновременно (по умолчанию 3), `CODEX_N` — мест в пачке (25). Робот запускается каждый час и добирает пачки
по мере того, как Codex их сдаёт. Упрёмся в лимит подписки — Codex перестанет отвечать, зависшие пачки через 10 часов
закрываются сами, места возвращаются в очередь.
