# -*- coding: utf-8 -*-
"""Native copy: FAQ extras, mirror block, bilingual labels, SEO footer lines."""

from __future__ import annotations


def faq_extra(code: str, site: str, dl: str) -> list[tuple[str, str]]:
  """Three extra FAQ items per README locale."""
  m: dict[str, list[tuple[str, str]]] = {
    "ru": [
      (
        "Windows 7 / macOS / Linux?",
        f"Установщик для **Windows 10/11 x64**. Подробнее: [{dl}]({dl}).",
      ),
      (
        "Где английская версия?",
        f"[{site}/en/]({site}/en/) — Download Horizon, гайды и FAQ на английском.",
      ),
      (
        "Зачем GitHub, если есть сайт?",
        f"Чтобы запросы вроде «Horizon Minecraft GitHub» и «Horizon launcher github» вели на канон **[horizonlauncher.net]({site}/)**, а не на зеркала.",
      ),
    ],
    "en": [
      (
        "Windows 7 / macOS / Linux?",
        f"The setup targets **Windows 10/11 x64**. See [{dl}]({dl}).",
      ),
      (
        "Russian version?",
        f"[{site}/]({site}/) — скачать Horizon (README.md на русском).",
      ),
      (
        "Why GitHub if the site exists?",
        f"So searches like «Horizon launcher github» point to canonical **[horizonlauncher.net]({site}/en/)**, not random mirrors.",
      ),
    ],
    "uk": [
      (
        "Windows 7 / macOS / Linux?",
        f"Інсталятор лише для **Windows 10/11 x64**. [{dl}]({dl}).",
      ),
      (
        "Де англійська версія?",
        f"[{site}/en/]({site}/en/) — Download Horizon.",
      ),
      (
        "Навіщо GitHub?",
        f"Щоб пошук «Horizon launcher github» вів на **[horizonlauncher.net]({site}/)**, а не на сторонні репозиторії.",
      ),
    ],
    "es": [
      (
        "¿Windows 7 / macOS / Linux?",
        f"Solo **Windows 10/11 x64**. Detalles: [{dl}]({dl}).",
      ),
      (
        "¿Versión en ruso?",
        f"[{site}/]({site}/) — README principal en ruso.",
      ),
      (
        "¿Por qué GitHub?",
        f"Para que búsquedas como «Horizon launcher github» lleven al sitio canónico **[horizonlauncher.net]({site}/es/)**.",
      ),
    ],
    "pt": [
      (
        "Windows 7 / macOS / Linux?",
        f"O instalador é para **Windows 10/11 x64**. Veja [{dl}]({dl}).",
      ),
      (
        "Versão em russo?",
        f"[{site}/]({site}/) — página principal em russo (README.md).",
      ),
      (
        "Por que GitHub?",
        f"Para que buscas como «Horizon launcher github» apontem para **[horizonlauncher.net]({site}/pt/)**, não para espelhos.",
      ),
    ],
    "de": [
      (
        "Windows 7 / macOS / Linux?",
        f"Nur **Windows 10/11 x64**. Details: [{dl}]({dl}).",
      ),
      (
        "Russische Seite?",
        f"[{site}/]({site}/) — Hauptseite und README.md auf Russisch.",
      ),
      (
        "Warum GitHub?",
        f"Damit Suchanfragen wie «Horizon launcher github» zu **[horizonlauncher.net]({site}/de/)** führen.",
      ),
    ],
    "fr": [
      (
        "Windows 7 / macOS / Linux ?",
        f"Uniquement **Windows 10/11 x64**. Voir [{dl}]({dl}).",
      ),
      (
        "Version russe ?",
        f"[{site}/]({site}/) — README principal en russe.",
      ),
      (
        "Pourquoi GitHub ?",
        f"Pour que « Horizon launcher github » mène au site canonique **[horizonlauncher.net]({site}/fr/)**.",
      ),
    ],
    "it": [
      (
        "Windows 7 / macOS / Linux?",
        f"Solo **Windows 10/11 x64**. Dettagli: [{dl}]({dl}).",
      ),
      (
        "Versione russa?",
        f"[{site}/]({site}/) — README principale in russo.",
      ),
      (
        "Perché GitHub?",
        f"Così ricerche come «Horizon launcher github» portano a **[horizonlauncher.net]({site}/it/)**.",
      ),
    ],
    "pl": [
      (
        "Windows 7 / macOS / Linux?",
        f"Tylko **Windows 10/11 x64**. Zobacz [{dl}]({dl}).",
      ),
      (
        "Wersja rosyjska?",
        f"[{site}/]({site}/) — główny README po rosyjsku.",
      ),
      (
        "Po co GitHub?",
        f"Aby zapytania «Horizon launcher github» prowadziły do **[horizonlauncher.net]({site}/pl/)**.",
      ),
    ],
    "tr": [
      (
        "Windows 7 / macOS / Linux?",
        f"Yalnızca **Windows 10/11 x64**. [{dl}]({dl}).",
      ),
      (
        "Rusça sürüm?",
        f"[{site}/]({site}/) — ana README Rusça.",
      ),
      (
        "Neden GitHub?",
        f"«Horizon launcher github» aramaları **[horizonlauncher.net]({site}/tr/)** adresine yönlensin diye.",
      ),
    ],
    "zh": [
      (
        "Windows 7 / macOS / Linux？",
        f"安装包仅支持 **Windows 10/11 x64**。详见 [{dl}]({dl})。",
      ),
      (
        "俄语站？",
        f"[{site}/]({site}/) — 主 README 为俄语。",
      ),
      (
        "为什么还有 GitHub？",
        f"让「Horizon launcher github」等搜索指向 canonical **[horizonlauncher.net]({site}/zh/)**。",
      ),
    ],
    "ja": [
      (
        "Windows 7 / macOS / Linux？",
        f"**Windows 10/11 x64** のみ対応。[{dl}]({dl})。",
      ),
      (
        "ロシア語サイトは？",
        f"[{site}/]({site}/) — メイン README はロシア語。",
      ),
      (
        "GitHub がある理由は？",
        f"「Horizon launcher github」検索を **[horizonlauncher.net]({site}/ja/)** に誘導するため。",
      ),
    ],
    "ko": [
      (
        "Windows 7 / macOS / Linux?",
        f"**Windows 10/11 x64** 만 지원. [{dl}]({dl}).",
      ),
      (
        "러시아어 버전?",
        f"[{site}/]({site}/) — 기본 README는 러시아어.",
      ),
      (
        "GitHub가 있는 이유?",
        f"«Horizon launcher github» 검색이 **[horizonlauncher.net]({site}/ko/)** 로 연결되도록.",
      ),
    ],
    "ar": [
      (
        "Windows 7 / macOS / Linux؟",
        f"المثبّت لـ **Windows 10/11 x64** فقط. [{dl}]({dl}).",
      ),
      (
        "النسخة الروسية؟",
        f"[{site}/]({site}/) — README الرئيسي بالروسية.",
      ),
      (
        "لماذا GitHub؟",
        f"حتى تُوجَّه عبارات مثل «Horizon launcher github» إلى **[horizonlauncher.net]({site}/ar/)**.",
      ),
    ],
    "hi": [
      (
        "Windows 7 / macOS / Linux?",
        f"केवल **Windows 10/11 x64**. [{dl}]({dl}).",
      ),
      (
        "रूसी संस्करण?",
        f"[{site}/]({site}/) — मुख्य README रूसी में.",
      ),
      (
        "GitHub क्यों?",
        f"ताकि «Horizon launcher github» खोज **[horizonlauncher.net]({site}/hi/)** पर जाए.",
      ),
    ],
    "id": [
      (
        "Windows 7 / macOS / Linux?",
        f"Hanya **Windows 10/11 x64**. [{dl}]({dl}).",
      ),
      (
        "Versi Rusia?",
        f"[{site}/]({site}/) — README utama berbahasa Rusia.",
      ),
      (
        "Mengapa GitHub?",
        f"Agar pencarian «Horizon launcher github» mengarah ke **[horizonlauncher.net]({site}/id/)**.",
      ),
    ],
    "vi": [
      (
        "Windows 7 / macOS / Linux?",
        f"Chỉ **Windows 10/11 x64**. [{dl}]({dl}).",
      ),
      (
        "Bản tiếng Nga?",
        f"[{site}/]({site}/) — README chính bằng tiếng Nga.",
      ),
      (
        "Vì sao có GitHub?",
        f"Để truy vấn «Horizon launcher github» trỏ về **[horizonlauncher.net]({site}/vi/)**.",
      ),
    ],
  }
  return m.get(code, m["en"])


