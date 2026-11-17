# -*- coding: utf-8 -*-
"""TOC, compare table, servers block, bilingual sitemap, localized SEO footer."""

from __future__ import annotations

import re
import unicodedata

from _locale_strings import (
  bilingual_section,
  faq_extra,
  mirror_block,
  seo_footer_lines,
  social_alt,
)


def github_slug(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[·—:]+", " ", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^\w\-]", "", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def site_paths(code: str, site: str) -> dict[str, str]:
    if code in ("ru", "uk"):
        root = site
    elif code == "en":
        root = f"{site}/en"
    else:
        root = f"{site}/{code}"
    return {
        "home": f"{root}/",
        "dl": f"{root}/download-horizon/",
        "inst": f"{root}/install-horizon/",
        "rust": f"{root}/minecraft-rust/",
        "perf": f"{root}/performance/",
        "mods": f"{root}/mods/",
        "serv": f"{root}/server/",
        "faq_p": f"{root}/faq/",
        "legal": f"{root}/legal/",
        "dh": f"{root}/distant-horizons/",
        "create": f"{root}/create-mod/",
        "shaders": f"{root}/shaders/",
        "gallery": f"{site}/gallery/",
        "launcher": f"{root}/launcher/",
    }


def feat_heading(t: dict) -> str:
    line = (t.get("feat_body") or "").split("\n", 1)[0].strip()
    return line[2:].strip() if line.startswith("##") else "Horizon features"


def build_toc(t: dict) -> str:
    feat = feat_heading(t)
    items: list[str] = [
        t["what_h"],
        t["dl_h"],
        t["paths_h"],
        feat,
        t["rust_h"],
        t["compare_h"],
        t["servers_h"],
        t["faq_h"],
        t["bilingual_h"],
    ]
    if t.get("mirror_h"):
        items.append(t["mirror_h"])
    items.append(t["seo_h"])
    return "\n".join(f"{i}. [{h}](#{github_slug(h)})" for i, h in enumerate(items, 1))


def _compare_body(paths: dict[str, str], e: str, *, rows: dict[str, str]) -> str:
    h = rows
    return f"""| | {h['c1']} | {h['c2']} | **Horizon** |
|---|---|---|---|
| {h['r_dl']} | minecraft.net | GitHub | **[{paths['home']}]({paths['home']})** |
| {h['r_client']} | JVM | JVM | **Rust ({h['rust_ed']})** |
| {h['r_goal']} | {h['v1']} | {h['v2']} | **FPS + {h['native']}** |
| {h['r_setup']} | setup | setup | **[{e}]({e})** |

{h['foot']}"""


def _servers_body(paths: dict[str, str], rel: str, latest: str, *, block: dict[str, str]) -> str:
    b = block
    return f"""- **{b['serv']}:** [{paths['serv']}]({paths['serv']})
- **{b['mods']}** `.hnmod`: [{paths['mods']}]({paths['mods']}) · [Distant Horizons]({paths['dh']}) · [Create]({paths['create']}) · [{b['sh']}]({paths['shaders']})
- **{b['fps']}:** [{paths['perf']}]({paths['perf']}) · **FAQ:** [{paths['faq_p']}]({paths['faq_p']}) · **LGPL:** [{paths['legal']}]({paths['legal']})

### {b['top_h']}

{b['top_kw'].format(L=latest)} · [{b['rel']}]({rel})"""


# Localized copy for compare rows + servers + headers
_LOCALE: dict[str, dict] = {
    "uk": {
        "toc_h": "Зміст",
        "compare_h": "Лаунчер vs ваніль vs інші клієнти",
        "servers_h": "Сервери, моди, FPS",
        "bilingual_h": "Усі сторінки сайту",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Завантажити / Win+R / setup.exe",
        "maint": "Оновлено 2026-11-17: лаунчер <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Офіційний Minecraft Launcher",
            "c2": "Prism / MultiMC",
            "r_dl": "Завантажити",
            "r_client": "Клієнт",
            "r_goal": "Мета",
            "r_setup": "Установка",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "ліцензія",
            "v2": "модпаки",
            "native": "нативний Windows-клієнт",
            "foot": "Неофіційний клієнт. Качайте лише **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Сервери Minecraft Java",
            "mods": "Моди",
            "sh": "шейдери",
            "fps": "FPS",
            "top_h": "Топ-запити",
            "top_kw": "`завантажити Horizon Minecraft` · `лаунчер Horizon Windows` · `Minecraft Rust Edition` · `Horizon {L}` · `Win+R Horizon`",
            "rel": "Релізи",
        },
        "seo_kw": "`завантажити Horizon` `лаунчер Horizon` `Minecraft на Rust` `Horizon {L}` `horizonlauncher.net` `LGPL Horizon` `download Horizon`",
        "seo_cta": "**Завантажити:**",
    },
    "es": {
        "toc_h": "Contenido",
        "compare_h": "Launcher vs vanilla vs otros clientes",
        "servers_h": "Servidores, mods, FPS",
        "bilingual_h": "Páginas del sitio",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Descargar / Win+R / setup.exe",
        "maint": "Actualizado 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher oficial de Minecraft",
            "c2": "Prism / MultiMC",
            "r_dl": "Descarga",
            "r_client": "Cliente",
            "r_goal": "Enfoque",
            "r_setup": "Instalación",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "licencia",
            "v2": "modpacks",
            "native": "cliente nativo Windows",
            "foot": "Cliente no oficial. Descarga solo en **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Servidores Minecraft Java",
            "mods": "Mods",
            "sh": "shaders",
            "fps": "Rendimiento",
            "top_h": "Búsquedas frecuentes",
            "top_kw": "`descargar Horizon Minecraft` · `launcher Horizon Windows` · `Minecraft Rust Edition` · `Horizon {L}` · `Win+R Horizon`",
            "rel": "Releases",
        },
        "seo_kw": "`descargar Horizon` `launcher Horizon` `Minecraft en Rust` `Horizon {L}` `horizonlauncher.net` `LGPL Horizon` `download Horizon`",
        "seo_cta": "**Descargar:**",
    },
    "pt": {
        "toc_h": "Conteúdo",
        "compare_h": "Launcher vs vanilla vs outros clientes",
        "servers_h": "Servidores, mods, FPS",
        "bilingual_h": "Páginas do site",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Baixar / Win+R / setup.exe",
        "maint": "Atualizado 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher oficial Minecraft",
            "c2": "Prism / MultiMC",
            "r_dl": "Download",
            "r_client": "Cliente",
            "r_goal": "Foco",
            "r_setup": "Instalação",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "licença",
            "v2": "modpacks",
            "native": "cliente nativo Windows",
            "foot": "Cliente não oficial. Baixe apenas em **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Servidores Minecraft Java",
            "mods": "Mods",
            "sh": "shaders",
            "fps": "Desempenho",
            "top_h": "Buscas comuns",
            "top_kw": "`baixar Horizon Minecraft` · `launcher Horizon Windows` · `Minecraft Rust Edition` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`baixar Horizon` `launcher Horizon` `Minecraft em Rust` `Horizon {L}` `horizonlauncher.net` `download Horizon`",
        "seo_cta": "**Baixar:**",
    },
    "de": {
        "toc_h": "Inhalt",
        "compare_h": "Launcher vs Vanilla vs andere Clients",
        "servers_h": "Server, Mods, FPS",
        "bilingual_h": "Seiten der Website",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Download / Win+R / setup.exe",
        "maint": "Stand 2026-11-17: Launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Offizieller Minecraft Launcher",
            "c2": "Prism / MultiMC",
            "r_dl": "Download",
            "r_client": "Client",
            "r_goal": "Ziel",
            "r_setup": "Installation",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "Lizenz",
            "v2": "Modpacks",
            "native": "nativer Windows-Client",
            "foot": "Inoffizieller Client. Nur **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Minecraft-Java-Server",
            "mods": "Mods",
            "sh": "Shader",
            "fps": "Performance",
            "top_h": "Top-Suchen",
            "top_kw": "`Horizon herunterladen` · `Horizon Launcher Windows` · `Minecraft Rust Edition` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`Horizon herunterladen` `Horizon Launcher` `Minecraft auf Rust` `Horizon {L}` `horizonlauncher.net` `download Horizon`",
        "seo_cta": "**Download:**",
    },
    "fr": {
        "toc_h": "Sommaire",
        "compare_h": "Launcher vs vanilla vs autres clients",
        "servers_h": "Serveurs, mods, FPS",
        "bilingual_h": "Pages du site",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Télécharger / Win+R / setup.exe",
        "maint": "Mis à jour 2026-11-17 : launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher Minecraft officiel",
            "c2": "Prism / MultiMC",
            "r_dl": "Téléchargement",
            "r_client": "Client",
            "r_goal": "Objectif",
            "r_setup": "Installation",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "licence",
            "v2": "modpacks",
            "native": "client Windows natif",
            "foot": "Client non officiel. Téléchargez uniquement sur **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Serveurs Minecraft Java",
            "mods": "Mods",
            "sh": "shaders",
            "fps": "Performances",
            "top_h": "Recherches fréquentes",
            "top_kw": "`télécharger Horizon Minecraft` · `launcher Horizon Windows` · `Horizon {L}` · `Minecraft Rust Edition`",
            "rel": "Releases",
        },
        "seo_kw": "`télécharger Horizon` `launcher Horizon` `Minecraft sur Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**Télécharger :**",
    },
    "it": {
        "toc_h": "Indice",
        "compare_h": "Launcher vs vanilla vs altri client",
        "servers_h": "Server, mod, FPS",
        "bilingual_h": "Pagine del sito",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Scarica / Win+R / setup.exe",
        "maint": "Aggiornato 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher Minecraft ufficiale",
            "c2": "Prism / MultiMC",
            "r_dl": "Download",
            "r_client": "Client",
            "r_goal": "Scopo",
            "r_setup": "Installazione",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "licenza",
            "v2": "modpack",
            "native": "client Windows nativo",
            "foot": "Client non ufficiale. Scarica solo da **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Server Minecraft Java",
            "mods": "Mod",
            "sh": "shader",
            "fps": "Prestazioni",
            "top_h": "Ricerche comuni",
            "top_kw": "`scaricare Horizon Minecraft` · `launcher Horizon Windows` · `Horizon {L}`",
            "rel": "Release",
        },
        "seo_kw": "`scaricare Horizon` `launcher Horizon` `Minecraft su Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**Scarica:**",
    },
    "pl": {
        "toc_h": "Spis treści",
        "compare_h": "Launcher vs vanilla vs inne klienty",
        "servers_h": "Serwery, mody, FPS",
        "bilingual_h": "Strony serwisu",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Pobierz / Win+R / setup.exe",
        "maint": "Aktualizacja 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Oficjalny launcher Minecraft",
            "c2": "Prism / MultiMC",
            "r_dl": "Pobieranie",
            "r_client": "Klient",
            "r_goal": "Cel",
            "r_setup": "Instalacja",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "licencja",
            "v2": "modpacki",
            "native": "natywny klient Windows",
            "foot": "Nieoficjalny klient. Pobieraj tylko z **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Serwery Minecraft Java",
            "mods": "Mody",
            "sh": "shadery",
            "fps": "Wydajność",
            "top_h": "Popularne wyszukiwania",
            "top_kw": "`pobierz Horizon Minecraft` · `launcher Horizon Windows` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`pobierz Horizon` `launcher Horizon` `Minecraft na Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**Pobierz:**",
    },
    "tr": {
        "toc_h": "İçindekiler",
        "compare_h": "Launcher vs vanilla vs diğer istemciler",
        "servers_h": "Sunucular, modlar, FPS",
        "bilingual_h": "Site sayfaları",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "İndir / Win+R / setup.exe",
        "maint": "Güncelleme 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Resmi Minecraft Launcher",
            "c2": "Prism / MultiMC",
            "r_dl": "İndirme",
            "r_client": "İstemci",
            "r_goal": "Odak",
            "r_setup": "Kurulum",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "lisans",
            "v2": "modpack",
            "native": "yerel Windows istemcisi",
            "foot": "Resmi olmayan istemci. Yalnızca **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Minecraft Java sunucuları",
            "mods": "Modlar",
            "sh": "shader",
            "fps": "Performans",
            "top_h": "Popüler aramalar",
            "top_kw": "`Horizon indir` · `Horizon launcher Windows` · `Horizon {L}` · `Minecraft Rust Edition`",
            "rel": "Sürümler",
        },
        "seo_kw": "`Horizon indir` `Horizon launcher` `Rust Minecraft` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**İndir:**",
    },
    "zh": {
        "toc_h": "目录",
        "compare_h": "启动器对比（官方 / JVM / Horizon）",
        "servers_h": "服务器、模组、FPS",
        "bilingual_h": "网站页面链接",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "下载 / Win+R / setup.exe",
        "maint": "更新 2026-11-17：启动器 <strong>{L}</strong>，LGPL，Win+R，UAC。",
        "compare_rows": {
            "c1": "官方 Minecraft 启动器",
            "c2": "Prism / MultiMC",
            "r_dl": "下载",
            "r_client": "客户端",
            "r_goal": "定位",
            "r_setup": "安装",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "正版",
            "v2": "整合包",
            "native": "Windows 原生客户端",
            "foot": "非官方客户端。仅从 **horizonlauncher.net** 下载。",
        },
        "servers": {
            "serv": "Minecraft Java 服务器",
            "mods": "模组",
            "sh": "光影",
            "fps": "性能",
            "top_h": "常见搜索",
            "top_kw": "`下载 Horizon Minecraft` · `Horizon 启动器 Windows` · `Horizon {L}` · `Minecraft Rust Edition`",
            "rel": "发布页",
        },
        "seo_kw": "`下载 Horizon` `Horizon 启动器` `Rust 版 Minecraft` `Horizon {L}` `horizonlauncher.net` `download Horizon`",
        "seo_cta": "**下载：**",
    },
    "ja": {
        "toc_h": "目次",
        "compare_h": "ランチャー比較（公式 / JVM / Horizon）",
        "servers_h": "サーバー・MOD・FPS",
        "bilingual_h": "サイト内リンク",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "ダウンロード / Win+R / setup.exe",
        "maint": "更新 2026-11-17：ランチャー <strong>{L}</strong>、LGPL、Win+R、UAC。",
        "compare_rows": {
            "c1": "公式 Minecraft ランチャー",
            "c2": "Prism / MultiMC",
            "r_dl": "入手",
            "r_client": "クライアント",
            "r_goal": "目的",
            "r_setup": "インストール",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "ライセンス",
            "v2": "modpack",
            "native": "Windows ネイティブ",
            "foot": "非公式クライアント。**horizonlauncher.net** のみ。",
        },
        "servers": {
            "serv": "Minecraft Java サーバー",
            "mods": "MOD",
            "sh": "シェーダー",
            "fps": "パフォーマンス",
            "top_h": "よくある検索",
            "top_kw": "`Horizon ダウンロード` · `Horizon ランチャー Windows` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`Horizon ダウンロード` `Horizon ランチャー` `Rust Minecraft` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**ダウンロード：**",
    },
    "ko": {
        "toc_h": "목차",
        "compare_h": "런처 비교 (공식 / JVM / Horizon)",
        "servers_h": "서버, 모드, FPS",
        "bilingual_h": "사이트 페이지",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "다운로드 / Win+R / setup.exe",
        "maint": "업데이트 2026-11-17: 런처 <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "공식 Minecraft 런처",
            "c2": "Prism / MultiMC",
            "r_dl": "다운로드",
            "r_client": "클라이언트",
            "r_goal": "목적",
            "r_setup": "설치",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "라이선스",
            "v2": "모드팩",
            "native": "Windows 네이티브",
            "foot": "비공식 클라이언트. **horizonlauncher.net** 만 사용.",
        },
        "servers": {
            "serv": "Minecraft Java 서버",
            "mods": "모드",
            "sh": "셰이더",
            "fps": "성능",
            "top_h": "자주 찾는 검색",
            "top_kw": "`Horizon 다운로드` · `Horizon 런처 Windows` · `Horizon {L}`",
            "rel": "릴리스",
        },
        "seo_kw": "`Horizon 다운로드` `Horizon 런처` `Rust 마인크래프트` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**다운로드:**",
    },
    "ar": {
        "toc_h": "المحتويات",
        "compare_h": "مقارنة المشغّلات",
        "servers_h": "السيرفرات والمودات وFPS",
        "bilingual_h": "صفحات الموقع",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "تنزيل / Win+R / setup.exe",
        "maint": "تحديث 2026-11-17: المشغّل <strong>{L}</strong>، LGPL، Win+R، UAC.",
        "compare_rows": {
            "c1": "مشغّل Minecraft الرسمي",
            "c2": "Prism / MultiMC",
            "r_dl": "التنزيل",
            "r_client": "العميل",
            "r_goal": "الهدف",
            "r_setup": "التثبيت",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "الترخيص",
            "v2": "حزم المود",
            "native": "عميل Windows أصلي",
            "foot": "عميل غير رسمي. التنزيل من **horizonlauncher.net** فقط.",
        },
        "servers": {
            "serv": "سيرفرات Minecraft Java",
            "mods": "مودات",
            "sh": "الشيدر",
            "fps": "الأداء",
            "top_h": "عمليات بحث شائعة",
            "top_kw": "`تنزيل Horizon Minecraft` · `Horizon launcher Windows` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`تنزيل Horizon` `Horizon launcher` `Minecraft على Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**تنزيل:**",
    },
    "hi": {
        "toc_h": "विषय सूची",
        "compare_h": "लॉन्चर तुलना",
        "servers_h": "सर्वर, मॉड, FPS",
        "bilingual_h": "साइट पेज",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "डाउनलोड / Win+R / setup.exe",
        "maint": "अपडेट 2026-11-17: लॉन्चर <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "आधिकारिक Minecraft Launcher",
            "c2": "Prism / MultiMC",
            "r_dl": "डाउनलोड",
            "r_client": "क्लाइंट",
            "r_goal": "उद्देश्य",
            "r_setup": "इंस्टॉल",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "लाइसेंस",
            "v2": "modpack",
            "native": "Windows नेटिव क्लाइंट",
            "foot": "अनौपचारिक क्लाइंट। केवल **horizonlauncher.net**।",
        },
        "servers": {
            "serv": "Minecraft Java सर्वर",
            "mods": "मॉड",
            "sh": "शेडर",
            "fps": "प्रदर्शन",
            "top_h": "लोकप्रिय खोज",
            "top_kw": "`Horizon Minecraft डाउनलोड` · `Horizon launcher Windows` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`Horizon डाउनलोड` `Horizon launcher` `Rust में Minecraft` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**डाउनलोड:**",
    },
    "id": {
        "toc_h": "Daftar isi",
        "compare_h": "Perbandingan launcher",
        "servers_h": "Server, mod, FPS",
        "bilingual_h": "Halaman situs",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Unduh / Win+R / setup.exe",
        "maint": "Diperbarui 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher Minecraft resmi",
            "c2": "Prism / MultiMC",
            "r_dl": "Unduh",
            "r_client": "Klien",
            "r_goal": "Fokus",
            "r_setup": "Instalasi",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "lisensi",
            "v2": "modpack",
            "native": "klien Windows native",
            "foot": "Klien tidak resmi. Hanya **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Server Minecraft Java",
            "mods": "Mod",
            "sh": "shader",
            "fps": "Performa",
            "top_h": "Pencarian populer",
            "top_kw": "`unduh Horizon Minecraft` · `launcher Horizon Windows` · `Horizon {L}`",
            "rel": "Rilis",
        },
        "seo_kw": "`unduh Horizon` `launcher Horizon` `Minecraft di Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**Unduh:**",
    },
    "vi": {
        "toc_h": "Mục lục",
        "compare_h": "So sánh launcher",
        "servers_h": "Máy chủ, mod, FPS",
        "bilingual_h": "Trang web",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Tải / Win+R / setup.exe",
        "maint": "Cập nhật 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC.",
        "compare_rows": {
            "c1": "Launcher Minecraft chính thức",
            "c2": "Prism / MultiMC",
            "r_dl": "Tải",
            "r_client": "Client",
            "r_goal": "Mục tiêu",
            "r_setup": "Cài đặt",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "bản quyền",
            "v2": "modpack",
            "native": "client Windows native",
            "foot": "Client không chính thức. Chỉ **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Máy chủ Minecraft Java",
            "mods": "Mod",
            "sh": "shader",
            "fps": "Hiệu năng",
            "top_h": "Tìm kiếm phổ biến",
            "top_kw": "`tải Horizon Minecraft` · `launcher Horizon Windows` · `Horizon {L}`",
            "rel": "Releases",
        },
        "seo_kw": "`tải Horizon` `launcher Horizon` `Minecraft trên Rust` `Horizon {L}` `horizonlauncher.net`",
        "seo_cta": "**Tải:**",
    },
}


