# -*- coding: utf-8 -*-
"""TOC, compare table, servers block, bilingual sitemap, localized SEO footer."""

from __future__ import annotations


def _ru(fmt: dict) -> dict:
    S, E, R, L = fmt["SITE"], fmt["EXE"], fmt["REL"], fmt["LATEST"]
    return {
        "maint_banner": (
            f'<p align="center"><em>Обновлено 2026-11-16: лаунчер <strong>{L}</strong>, LGPL, Win+R, UAC. '
            f'Скачивание только с <a href="{S}/">horizonlauncher.net</a>.</em></p>'
        ),
        "social_banner": (
            f'[![Скачать Horizon Minecraft на Rust]({S}/media/social-preview.jpg)]({S}/)'
        ),
        "toc_h": "Содержание",
        "toc": (
            "1. [Что такое Horizon Minecraft](#что-такое-horizon-minecraft)\n"
            "2. [Скачать Horizon бесплатно (Windows)](#скачать-horizon-бесплатно-windows)\n"
            "3. [Как установить лаунчер Horizon](#как-установить-лаунчер-horizon--два-способа)\n"
            "4. [Возможности Horizon Minecraft](#возможности-horizon-minecraft-клиент-java-на-rust)\n"
            "5. [Minecraft на Rust — зачем это](#minecraft-на-rust--зачем-это)\n"
            "6. [Лаунчер vs ваниль vs другие клиенты](#лаунчер-vs-ваниль-vs-другие-клиенты)\n"
            "7. [Сервера, моды, FPS](#сервера-моды-fps)\n"
            "8. [FAQ](#faq)\n"
            "9. [Все страницы сайта](#все-страницы-сайта)\n"
            "10. [English — Download Horizon](#english--download-horizon-minecraft-launcher)\n"
            "11. [SEO-теги](#seo-теги-и-ключевые-запросы)"
        ),
        "compare_h": "Лаунчер vs ваниль vs другие клиенты",
        "compare_body": f"""| | Официальный Minecraft Launcher | Prism / MultiMC / другие Java-лаунчеры | **Horizon (этот пост)** |
|---|---|---|---|
| Скачать | minecraft.net | GitHub лаунчеров | **[{S}]({S}/)** |
| Клиент | JVM (vanilla / Fabric) | JVM | **Rust-клиент (Minecraft Rust Edition)** |
| Цель | лицензия и ваниль | модпаки | **FPS + нативный клиент Windows** |
| Установка | свой setup | свой setup | **horizon-launcher-setup.exe** |
| Для кого | все | моддеры | кому нужен **скачать Horizon Minecraft на Rust** |

Horizon **не заменяет** лицензию. Если вы ищете «скачать Minecraft без лицензии» — это не тот репозиторий. Здесь: **скачать лаунчер Horizon** с **[horizonlauncher.net]({S}/)**.""",
        "servers_h": "Сервера, моды, FPS",
        "servers_body": f"""- **Сервера Minecraft Java:** [{S}/server/]({S}/server/) · [EN]({S}/en/server/)
- **Моды** `.hnmod`: [{S}/mods/]({S}/mods/) · [Distant Horizons]({S}/distant-horizons/) · [Create]({S}/create-mod/) · [шейдеры]({S}/shaders/)
- **FPS:** [{S}/performance/]({S}/performance/) · **FAQ:** [{S}/faq/]({S}/faq/) · **LGPL:** [{S}/legal/]({S}/legal/)

### Топ запросов

`скачать Horizon Minecraft` · `лаунчер Horizon Windows 11` · `Minecraft Rust Edition` · `Horizon {L}` · `LGPL Horizon` · `Distant Horizons Horizon` · `Horizon shaders API 0.2` · `Win+R Horizon`""",
        "bilingual_h": "Все страницы сайта (внутренние ссылки)",
        "bilingual_body": f"""**Русский:** [{S}/]({S}/) · [download-horizon]({S}/download-horizon/) · [install]({S}/install-horizon/) · [minecraft-rust]({S}/minecraft-rust/) · [launcher]({S}/launcher/) · [gallery]({S}/gallery/) · [llms.txt]({S}/llms.txt) · [Telegram](https://t.me/horizonlauncher) · [{E}]({E})

**English:** [{S}/en/]({S}/en/) · [download]({S}/en/download-horizon/) · [install]({S}/en/install-horizon/) · [minecraft-rust]({S}/en/minecraft-rust/) · [legal]({S}/en/legal/)""",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "mirror_body": f"""**Horizon** is a free **Windows Minecraft launcher** plus a **Minecraft Java client in Rust** (Minecraft Rust Edition). **Canonical download:** [{S}/en/]({S}/en/) · [{S}/en/download-horizon/]({S}/en/download-horizon/) · [{E}]({E}) · launcher **{L}**. Unofficial — not Mojang/Microsoft. News: [t.me/horizonlauncher](https://t.me/horizonlauncher).""",
        "seo_kw_block": (
            "`скачать Horizon` `скачать Horizon Minecraft` `Horizon {L}` `horizon-launcher-setup.exe` "
            "`horizonlauncher.net` `Minecraft Rust Edition` `download Horizon` `Horizon launcher github` "
            "`Distant Horizons Horizon` `Create mod Horizon` `Horizon shaders` `LGPL Horizon` `Win+R Horizon`"
        ).format(L=L),
        "seo_links_h": "Скачать / Win+R / setup.exe",
        "seo_cta": f"**Скачать:** [{S}]({S}/) · [download-horizon]({S}/download-horizon/) · [{E}]({E})",
    }