def mirror_block(code: str, site: str, exe: str, latest: str) -> tuple[str, str]:
  """Section title + body (EN landing for non-EN; RU landing for EN)."""
  en_home = f"{site}/en/"
  en_dl = f"{site}/en/download-horizon/"
  ru_home = f"{site}/"
  ru_dl = f"{site}/download-horizon/"

  if code == "en":
    return (
      "Русский — скачать Horizon Minecraft launcher",
      f"**Horizon** — бесплатный **лаунчер Minecraft для Windows** и **клиент Java на Rust** "
      f"(Minecraft Rust Edition). Канон: [{ru_home}]({ru_home}) · [{ru_dl}]({ru_dl}) · **[{exe}]({exe})** · версия **{latest}**. "
      f"Официальный Horizon. Качай с horizonlauncher.net.",
    )

  if code == "ru":
    return (
      "English — Download Horizon Minecraft launcher",
      f"**Horizon** is a free **Windows Minecraft launcher** and **Minecraft Java client in Rust** "
      f"(Minecraft Rust Edition). Canonical download: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Official Horizon team. News: [t.me/horizonlauncher](https://t.me/horizonlauncher).",
    )

  titles = {
    "uk": "Англійська — Download Horizon Minecraft launcher",
    "es": "Inglés — descargar Horizon Minecraft launcher",
    "pt": "Inglês — baixar Horizon Minecraft launcher",
    "de": "Englisch — Horizon Minecraft Launcher herunterladen",
    "fr": "Anglais — télécharger le launcher Horizon Minecraft",
    "it": "Inglese — scarica Horizon Minecraft launcher",
    "pl": "Angielski — pobierz Horizon Minecraft launcher",
    "tr": "İngilizce — Horizon Minecraft launcher indir",
    "zh": "English — 下载 Horizon Minecraft launcher",
    "ja": "English — Horizon Minecraft ランチャーをダウンロード",
    "ko": "English — Horizon Minecraft 런처 다운로드",
    "ar": "English — تنزيل Horizon Minecraft launcher",
    "hi": "English — Horizon Minecraft launcher डाउनलोड",
    "id": "English — unduh Horizon Minecraft launcher",
    "vi": "English — tải Horizon Minecraft launcher",
  }
  bodies = {
    "uk": (
      f"**Horizon** — безкоштовний **лаунчер Minecraft для Windows** і **клієнт Java на Rust**. "
      f"Офіційна англійська сторінка: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Не Mojang / Microsoft."
    ),
    "es": (
      f"**Horizon** es un **launcher de Minecraft para Windows** gratuito y un **cliente Java en Rust** "
      f"(Minecraft Rust Edition). Descarga canónica en inglés: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"No es de Mojang/Microsoft."
    ),
    "pt": (
      f"**Horizon** é um **launcher Minecraft para Windows** gratuito e um **cliente Java em Rust** "
      f"(Minecraft Rust Edition). Página oficial em inglês: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Não é da Mojang/Microsoft."
    ),
    "de": (
      f"**Horizon** ist ein kostenloser **Minecraft-Launcher für Windows** und ein **Java-Client in Rust** "
      f"(Minecraft Rust Edition). Offizielle englische Seite: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Nicht von Mojang/Microsoft."
    ),
    "fr": (
      f"**Horizon** est un **launcher Minecraft Windows** gratuit et un **client Java en Rust** "
      f"(Minecraft Rust Edition). Page anglaise officielle : [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Non affilié à Mojang/Microsoft."
    ),
    "it": (
      f"**Horizon** è un **launcher Minecraft per Windows** gratuito e un **client Java in Rust** "
      f"(Minecraft Rust Edition). Download canonico in inglese: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Non è Mojang/Microsoft."
    ),
    "pl": (
      f"**Horizon** to darmowy **launcher Minecraft na Windows** i **klient Java w Rust** "
      f"(Minecraft Rust Edition). Angielska strona: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Niezależny od Mojang/Microsoft."
    ),
    "tr": (
      f"**Horizon** ücretsiz bir **Windows Minecraft launcher** ve **Rust ile Java istemcisidir** "
      f"(Minecraft Rust Edition). Resmî İngilizce sayfa: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. "
      f"Mojang/Microsoft ürünü değildir."
    ),
    "zh": (
      f"**Horizon** 是免费的 **Windows Minecraft 启动器** 与 **Rust 重写的 Java 客户端**（Minecraft Rust Edition）。"
      f"英文 canonical 页面：[{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**。非 Mojang/Microsoft 官方产品。"
    ),
    "ja": (
      f"**Horizon** は無料の **Windows 向け Minecraft ランチャー** と **Rust 製 Java クライアント**（Minecraft Rust Edition）です。"
      f"英語の公式ページ：[{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**。Mojang/Microsoft 公式ではありません。"
    ),
    "ko": (
      f"**Horizon**은 무료 **Windows Minecraft 런처**와 **Rust Java 클라이언트**(Minecraft Rust Edition)입니다. "
      f"영문 공식 페이지: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. Mojang/Microsoft 공식 아님."
    ),
    "ar": (
      f"**Horizon** مشغّل **Minecraft لـ Windows** مجاني و**عميل Java بلغة Rust** (Minecraft Rust Edition). "
      f"الصفحة الإنجليزية الرسمية: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. غير تابع لـ Mojang/Microsoft."
    ),
    "hi": (
      f"**Horizon** एक मुफ़्त **Windows Minecraft launcher** और **Rust में Java क्लाइंट** (Minecraft Rust Edition) है। "
      f"अंग्रेज़ी canonical पेज: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. Mojang/Microsoft आधिकारिक नहीं।"
    ),
    "id": (
      f"**Horizon** adalah **launcher Minecraft Windows** gratis dan **klien Java di Rust** "
      f"(Minecraft Rust Edition). Halaman Inggris resmi: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. Bukan Mojang/Microsoft."
    ),
    "vi": (
      f"**Horizon** là **launcher Minecraft Windows** miễn phí và **client Java viết bằng Rust** "
      f"(Minecraft Rust Edition). Trang tiếng Anh chính thức: [{en_home}]({en_home}) · [{en_dl}]({en_dl}) · **[{exe}]({exe})** · **{latest}**. Không phải Mojang/Microsoft."
    ),
  }
  title = titles.get(code, titles["es"])
  body = bodies.get(code, bodies["es"])
  return title, body