def _ru(fmt: dict) -> dict:
    S, E, R, L = fmt["SITE"], fmt["EXE"], fmt["REL"], fmt["LATEST"]
    paths = site_paths("ru", S)
    loc = {
        "toc_h": "Содержание",
        "compare_h": "Лаунчер vs ваниль vs другие клиенты",
        "servers_h": "Сервера, моды, FPS",
        "bilingual_h": "Все страницы сайта (внутренние ссылки)",
        "mirror_h": "English — Download Horizon Minecraft launcher",
        "seo_links_h": "Скачать / Win+R / setup.exe",
    }
    extra = _pack_locale(loc, paths, fmt, {
        "maint": f"Обновлено 2026-11-17: лаунчер <strong>{L}</strong>, LGPL, Win+R, UAC. Скачивание только с <a href=\"{S}/\">horizonlauncher.net</a>.",
        "compare_rows": {
            "c1": "Официальный Minecraft Launcher",
            "c2": "Prism / MultiMC / другие Java-лаунчеры",
            "r_dl": "Скачать",
            "r_client": "Клиент",
            "r_goal": "Цель",
            "r_setup": "Установка",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "лицензия и ваниль",
            "v2": "модпаки",
            "native": "нативный клиент Windows",
            "foot": f"Horizon **не заменяет** лицензию. Качайте с **[horizonlauncher.net]({S}/)**.",
        },
        "servers": {
            "serv": "Серверы Minecraft Java",
            "mods": "Моды",
            "sh": "шейдеры",
            "fps": "FPS",
            "top_h": "Топ запросов",
            "top_kw": "`скачать Horizon Minecraft` · `лаунчер Horizon Windows 11` · `Minecraft Rust Edition` · `Horizon {L}` · `LGPL Horizon` · `Win+R Horizon`",
            "rel": "Релизы GitHub",
        },
        "seo_kw": (
            "`скачать Horizon` `скачать Horizon Minecraft` `Horizon {L}` `horizon-launcher-setup.exe` "
            "`horizonlauncher.net` `download Horizon` `Distant Horizons Horizon` `LGPL Horizon` `Win+R Horizon`"
        ).format(L=L),
        "seo_cta": f"**Скачать:** [{S}]({S}/) · [download-horizon]({paths['dl']}) · [{E}]({E})",
        "bilingual_body": f"""**Русский:** [{paths['home']}]({paths['home']}) · [download-horizon]({paths['dl']}) · [install]({paths['inst']}) · [minecraft-rust]({paths['rust']}) · [gallery]({paths['gallery']}) · [llms.txt]({S}/llms.txt) · [Telegram](https://t.me/horizonlauncher)

**English:** [{S}/en/]({S}/en/) · [download]({S}/en/download-horizon/) · [legal]({S}/en/legal/)""",
        "mirror_body": "",
        "social": f"[![{social_alt('ru')}]({S}/media/social-preview.jpg)]({S}/)",
    })
    return extra