def _en(fmt: dict) -> dict:
    S, E, R, L = fmt["SITE"], fmt["EXE"], fmt["REL"], fmt["LATEST"]
    return {
        "maint_banner": (
            f'<p align="center"><em>Updated 2026-11-16: launcher <strong>{L}</strong>, LGPL, Win+R, UAC. '
            f'Download only from <a href="{S}/en/">horizonlauncher.net</a>.</em></p>'
        ),
        "social_banner": (
            f'[![Download Horizon Minecraft on Rust]({S}/media/social-preview.jpg)]({S}/en/)'
        ),
        "toc_h": "Contents",
        "toc": (
            "1. [What is Horizon](#what-is-horizon-minecraft)\n"
            "2. [Download Horizon free](#download-horizon-free-windows)\n"
            "3. [Install the launcher](#how-to-install-horizon--two-methods)\n"
            "4. [Horizon features](#horizon-minecraft-features-java-client-in-rust)\n"
            "5. [Why Minecraft on Rust](#why-minecraft-on-rust)\n"
            "6. [Launcher comparison](#launcher-vs-vanilla-vs-other-launchers)\n"
            "7. [Servers, mods, FPS](#servers-mods-fps)\n"
            "8. [FAQ](#faq)\n"
            "9. [Site map](#all-site-pages)\n"
            "10. [Русский — Скачать Horizon](#русский--скачать-horizon-minecraft-launcher)\n"
            "11. [SEO tags](#seo-tags-and-search-queries)"
        ),
        "compare_h": "Launcher vs vanilla vs other launchers",
        "compare_body": f"""| | Official Minecraft Launcher | Prism / MultiMC / JVM launchers | **Horizon (this repo)** |
|---|---|---|---|
| Download | minecraft.net | GitHub | **[{S}/en/]({S}/en/)** |
| Client | JVM | JVM | **Rust client (Minecraft Rust Edition)** |
| Focus | license & vanilla | modpacks | **FPS + native Windows client** |
| Install | own setup | own setup | **horizon-launcher-setup.exe** |

Unofficial client — use a legitimate Java license. Download only **horizonlauncher.net**.""",
        "servers_h": "Servers, mods, FPS",
        "servers_body": f"""- **Java servers:** [{S}/en/server/]({S}/en/server/)
- **Mods** `.hnmod`: [{S}/en/mods/]({S}/en/mods/) · [Distant Horizons]({S}/en/distant-horizons/) · [Create]({S}/en/create-mod/) · [shaders]({S}/en/shaders/)
- **Performance:** [{S}/en/performance/]({S}/en/performance/) · **Legal LGPL:** [{S}/en/legal/]({S}/en/legal/)

### Top searches

`download Horizon Minecraft` · `Horizon launcher Windows` · `Minecraft Rust Edition` · `Horizon {L}` · `Win+R Horizon` · `Horizon shaders API 0.2`""",
        "bilingual_h": "All site pages (internal links)",
        "bilingual_body": f"""**English:** [{S}/en/]({S}/en/) · [download]({S}/en/download-horizon/) · [install]({S}/en/install-horizon/) · [gallery]({S}/gallery/) · [{E}]({E}) · [Telegram](https://t.me/horizonlauncher)

**Русский:** [{S}/]({S}/) · [скачать]({S}/download-horizon/) · [установить]({S}/install-horizon/) · [minecraft-rust]({S}/minecraft-rust/)""",
        "mirror_h": "Русский — Скачать Horizon Minecraft launcher",
        "mirror_body": f"""**Horizon** — бесплатный **лаунчер Minecraft Windows** и **клиент Java на Rust**. Канон: [{S}/]({S}/) · [{S}/download-horizon/]({S}/download-horizon/) · **[{E}]({E})** · версия **{L}**. Не Mojang/Microsoft.""",
        "seo_kw_block": (
            "`download Horizon` `download Horizon Minecraft` `Horizon launcher Windows` `Minecraft on Rust` "
            f"`Horizon {L}` `horizon-launcher-setup.exe` `horizonlauncher.net` `Horizon launcher github` "
            "`Distant Horizons Horizon` `LGPL Horizon` `Win+R Horizon` `скачать Horizon` `Minecraft Rust Edition`"
        ),
        "seo_links_h": "Download / Win+R / setup.exe",
        "seo_cta": f"**Download Horizon:** [{S}/en/]({S}/en/) · [download]({S}/en/download-horizon/) · [{E}]({E})",
    }


