# Privacy Policy / Політика конфіденційності

**App / Застосунок:** Mewmori
**Effective date / Дата набуття чинності:** June 10, 2026
**Last updated / Останнє оновлення:** June 10, 2026

<p align="center">
  <a href="#english"><b>🇬🇧 English</b></a>
  &nbsp;·&nbsp;
  <a href="#ukrainian"><b>🇺🇦 Українська</b></a>
  &nbsp;·&nbsp;
  <a href="./terms/"><b>Terms of Use / Умови використання</b></a>
</p>

---

<a id="english"></a>

## 🇬🇧 English

This Privacy Policy describes how the **Mewmori** mobile application ("App", "we") handles your information. By using the App, you agree to the terms below.

### 1. The short version

Mewmori has **no accounts and no tracking**. Your vocabulary lives on your device (and, with a Pro subscription, in your own private iCloud). The only thing that ever leaves your device is the word or phrase you ask the App to translate — it is sent to our translation server and to our AI provider to produce the translation, and it is not used to identify you.

### 2. Information we process

**Words and phrases you submit for translation or sentence checking.** When you add a word (or use the sentence-check exercise), the text you entered, the language pair, and the result format are sent over HTTPS to our server-side proxy (hosted on Cloudflare Workers), which forwards the text to **Anthropic** (the Claude AI model) to generate the translation and learner notes. We do **not** store your texts on our servers; the proxy holds no database of your entries.

**Anonymous install identifier.** The App generates a random identifier (UUID) on first launch. It is sent with translation requests **solely** to enforce fair-use limits (a weekly request quota) and prevent abuse. It is not linked to your name, email, Apple ID, or device serial number, and it is never shared with the AI provider. Quota counters expire automatically (about 16 days). Reinstalling the App creates a new identifier.

**Your vocabulary and learning progress.** Saved words, translations, notes, and spaced-repetition progress are stored **locally on your device**. If you have an active Mewmori Pro subscription, this data also syncs through **your private iCloud database (Apple CloudKit)**. We have no access to your iCloud data — it is encrypted and managed by Apple under your Apple ID.

**Subscription status.** Purchases are processed entirely by the Apple App Store. We receive only an anonymized confirmation that a subscription is active. We never see your payment details.

### 3. What we do NOT do

- No analytics SDKs (Google Analytics, Firebase, Mixpanel, etc.).
- No advertising and no ad networks.
- No marketing trackers, no fingerprinting, no selling of data.
- No accounts, no email collection, no contact upload.
- No crash reporters that send data to third parties.

### 4. Third-party services

| Service | Purpose | What it receives | Policy |
|---|---|---|---|
| Anthropic (Claude) | Generates translations and learner notes | Only the text you submitted and the language pair — no identifiers | <https://www.anthropic.com/privacy> |
| Cloudflare | Hosts our translation proxy and quota counters | Standard network metadata (IP address during the request), the anonymous install ID | <https://www.cloudflare.com/privacypolicy/> |
| Apple — App Store | Processes purchases and subscriptions | Payment handled entirely by Apple | <https://www.apple.com/legal/privacy/> |
| Apple — iCloud / CloudKit | Syncs your vocabulary across your devices (Pro) | Your vocabulary data, stored in **your** private iCloud | <https://www.apple.com/legal/privacy/> |

### 5. Notifications and permissions

Study reminders are **local notifications** scheduled on your device; they require your permission, which you can revoke any time in iOS Settings. The App does not request access to your microphone, camera, photos, contacts, location, or calendar.

### 6. Data retention and deletion

Local data is deleted when you delete the App. iCloud data (Pro) can be removed via **iOS Settings → Apple ID → iCloud → Manage Storage → Mewmori**, or by deleting your words inside the App before removing it. Server-side quota counters expire automatically and contain no personal content.

### 7. Children

The App is not directed at children under 13 and does not knowingly collect personal information from them.

### 8. Changes to this policy

We may update this policy; changes are published at this address with an updated date. Continued use of the App after an update means you accept the new version.

### 9. Contact

**Email:** danyalaykun@gmail.com

<p align="center">
  <a href="#ukrainian"><b>🇺🇦 Перейти на українську</b></a>
</p>

---

<a id="ukrainian"></a>

## 🇺🇦 Українська

Ця Політика конфіденційності описує, як мобільний застосунок **Mewmori** («Застосунок», «ми») обробляє вашу інформацію. Користуючись Застосунком, ви погоджуєтеся з умовами нижче.

### 1. Якщо коротко