def _en(fmt: dict) -> dict:
    S, E, R, L = fmt["SITE"], fmt["EXE"], fmt["REL"], fmt["LATEST"]
    paths = site_paths("en", S)
    loc = {
        "toc_h": "Contents",
        "compare_h": "Launcher vs vanilla vs other launchers",
        "servers_h": "Servers, mods, FPS",
        "bilingual_h": "All site pages (internal links)",
        "mirror_h": "Русский — Скачать Horizon Minecraft launcher",
        "seo_links_h": "Download / Win+R / setup.exe",
    }
    return _pack_locale(loc, paths, fmt, {
        "maint": f"Updated 2026-11-17: launcher <strong>{L}</strong>, LGPL, Win+R, UAC. Download only from <a href=\"{paths['home']}\">horizonlauncher.net</a>.",
        "compare_rows": {
            "c1": "Official Minecraft Launcher",
            "c2": "Prism / MultiMC / JVM launchers",
            "r_dl": "Download",
            "r_client": "Client",
            "r_goal": "Focus",
            "r_setup": "Install",
            "rust_ed": "Minecraft Rust Edition",
            "v1": "license & vanilla",
            "v2": "modpacks",
            "native": "native Windows client",
            "foot": "Unofficial — use a legitimate Java license. Download only **horizonlauncher.net**.",
        },
        "servers": {
            "serv": "Minecraft Java servers",
            "mods": "Mods",
            "sh": "shaders",
            "fps": "Performance",
            "top_h": "Top searches",
            "top_kw": "`download Horizon Minecraft` · `Horizon launcher Windows` · `Horizon {L}` · `Win+R Horizon`",
            "rel": "GitHub Releases",
        },
        "seo_kw": (
            "`download Horizon` `download Horizon Minecraft` `Horizon launcher Windows` `Minecraft on Rust` "
            f"`Horizon {L}` `horizonlauncher.net` `скачать Horizon` `LGPL Horizon` `Win+R Horizon`"
        ),
        "seo_cta": f"**Download Horizon:** [{paths['home']}]({paths['home']}) · [{paths['dl']}]({paths['dl']}) · [{E}]({E})",
        "bilingual_body": f"""**English:** [{paths['home']}]({paths['home']}) · [download]({paths['dl']}) · [install]({paths['inst']}) · [gallery]({paths['gallery']}) · [{E}]({E})

**Русский:** [{S}/]({S}/) · [скачать]({S}/download-horizon/) · [minecraft-rust]({S}/minecraft-rust/)""",
        "mirror_body": "",
        "social": f"[![{social_alt('en')}]({S}/media/social-preview.jpg)]({paths['home']})",
    })