def bilingual_section(
  code: str,
  site: str,
  paths: dict[str, str],
  exe: str,
) -> str:
  labels = {
    "uk": ("Українська", "English", "Русский", "карта сайту"),
    "es": ("Español", "English", "Русский", "mapa del sitio"),
    "pt": ("Português", "English", "Русский", "mapa do site"),
    "de": ("Deutsch", "English", "Русisch", "Sitemap"),
    "fr": ("Français", "English", "Russe", "plan du site"),
    "it": ("Italiano", "English", "Russo", "mappa del sito"),
    "pl": ("Polski", "English", "Rosyjski", "mapa witryny"),
    "tr": ("Türkçe", "English", "Rusça", "site haritası"),
    "zh": ("简体中文", "English", "俄语", "网站地图"),
    "ja": ("日本語", "English", "ロシア語", "サイトマップ"),
    "ko": ("한국어", "English", "러시아어", "사이트맵"),
    "ar": ("العربية", "English", "Русский", "خريطة الموقع"),
    "hi": ("हिन्दी", "English", "Русский", "साइटमैप"),
    "id": ("Indonesia", "English", "Rusia", "peta situs"),
    "vi": ("Tiếng Việt", "English", "Tiếng Nga", "sơ đồ trang"),
  }
  loc, en_l, ru_l, sm = labels.get(code, ("Local", "English", "Русский", "sitemap"))
  return f"""**{loc}:** [{paths['home']}]({paths['home']}) · [{paths['dl']}]({paths['dl']}) · [{paths['inst']}]({paths['inst']}) · [{paths['rust']}]({paths['rust']}) · [{paths['gallery']}]({paths['gallery']}) · [{exe}]({exe})

**{en_l}:** [{site}/en/]({site}/en/) · [{site}/en/download-horizon/]({site}/en/download-horizon/)

**{ru_l}:** [{site}/]({site}/) · [{site}/download-horizon/]({site}/download-horizon/)

[{sm}]({site}/sitemap.xml) · [Telegram](https://t.me/horizonlauncher)"""