У Mewmori **немає акаунтів і немає трекінгу**. Ваш словник живе на вашому пристрої (а з підпискою Pro — у вашому власному приватному iCloud). Єдине, що залишає пристрій, — це слово чи фраза, яку ви просите перекласти: вона надсилається на наш сервер перекладу та нашому AI-провайдеру, щоб згенерувати переклад, і не використовується для вашої ідентифікації.

### 2. Інформація, яку ми обробляємо

**Слова та фрази, які ви надсилаєте на переклад або перевірку речення.** Коли ви додаєте слово (або користуєтеся вправою «Перевірка речення»), введений текст і мовна пара передаються через HTTPS на наш серверний проксі (на Cloudflare Workers), який пересилає текст до **Anthropic** (AI-модель Claude) для генерації перекладу та навчальних приміток. Ми **не** зберігаємо ваші тексти на серверах; проксі не має бази даних ваших записів.

**Анонімний ідентифікатор встановлення.** При першому запуску Застосунок генерує випадковий ідентифікатор (UUID). Він надсилається разом із запитами на переклад **виключно** для дотримання лімітів чесного використання (тижнева квота запитів) і захисту від зловживань. Він не повʼязаний з вашим імʼям, поштою, Apple ID чи серійним номером пристрою і ніколи не передається AI-провайдеру. Лічильники квоти видаляються автоматично (близько 16 днів). Перевстановлення Застосунку створює новий ідентифікатор.

**Ваш словник і прогрес навчання.** Збережені слова, переклади, примітки та прогрес інтервальних повторень зберігаються **локально на вашому пристрої**. Якщо у вас активна підписка Mewmori Pro, ці дані також синхронізуються через **вашу приватну базу iCloud (Apple CloudKit)**. Ми не маємо доступу до ваших даних iCloud — їх шифрує та обслуговує Apple у межах вашого Apple ID.

**Статус підписки.** Покупки повністю обробляє Apple App Store. Ми отримуємо лише знеособлене підтвердження, що підписка активна. Ваших платіжних даних ми не бачимо.

### 3. Чого ми НЕ робимо

- Жодних SDK аналітики (Google Analytics, Firebase, Mixpanel тощо).
- Жодної реклами та рекламних мереж.
- Жодних маркетингових трекерів, фінгерпринтингу чи продажу даних.
- Жодних акаунтів, збору пошти чи завантаження контактів.
- Жодних крашрепортерів, що надсилають дані третім сторонам.

### 4. Сторонні сервіси

| Сервіс | Призначення | Що отримує | Політика |
|---|---|---|---|
| Anthropic (Claude) | Генерує переклади та навчальні примітки | Лише надісланий вами текст і мовну пару — без ідентифікаторів | <https://www.anthropic.com/privacy> |
| Cloudflare | Хостить наш проксі перекладів і лічильники квоти | Стандартні мережеві метадані (IP-адреса під час запиту), анонімний ідентифікатор встановлення | <https://www.cloudflare.com/privacypolicy/> |
| Apple — App Store | Обробляє покупки та підписки | Оплату повністю обробляє Apple | <https://www.apple.com/legal/privacy/> |
| Apple — iCloud / CloudKit | Синхронізує словник між вашими пристроями (Pro) | Дані вашого словника у **вашому** приватному iCloud | <https://www.apple.com/legal/privacy/> |

### 5. Сповіщення та дозволи

Нагадування про навчання — це **локальні сповіщення**, заплановані на вашому пристрої; вони потребують вашого дозволу, який можна будь-коли відкликати в Налаштуваннях iOS. Застосунок не запитує доступ до мікрофона, камери, фото, контактів, геолокації чи календаря.

### 6. Зберігання та видалення даних

Локальні дані видаляються разом із Застосунком. Дані iCloud (Pro) можна видалити через **Налаштування iOS → Apple ID → iCloud → Керування сховищем → Mewmori** або видаливши слова в Застосунку перед його видаленням. Серверні лічильники квоти видаляються автоматично й не містять персонального вмісту.

### 7. Діти

Застосунок не призначений для дітей до 13 років і свідомо не збирає від них персональну інформацію.

### 8. Зміни до цієї політики

Ми можемо оновлювати цю політику; зміни публікуються за цією адресою з оновленою датою. Подальше користування Застосунком після оновлення означає згоду з новою версією.

### 9. Контакти

**Email:** danyalaykun@gmail.com

<p align="center">
  <a href="#english"><b>🇬🇧 Switch to English</b></a>
  &nbsp;·&nbsp;
  <a href="./terms/"><b>Умови використання</b></a>
</p>