def _pack_locale(loc: dict, paths: dict, fmt: dict, data: dict) -> dict:
    S, E, R, L = fmt["SITE"], fmt["EXE"], fmt["REL"], fmt["LATEST"]
    seo_kw = data["seo_kw"]
    if "{L}" in seo_kw:
        seo_kw = seo_kw.format(L=L)
    return {
        "maint_banner": f'<p align="center"><em>{data["maint"]}</em></p>',
        "social_banner": data["social"],
        "toc_h": loc["toc_h"],
        "compare_h": loc["compare_h"],
        "compare_body": _compare_body(paths, E, rows=data["compare_rows"]),
        "servers_h": loc["servers_h"],
        "servers_body": _servers_body(paths, R, L, block=data["servers"]),
        "bilingual_h": loc["bilingual_h"],
        "bilingual_body": data["bilingual_body"],
        "mirror_h": loc["mirror_h"],
        "mirror_body": data.get("mirror_body", ""),
        "seo_kw_block": seo_kw,
        "seo_links_h": loc["seo_links_h"],
        "seo_cta": data["seo_cta"],
    }


def _locale(code: str, fmt: dict) -> dict:
    S, E = fmt["SITE"], fmt["EXE"]
    paths = site_paths(code, S)
    meta = _LOCALE[code]
    L = fmt["LATEST"]
    loc_heads = {
        "toc_h": meta["toc_h"],
        "compare_h": meta["compare_h"],
        "servers_h": meta["servers_h"],
        "bilingual_h": meta["bilingual_h"],
        "mirror_h": meta["mirror_h"],
        "seo_links_h": meta["seo_links_h"],
    }
    seo_kw = meta["seo_kw"].format(L=L)
    return _pack_locale(
        loc_heads,
        paths,
        fmt,
        {
            "maint": meta["maint"].format(L=L) + f' <a href="{paths["home"]}">horizonlauncher.net</a>.',
            "compare_rows": meta["compare_rows"],
            "servers": meta["servers"],
            "seo_kw": seo_kw,
            "seo_cta": f'{meta["seo_cta"]} [{paths["home"]}]({paths["home"]}) · [{paths["dl"]}]({paths["dl"]}) · [{E}]({E})',
            "bilingual_body": bilingual_section(code, S, paths, E),
            "mirror_body": "",
            "social": f"[![{social_alt(code)}]({S}/media/social-preview.jpg)]({paths['home']})",
        },
    )