def _generic(code: str, fmt: dict) -> dict:
    """Localized headers + EN/RU sitemap; body mostly EN for parity."""
    S, E, L = fmt["SITE"], fmt["EXE"], fmt["LATEST"]
    prefix = "" if code in ("ru", "uk") else f"{S}/{code}/"
    if code in ("ru", "uk"):
        home, dl = f"{S}/", f"{S}/download-horizon/"
    else:
        home = f"{S}/{code}/" if code not in ("en",) else f"{S}/en/"
        dl = f"{S}/{code}/download-horizon/" if code not in ("en",) else f"{S}/en/download-horizon/"

    titles = {
        "uk": ("Зміст", "Лаунчер vs ваніль", "Сервери, моди, FPS", "Усі сторінки сайту"),
        "es": ("Contenido", "Lanzador vs vanilla", "Servidores, mods, FPS", "Páginas del sitio"),
        "pt": ("Conteúdo", "Launcher vs vanilla", "Servidores, mods, FPS", "Páginas do site"),
        "de": ("Inhalt", "Launcher vs Vanilla", "Server, Mods, FPS", "Seiten der Website"),
        "fr": ("Sommaire", "Launcher vs vanilla", "Serveurs, mods, FPS", "Pages du site"),
        "it": ("Indice", "Launcher vs vanilla", "Server, mod, FPS", "Pagine del sito"),
        "pl": ("Spis treści", "Launcher vs vanilla", "Serwery, mody, FPS", "Strony serwisu"),
        "tr": ("İçindekiler", "Launcher vs vanilla", "Sunucular, modlar, FPS", "Site sayfaları"),
        "zh": ("目录", "启动器对比", "服务器、模组、FPS", "网站页面"),
        "ja": ("目次", "ランチャー比較", "サーバー・MOD・FPS", "サイト内リンク"),
        "ko": ("목차", "런처 비교", "서버, 모드, FPS", "사이트 페이지"),
        "ar": ("المحتويات", "مقارنة المشغّل", "السيرفرات والمودات", "صفحات الموقع"),
        "hi": ("विषय सूची", "लॉन्चर तुलना", "सर्वर, मॉड, FPS", "साइट पेज"),
        "id": ("Daftar isi", "Launcher vs vanilla", "Server, mod, FPS", "Halaman situs"),
        "vi": ("Mục lục", "So sánh launcher", "Máy chủ, mod, FPS", "Trang web"),
    }
    toc_h, compare_h, servers_h, bilingual_h = titles.get(
        code, ("Contents", "Launcher comparison", "Servers, mods, FPS", "Site pages")
    )

    compare_body = f"""| | Official launcher | JVM launchers | **Horizon** |
|---|---|---|---|
| Download | minecraft.net | GitHub | **[{home}]({home})** |
| Client | JVM | JVM | **Rust (Minecraft Rust Edition)** |
| Setup | vendor installer | vendor | **[{E}]({E})** |

Canonical download: **horizonlauncher.net** only."""

    servers_body = f"""- **Servers / mods / FPS / legal:** [{home}]({home}) · [{dl}]({dl})
- **Distant Horizons · Create · shaders:** [{S}/en/distant-horizons/]({S}/en/distant-horizons/) (EN guides)
- **Releases {L}:** [{fmt['REL']}]({fmt['REL']})"""

    bilingual_body = f"""**{code.upper()} / local:** [{home}]({home}) · [{dl}]({dl}) · [{E}]({E})

**EN:** [{S}/en/]({S}/en/) · **RU:** [{S}/]({S}/) · [sitemap]({S}/sitemap.xml) · [Telegram](https://t.me/horizonlauncher)"""

    return {
        "maint_banner": (
            f'<p align="center"><em>Launcher <strong>{L}</strong> · LGPL · Win+R · UAC · '
            f'<a href="{home}">horizonlauncher.net</a></em></p>'
        ),
        "social_banner": f'[![Horizon Minecraft]({S}/media/social-preview.jpg)]({home})',
        "toc_h": toc_h,
        "toc": (
            f"1. [{compare_h}](#{compare_h.lower().replace(' ', '-').replace(',', '')})\n"
            f"2. [FAQ](#faq)\n"
            f"3. [{bilingual_h}](#{bilingual_h.lower().replace(' ', '-')})"
        ),
        "compare_h": compare_h,
        "compare_body": compare_body,
        "servers_h": servers_h,
        "servers_body": servers_body,
        "bilingual_h": bilingual_h,
        "bilingual_body": bilingual_body,
        "mirror_h": "",
        "mirror_body": "",
        "seo_kw_block": (
            f"`download Horizon` `Horizon {L}` `horizonlauncher.net` `Minecraft Rust Edition` "
            f"`horizon-launcher-setup.exe` `Win+R Horizon` `LGPL Horizon`"
        ),
        "seo_links_h": "Download / Win+R / setup.exe",
        "seo_cta": f"**Horizon:** [{home}]({home}) · [{E}]({E})",
    }