def seo_footer_lines(
  code: str,
  site: str,
  paths: dict[str, str],
  exe: str,
  tg: str,
) -> str:
  L = {
    "ru": ("Сайт", "Скачать", "Настройка", "Установщик", "EN", "Minecraft на Rust", "Telegram", "Карта сайта"),
    "en": ("Site", "Download", "Win+R", "Setup", "RU main", "Minecraft on Rust", "Telegram", "Sitemap"),
    "uk": ("Сайт", "Завантажити", "Win+R", "Setup.exe", "EN", "Minecraft на Rust", "Telegram", "Карта сайту"),
    "es": ("Sitio", "Descargar", "Win+R", "Setup", "EN", "Minecraft en Rust", "Telegram", "Mapa del sitio"),
    "pt": ("Site", "Baixar", "Win+R", "Setup", "EN", "Minecraft em Rust", "Telegram", "Mapa do site"),
    "de": ("Webseite", "Download", "Win+R", "Setup", "EN", "Minecraft in Rust", "Telegram", "Sitemap"),
    "fr": ("Site", "Télécharger", "Win+R", "Setup", "EN", "Minecraft sur Rust", "Telegram", "Plan du site"),
    "it": ("Sito", "Scarica", "Win+R", "Setup", "EN", "Minecraft su Rust", "Telegram", "Mappa sito"),
    "pl": ("Strona", "Pobierz", "Win+R", "Setup", "EN", "Minecraft na Rust", "Telegram", "Mapa witryny"),
    "tr": ("Site", "İndir", "Win+R", "Setup", "EN", "Rust'ta Minecraft", "Telegram", "Site haritası"),
    "zh": ("网站", "下载", "Win+R", "安装包", "EN", "Rust 版 Minecraft", "Telegram", "网站地图"),
    "ja": ("サイト", "ダウンロード", "Win+R", "セットアップ", "EN", "Rust版 Minecraft", "Telegram", "サイトマップ"),
    "ko": ("사이트", "다운로드", "Win+R", "설치 파일", "EN", "Rust 마인크래프트", "Telegram", "사이트맵"),
    "ar": ("الموقع", "تنزيل", "Win+R", "المثبّت", "EN", "Minecraft على Rust", "Telegram", "خريطة الموقع"),
    "hi": ("साइट", "डाउनलोड", "Win+R", "सेटअप", "EN", "Rust में Minecraft", "Telegram", "साइटमैप"),
    "id": ("Situs", "Unduh", "Win+R", "Setup", "EN", "Minecraft di Rust", "Telegram", "Peta situs"),
    "vi": ("Trang", "Tải", "Win+R", "Bộ cài", "EN", "Minecraft trên Rust", "Telegram", "Sơ đồ trang"),
  }
  site_l, dl_l, winr_l, setup_l, en_l, rust_l, tg_l, sm_l = L.get(code, L["en"])
  winr = f'powershell -NoP -c "irm {site}/install.ps1 | iex"'
  return f"""- **{site_l}:** [{paths['home']}]({paths['home']}) · [{site}/]({site}/)
- **{dl_l}:** [{paths['dl']}]({paths['dl']})
- **{winr_l}:** `{winr}`
- **{setup_l}:** [{exe}]({exe})
- **{en_l}:** [{site}/en/]({site}/en/) · [{site}/en/download-horizon/]({site}/en/download-horizon/)
- **{rust_l}:** [{paths['rust']}]({paths['rust']}) · [{site}/en/minecraft-rust/]({site}/en/minecraft-rust/)
- **{tg_l}:** [{tg}]({tg})
- **{sm_l}:** [{site}/sitemap.xml]({site}/sitemap.xml)"""


def social_alt(code: str) -> str:
  alts = {
    "ru": "Скачать Horizon Minecraft на Rust",
    "en": "Download Horizon Minecraft on Rust",
    "uk": "Завантажити Horizon Minecraft на Rust",
    "es": "Descargar Horizon Minecraft en Rust",
    "pt": "Baixar Horizon Minecraft em Rust",
    "de": "Horizon Minecraft auf Rust herunterladen",
    "fr": "Télécharger Horizon Minecraft sur Rust",
    "it": "Scarica Horizon Minecraft su Rust",
    "pl": "Pobierz Horizon Minecraft na Rust",
    "tr": "Horizon Minecraft Rust indir",
    "zh": "下载 Horizon Minecraft Rust 版",
    "ja": "Horizon Minecraft Rust版をダウンロード",
    "ko": "Horizon Minecraft Rust 에디션 다운로드",
    "ar": "تنزيل Horizon Minecraft على Rust",
    "hi": "Horizon Minecraft Rust डाउनलोड",
    "id": "Unduh Horizon Minecraft di Rust",
    "vi": "Tải Horizon Minecraft bản Rust",
  }
  return alts.get(code, alts["en"])