def seo_footer_localized(t: dict, seo: str, dl: str, *, SITE: str, EXE: str, LATEST: str, TG: str) -> str:
    links = f"""### {t.get("seo_links_h", "Links")}

{t.get("seo_footer_lines", "")}
"""
    kw = t.get("seo_kw_block") or seo
    cta = t.get("seo_cta", f"[{SITE}]({SITE}) · [{EXE}]({EXE})")
    extra = " ".join(f"`{k}`" for k in t.get("seo", [])[:12])
    return f"""## {t['seo_h']}

{kw}

{extra}

{links}

{cta}
"""


def apply_readme_extras(T: dict, *, SITE: str, EXE: str, REL: str, LATEST: str, TG: str) -> None:
    fmt = dict(SITE=SITE, EXE=EXE, REL=REL, LATEST=LATEST)
    factories = {"ru": _ru, "en": _en}
    for code, t in T.items():
        pack = factories[code](fmt) if code in factories else _locale(code, fmt)
        t.update(pack)
        paths = site_paths(code, SITE)
        t["paths"] = paths
        mh, mb = mirror_block(code, SITE, EXE, LATEST)
        t["mirror_h"] = mh
        t["mirror_body"] = mb
        t["seo_footer_lines"] = seo_footer_lines(code, SITE, paths, EXE, TG)
        t["faq"] = list(t["faq"]) + faq_extra(code, SITE, paths["dl"])
        merged = {**t, **pack, "mirror_h": mh}
        t["toc"] = build_toc(merged)