def seo_footer_localized(t: dict, seo: str, dl: str, *, SITE: str, EXE: str, LATEST: str, TG: str) -> str:
    links = f"""### {t.get("seo_links_h", "Links")}

- Site: [{SITE}/]({SITE}/)
- Download: [{dl}]({dl})
- Win+R: `powershell -NoP -c "irm {SITE}/install.ps1 | iex"`
- Setup: [{EXE}]({EXE})
- EN: [{SITE}/en/]({SITE}/en/)
- Minecraft on Rust: [{SITE}/minecraft-rust/]({SITE}/minecraft-rust/) · [{SITE}/en/minecraft-rust/]({SITE}/en/minecraft-rust/)
- Telegram: [{TG}]({TG})
- Sitemap: [{SITE}/sitemap.xml]({SITE}/sitemap.xml)
"""
    kw = t.get("seo_kw_block", seo)
    cta = t.get("seo_cta", f"[{SITE}]({SITE}) · [{EXE}]({EXE})")
    return f"""## {t['seo_h']}

{kw}

{links}

{cta}
"""


def apply_readme_extras(T: dict, *, SITE: str, EXE: str, REL: str, LATEST: str) -> None:
    fmt = dict(SITE=SITE, EXE=EXE, REL=REL, LATEST=LATEST)
    for code in T:
        if code == "ru":
            T[code].update(_ru(fmt))
        elif code == "en":
            T[code].update(_en(fmt))
        else:
            T[code].update(_generic(code, fmt))

    # Extra FAQ (all locales)
    extra = [
        (
            "Win 7 / macOS / Linux?",
            f"Official setup targets **Windows 10/11 x64**. See [{SITE}/download-horizon/]({SITE}/download-horizon/).",
        ),
        (
            "Why this GitHub README?",
            f"So searches like «Horizon launcher github» lead to canonical **[horizonlauncher.net]({SITE}/)**.",
        ),
    ]
    faq_en = [
        (
            "Windows 7 / macOS / Linux?",
            f"Setup targets **Windows 10/11 x64**. See [{SITE}/en/download-horizon/]({SITE}/en/download-horizon/).",
        ),
        (
            "Russian version?",
            f"[{SITE}/]({SITE}/) — скачать Horizon.",
        ),
        (
            "Why GitHub if the site exists?",
            f"So «Horizon Minecraft GitHub» queries point to **[horizonlauncher.net]({SITE}/en/)**.",
        ),
    ]
    faq_ru = [
        ("Windows 7 / macOS / Linux?", f"Setup для **Windows 10/11 x64**. Актуально: [{SITE}/download-horizon/]({SITE}/download-horizon/)."),
        ("Где английская версия?", f"[{SITE}/en/]({SITE}/en/) — Download Horizon."),
        (
            "Зачем GitHub, если есть сайт?",
            f"Чтобы запросы «Horizon Minecraft GitHub» вели на **[horizonlauncher.net]({SITE}/)**.",
        ),
    ]
    if "ru" in T:
        T["ru"]["faq"] = list(T["ru"]["faq"]) + faq_ru
    for code in T:
        if code == "ru":
            continue
        if code == "en":
            T[code]["faq"] = list(T[code]["faq"]) + faq_en
        else:
            T[code]["faq"] = list(T[code]["faq"]) + extra