# -*- coding: utf-8 -*-
"""Localized feat_body, extra FAQ, and SEO tags for GitHub README i18n."""

from __future__ import annotations

# fmt: SITE EXE REL LATEST


def faq_extra(lang: str, *, SITE: str, EXE: str, REL: str, LATEST: str) -> list[tuple[str, str]]:
    m = {
        "uk": [
            (
                "Яка ліцензія?",
                f"З **{LATEST}** upstream Horizon — **LGPL-3.0-or-later**. Файли Minecraft — Mojang/Microsoft. [{SITE}/legal/]({SITE}/legal/).",
            ),
            (
                "Distant Horizons, Create і шейдери?",
                f"Так — нативні моди (.hnmod). [Distant Horizons]({SITE}/distant-horizons/) · [Create]({SITE}/create-mod/) · [шейдери]({SITE}/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Релізи]({REL}) · лаунчер **{LATEST}** на [{SITE}/]({SITE}/).",
            ),
        ],
        "es": [
            (
                "¿Qué licencia?",
                f"Desde **{LATEST}**, Horizon upstream es **LGPL-3.0-or-later**. Ver [{SITE}/es/legal/]({SITE}/es/legal/).",
            ),
            (
                "¿Distant Horizons, Create y shaders?",
                f"Sí — mods nativos (.hnmod). [{SITE}/es/distant-horizons/]({SITE}/es/distant-horizons/) · [Create]({SITE}/es/create-mod/) · [shaders]({SITE}/es/shaders/).",
            ),
            (
                "¿Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** en [{SITE}/es/]({SITE}/es/).",
            ),
        ],
        "pt": [
            (
                "Qual licença?",
                f"A partir de **{LATEST}**, Horizon upstream é **LGPL-3.0-or-later**. [{SITE}/pt/legal/]({SITE}/pt/legal/).",
            ),
            (
                "Distant Horizons, Create e shaders?",
                f"Sim — mods nativos (.hnmod). [{SITE}/pt/distant-horizons/]({SITE}/pt/distant-horizons/) · [Create]({SITE}/pt/create-mod/) · [shaders]({SITE}/pt/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** em [{SITE}/pt/]({SITE}/pt/).",
            ),
        ],
        "de": [
            (
                "Welche Lizenz?",
                f"Ab **{LATEST}** ist Horizon upstream **LGPL-3.0-or-later**. [{SITE}/de/legal/]({SITE}/de/legal/).",
            ),
            (
                "Distant Horizons, Create, Shader?",
                f"Ja — native Mods (.hnmod). [{SITE}/de/distant-horizons/]({SITE}/de/distant-horizons/) · [Create]({SITE}/de/create-mod/) · [Shader]({SITE}/de/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · Launcher **{LATEST}** auf [{SITE}/de/]({SITE}/de/).",
            ),
        ],
        "fr": [
            (
                "Quelle licence ?",
                f"Depuis **{LATEST}**, Horizon upstream est en **LGPL-3.0-or-later**. [{SITE}/fr/legal/]({SITE}/fr/legal/).",
            ),
            (
                "Distant Horizons, Create et shaders ?",
                f"Oui — mods natifs (.hnmod). [{SITE}/fr/distant-horizons/]({SITE}/fr/distant-horizons/) · [Create]({SITE}/fr/create-mod/) · [shaders]({SITE}/fr/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69 ?",
                f"[Releases]({REL}) · launcher **{LATEST}** sur [{SITE}/fr/]({SITE}/fr/).",
            ),
        ],
        "it": [
            (
                "Quale licenza?",
                f"Da **{LATEST}**, Horizon upstream è **LGPL-3.0-or-later**. [{SITE}/it/legal/]({SITE}/it/legal/).",
            ),
            (
                "Distant Horizons, Create e shader?",
                f"Sì — mod nativi (.hnmod). [{SITE}/it/distant-horizons/]({SITE}/it/distant-horizons/) · [Create]({SITE}/it/create-mod/) · [shader]({SITE}/it/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** su [{SITE}/it/]({SITE}/it/).",
            ),
        ],
        "pl": [
            (
                "Jaka licencja?",
                f"Od **{LATEST}** Horizon upstream ma **LGPL-3.0-or-later**. [{SITE}/pl/legal/]({SITE}/pl/legal/).",
            ),
            (
                "Distant Horizons, Create i shadery?",
                f"Tak — natywne mody (.hnmod). [{SITE}/pl/distant-horizons/]({SITE}/pl/distant-horizons/) · [Create]({SITE}/pl/create-mod/) · [shadery]({SITE}/pl/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** na [{SITE}/pl/]({SITE}/pl/).",
            ),
        ],
        "tr": [
            (
                "Lisans nedir?",
                f"**{LATEST}** itibarıyla Horizon upstream **LGPL-3.0-or-later**. [{SITE}/tr/legal/]({SITE}/tr/legal/).",
            ),
            (
                "Distant Horizons, Create ve shader?",
                f"Evet — yerel modlar (.hnmod). [{SITE}/tr/distant-horizons/]({SITE}/tr/distant-horizons/) · [Create]({SITE}/tr/create-mod/) · [shader]({SITE}/tr/shaders/).",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** [{SITE}/tr/]({SITE}/tr/).",
            ),
        ],
        "zh": [
            (
                "什么许可证？",
                f"从 **{LATEST}** 起，Horizon 上游为 **LGPL-3.0-or-later**。[{SITE}/zh/legal/]({SITE}/zh/legal/)",
            ),
            (
                "Distant Horizons、Create 和光影？",
                f"支持 — 原生模组 (.hnmod)。[{SITE}/zh/distant-horizons/]({SITE}/zh/distant-horizons/) · [Create]({SITE}/zh/create-mod/) · [光影]({SITE}/zh/shaders/)",
            ),
            (
                "0.2.65–0.2.69 更新？",
                f"[Releases]({REL}) · 启动器 **{LATEST}** [{SITE}/zh/]({SITE}/zh/)",
            ),
        ],
        "ja": [
            (
                "ライセンスは？",
                f"**{LATEST}** 以降、Horizon 上流は **LGPL-3.0-or-later**。[{SITE}/ja/legal/]({SITE}/ja/legal/)",
            ),
            (
                "Distant Horizons、Create、シェーダー？",
                f"対応 — ネイティブ Mod (.hnmod)。[{SITE}/ja/distant-horizons/]({SITE}/ja/distant-horizons/) · [Create]({SITE}/ja/create-mod/) · [シェーダー]({SITE}/ja/shaders/)",
            ),
            (
                "チェンジログ 0.2.65–0.2.69？",
                f"[Releases]({REL}) · ランチャー **{LATEST}** [{SITE}/ja/]({SITE}/ja/)",
            ),
        ],
        "ko": [
            (
                "라이선스는?",
                f"**{LATEST}**부터 Horizon 업스트림 **LGPL-3.0-or-later**. [{SITE}/ko/legal/]({SITE}/ko/legal/)",
            ),
            (
                "Distant Horizons, Create, 셰이더?",
                f"지원 — 네이티브 모드 (.hnmod). [{SITE}/ko/distant-horizons/]({SITE}/ko/distant-horizons/) · [Create]({SITE}/ko/create-mod/) · [셰이더]({SITE}/ko/shaders/)",
            ),
            (
                "변경 로그 0.2.65–0.2.69?",
                f"[Releases]({REL}) · 런처 **{LATEST}** [{SITE}/ko/]({SITE}/ko/)",
            ),
        ],
        "ar": [
            (
                "ما الترخيص؟",
                f"منذ **{LATEST}** Horizon upstream تحت **LGPL-3.0-or-later**. [{SITE}/ar/legal/]({SITE}/ar/legal/)",
            ),
            (
                "Distant Horizons وCreate والشيدر؟",
                f"نعم — مودات أصلية (.hnmod). [{SITE}/ar/distant-horizons/]({SITE}/ar/distant-horizons/) · [Create]({SITE}/ar/create-mod/) · [شيدر]({SITE}/ar/shaders/)",
            ),
            (
                "سجل التغيير 0.2.65–0.2.69؟",
                f"[Releases]({REL}) · اللانشر **{LATEST}** [{SITE}/ar/]({SITE}/ar/)",
            ),
        ],
        "hi": [
            (
                "लाइसेंस क्या है?",
                f"**{LATEST}** से Horizon upstream **LGPL-3.0-or-later**। [{SITE}/hi/legal/]({SITE}/hi/legal/)",
            ),
            (
                "Distant Horizons, Create और शेडर?",
                f"हाँ — नेटिव मॉड (.hnmod)। [{SITE}/hi/distant-horizons/]({SITE}/hi/distant-horizons/) · [Create]({SITE}/hi/create-mod/) · [शेडर]({SITE}/hi/shaders/)",
            ),
            (
                "चेंजलॉग 0.2.65–0.2.69?",
                f"[Releases]({REL}) · लॉन्चर **{LATEST}** [{SITE}/hi/]({SITE}/hi/)",
            ),
        ],
        "id": [
            (
                "Lisensi apa?",
                f"Sejak **{LATEST}**, Horizon upstream **LGPL-3.0-or-later**. [{SITE}/id/legal/]({SITE}/id/legal/)",
            ),
            (
                "Distant Horizons, Create, shader?",
                f"Ya — mod native (.hnmod). [{SITE}/id/distant-horizons/]({SITE}/id/distant-horizons/) · [Create]({SITE}/id/create-mod/) · [shader]({SITE}/id/shaders/)",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** [{SITE}/id/]({SITE}/id/)",
            ),
        ],
        "vi": [
            (
                "Giấy phép nào?",
                f"Từ **{LATEST}**, Horizon upstream là **LGPL-3.0-or-later**. [{SITE}/vi/legal/]({SITE}/vi/legal/)",
            ),
            (
                "Distant Horizons, Create và shader?",
                f"Có — mod native (.hnmod). [{SITE}/vi/distant-horizons/]({SITE}/vi/distant-horizons/) · [Create]({SITE}/vi/create-mod/) · [shader]({SITE}/vi/shaders/)",
            ),
            (
                "Changelog 0.2.65–0.2.69?",
                f"[Releases]({REL}) · launcher **{LATEST}** [{SITE}/vi/]({SITE}/vi/)",
            ),
        ],
    }
    return m.get(lang, [])


def seo_extra(lang: str, *, LATEST: str) -> list[str]:
    m = {
        "uk": [
            "Distant Horizons Horizon",
            "Create mod Horizon",
            "шейдери Horizon",
            "LGPL Horizon",
            "Horizon Win+R",
            "Minecraft Java Rust",
        ],
        "es": [
            "descargar Horizon",
            "Distant Horizons Horizon",
            "Create mod Horizon",
            "shaders Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
            "launcher Minecraft FPS",
        ],
        "pt": [
            "baixar Horizon",
            "Distant Horizons Horizon",
            "Create mod Horizon",
            "shaders Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "de": [
            "Horizon herunterladen",
            "Distant Horizons Horizon",
            "Create Mod Horizon",
            "Shader Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "fr": [
            "télécharger Horizon",
            "Distant Horizons Horizon",
            "mod Create Horizon",
            "shaders Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "it": [
            "scaricare Horizon",
            "Distant Horizons Horizon",
            "mod Create Horizon",
            "shader Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "pl": [
            "pobierz Horizon",
            "Distant Horizons Horizon",
            "mod Create Horizon",
            "shadery Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "tr": [
            "Horizon indir",
            "Distant Horizons Horizon",
            "Create mod Horizon",
            "shader Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "zh": [
            "下载 Horizon",
            "Distant Horizons Horizon",
            "Create 模组 Horizon",
            "光影 Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
            "Minecraft Rust 客户端",
        ],
        "ja": [
            "Horizon ダウンロード",
            "Distant Horizons Horizon",
            "Create モッド",
            "シェーダー Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "ko": [
            "Horizon 다운로드",
            "Distant Horizons Horizon",
            "Create 모드",
            "셰이더 Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "ar": [
            "تنزيل Horizon",
            "Distant Horizons Horizon",
            "Create Horizon",
            "شيدر Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "hi": [
            "Horizon डाउनलोड",
            "Distant Horizons Horizon",
            "Create mod Horizon",
            "शेडर Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "id": [
            "unduh Horizon",
            "Distant Horizons Horizon",
            "mod Create Horizon",
            "shader Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
        "vi": [
            "tải Horizon",
            "Distant Horizons Horizon",
            "mod Create Horizon",
            "shader Horizon",
            "LGPL Horizon",
            f"Horizon {LATEST}",
        ],
    }
    return m.get(lang, [])


def feat_body(lang: str) -> str:
    """Return feat_body template; caller .format(SITE=, EXE=, REL=, LATEST=)."""
    bodies: dict[str, str] = {}
    bodies["uk"] = """
## Можливості Horizon Minecraft (клієнт Java на Rust)

**Horizon** переписує **Minecraft: Java Edition 26.3** мовою **Rust**: ті самі світи й правила, нативний рендер замість JVM. Встановлюйте **лаунчер Horizon** лише з **[horizonlauncher.net]({SITE}/)**.

| Запит | Сторінка |
|-------|----------|
| завантажити Horizon, setup exe, Win+R | [{SITE}/download-horizon/]({SITE}/download-horizon/) |
| Minecraft на Rust, вищий FPS | [{SITE}/minecraft-rust/]({SITE}/minecraft-rust/) · [{SITE}/performance/]({SITE}/performance/) |
| Distant Horizons, Create, шейдери | [{SITE}/distant-horizons/]({SITE}/distant-horizons/) · [{SITE}/create-mod/]({SITE}/create-mod/) · [{SITE}/shaders/]({SITE}/shaders/) |
| мультиплеєр | [{SITE}/server/]({SITE}/server/) |
| LGPL | [{SITE}/legal/]({SITE}/legal/) |

### Parity та FPS

Сотні **differential harnesses** порівнюють ваніль Java і Horizon Rust на однакових вхідних даних — чанки, редстоун, мережа, світло, сейви.

### У грі (upstream; Windows setup на сайті)

Одиночна гра та LAN, **LOD** до 1024 чанків, геймпади, нативні моди **`.hnmod`**, **shader API 0.2**, **LGPL-3.0-or-later** з 0.2.69.

### Останні патчі лаунчера

**0.2.69** LGPL · **0.2.68** UI · **0.2.67** shader API 0.2 · **0.2.66–0.2.65** мережа та завантаження. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["es"] = """
## Funciones de Horizon Minecraft (cliente Java en Rust)

**Horizon** reimplementa **Minecraft: Java Edition 26.3** en **Rust**: mismos mundos y reglas, render nativo sin la JVM. Instala el **launcher Horizon** solo desde **[horizonlauncher.net]({SITE}/es/)**.

| Búsqueda | URL canónica |
|----------|----------------|
| descargar Horizon, setup exe, Win+R | [{SITE}/es/download-horizon/]({SITE}/es/download-horizon/) |
| Minecraft en Rust, más FPS | [{SITE}/es/minecraft-rust/]({SITE}/es/minecraft-rust/) · [{SITE}/es/performance/]({SITE}/es/performance/) |
| Distant Horizons, Create, shaders | [{SITE}/es/distant-horizons/]({SITE}/es/distant-horizons/) · [{SITE}/es/create-mod/]({SITE}/es/create-mod/) · [{SITE}/es/shaders/]({SITE}/es/shaders/) |
| multijugador | [{SITE}/es/server/]({SITE}/es/server/) |
| LGPL | [{SITE}/es/legal/]({SITE}/es/legal/) |

### Paridad y FPS

Cientos de **differential harnesses** comparan Java vanilla y Horizon Rust con las mismas entradas.

### En el juego

Un jugador y LAN, **LOD** lejano, mandos, mods nativos **`.hnmod`**, **shader API 0.2**, **LGPL** desde 0.2.69.

### Parches recientes del launcher

**0.2.69** LGPL · **0.2.68** UI · **0.2.67** shader API 0.2. Notas: [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["pt"] = """
## Recursos do Horizon Minecraft (cliente Java em Rust)

**Horizon** reescreve **Minecraft: Java Edition 26.3** em **Rust**: mesmos mundos, render nativo sem JVM. Baixe o **launcher Horizon** apenas em **[horizonlauncher.net]({SITE}/pt/)**.

| Busca | Página |
|-------|--------|
| baixar Horizon, setup, Win+R | [{SITE}/pt/download-horizon/]({SITE}/pt/download-horizon/) |
| Minecraft em Rust, mais FPS | [{SITE}/pt/minecraft-rust/]({SITE}/pt/minecraft-rust/) · [{SITE}/pt/performance/]({SITE}/pt/performance/) |
| Distant Horizons, Create, shaders | [{SITE}/pt/distant-horizons/]({SITE}/pt/distant-horizons/) · [{SITE}/pt/create-mod/]({SITE}/pt/create-mod/) · [{SITE}/pt/shaders/]({SITE}/pt/shaders/) |
| multiplayer | [{SITE}/pt/server/]({SITE}/pt/server/) |
| LGPL | [{SITE}/pt/legal/]({SITE}/pt/legal/) |

### Paridade e FPS

Centenas de **differential harnesses** comparam Java vanilla e Horizon Rust.

### No jogo

Singleplayer e LAN, **LOD**, controles, mods **`.hnmod`**, **shader API 0.2**, **LGPL** desde 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["de"] = """
## Horizon Minecraft — Funktionen (Java-Client in Rust)

**Horizon** implementiert **Minecraft: Java Edition 26.3** in **Rust** neu: gleiche Welten, natives Rendering statt JVM. Launcher nur von **[horizonlauncher.net]({SITE}/de/)**.

| Suche | Seite |
|-------|-------|
| Horizon herunterladen, Win+R | [{SITE}/de/download-horizon/]({SITE}/de/download-horizon/) |
| Minecraft auf Rust, mehr FPS | [{SITE}/de/minecraft-rust/]({SITE}/de/minecraft-rust/) · [{SITE}/de/performance/]({SITE}/de/performance/) |
| Distant Horizons, Create, Shader | [{SITE}/de/distant-horizons/]({SITE}/de/distant-horizons/) · [{SITE}/de/create-mod/]({SITE}/de/create-mod/) · [{SITE}/de/shaders/]({SITE}/de/shaders/) |
| Multiplayer | [{SITE}/de/server/]({SITE}/de/server/) |
| LGPL | [{SITE}/de/legal/]({SITE}/de/legal/) |

### Parität & FPS

Hunderte **Differential Harnesses** vergleichen Vanilla-Java und Horizon-Rust.

### Im Spiel

Singleplayer, LAN, **LOD**, Gamepads, native **`.hnmod`**-Mods, **Shader API 0.2**, **LGPL** ab 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["fr"] = """
## Fonctions Horizon Minecraft (client Java en Rust)

**Horizon** réécrit **Minecraft: Java Edition 26.3** en **Rust** : mêmes mondes, rendu natif sans JVM. Téléchargez le launcher sur **[horizonlauncher.net]({SITE}/fr/)**.

| Recherche | Page |
|-----------|------|
| télécharger Horizon, Win+R | [{SITE}/fr/download-horizon/]({SITE}/fr/download-horizon/) |
| Minecraft sur Rust, FPS | [{SITE}/fr/minecraft-rust/]({SITE}/fr/minecraft-rust/) · [{SITE}/fr/performance/]({SITE}/fr/performance/) |
| Distant Horizons, Create, shaders | [{SITE}/fr/distant-horizons/]({SITE}/fr/distant-horizons/) · [{SITE}/fr/create-mod/]({SITE}/fr/create-mod/) · [{SITE}/fr/shaders/]({SITE}/fr/shaders/) |
| multijoueur | [{SITE}/fr/server/]({SITE}/fr/server/) |
| LGPL | [{SITE}/fr/legal/]({SITE}/fr/legal/) |

### Parité et FPS

Des centaines de **harnesses différentiels** comparent Java vanilla et Horizon Rust.

### En jeu

Solo, LAN, **LOD**, manettes, mods **`.hnmod`**, **shader API 0.2**, **LGPL** dès 0.2.69. [{REL}]({REL})

Win+R : `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["it"] = """
## Funzioni Horizon Minecraft (client Java in Rust)

**Horizon** riscrive **Minecraft: Java Edition 26.3** in **Rust**: stessi mondi, rendering nativo senza JVM. Scarica il launcher da **[horizonlauncher.net]({SITE}/it/)**.

| Ricerca | Pagina |
|---------|--------|
| scaricare Horizon, Win+R | [{SITE}/it/download-horizon/]({SITE}/it/download-horizon/) |
| Minecraft su Rust, FPS | [{SITE}/it/minecraft-rust/]({SITE}/it/minecraft-rust/) · [{SITE}/it/performance/]({SITE}/it/performance/) |
| Distant Horizons, Create, shader | [{SITE}/it/distant-horizons/]({SITE}/it/distant-horizons/) · [{SITE}/it/create-mod/]({SITE}/it/create-mod/) · [{SITE}/it/shaders/]({SITE}/it/shaders/) |
| multiplayer | [{SITE}/it/server/]({SITE}/it/server/) |
| LGPL | [{SITE}/it/legal/]({SITE}/it/legal/) |

### Parità e FPS

Centinaia di **harness differenziali** confrontano Java vanilla e Horizon Rust.

### In gioco

Singleplayer, LAN, **LOD**, gamepad, mod **`.hnmod`**, **shader API 0.2**, **LGPL** da 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["pl"] = """
## Horizon Minecraft — funkcje (klient Java w Rust)

**Horizon** przepisuje **Minecraft: Java Edition 26.3** w **Rust**: te same światy, natywny render zamiast JVM. Pobierz launcher z **[horizonlauncher.net]({SITE}/pl/)**.

| Zapytanie | Strona |
|-----------|--------|
| pobierz Horizon, Win+R | [{SITE}/pl/download-horizon/]({SITE}/pl/download-horizon/) |
| Minecraft na Rust, FPS | [{SITE}/pl/minecraft-rust/]({SITE}/pl/minecraft-rust/) · [{SITE}/pl/performance/]({SITE}/pl/performance/) |
| Distant Horizons, Create, shadery | [{SITE}/pl/distant-horizons/]({SITE}/pl/distant-horizons/) · [{SITE}/pl/create-mod/]({SITE}/pl/create-mod/) · [{SITE}/pl/shaders/]({SITE}/pl/shaders/) |
| multiplayer | [{SITE}/pl/server/]({SITE}/pl/server/) |
| LGPL | [{SITE}/pl/legal/]({SITE}/pl/legal/) |

### Parity i FPS

Setki **differential harnesses** porównują Java vanilla i Horizon Rust.

### W grze

Singleplayer, LAN, **LOD**, pad, mody **`.hnmod`**, **shader API 0.2**, **LGPL** od 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["tr"] = """
## Horizon Minecraft özellikleri (Java istemcisi, Rust)

**Horizon**, **Minecraft: Java Edition 26.3**'ü **Rust** ile yeniden yazar: aynı dünyalar, JVM yerine yerel render. Launcher'ı yalnızca **[horizonlauncher.net]({SITE}/tr/)** üzerinden indirin.

| Arama | Sayfa |
|-------|-------|
| Horizon indir, Win+R | [{SITE}/tr/download-horizon/]({SITE}/tr/download-horizon/) |
| Rust'ta Minecraft, FPS | [{SITE}/tr/minecraft-rust/]({SITE}/tr/minecraft-rust/) · [{SITE}/tr/performance/]({SITE}/tr/performance/) |
| Distant Horizons, Create, shader | [{SITE}/tr/distant-horizons/]({SITE}/tr/distant-horizons/) · [{SITE}/tr/create-mod/]({SITE}/tr/create-mod/) · [{SITE}/tr/shaders/]({SITE}/tr/shaders/) |
| çok oyunculu | [{SITE}/tr/server/]({SITE}/tr/server/) |
| LGPL | [{SITE}/tr/legal/]({SITE}/tr/legal/) |

### Parity ve FPS

Yüzlerce **differential harness**, vanilla Java ile Horizon Rust'ı karşılaştırır.

### Oyunda

Tek oyuncu, LAN, **LOD**, gamepad, **`.hnmod`** modlar, **shader API 0.2**, **LGPL** 0.2.69'dan. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["zh"] = """
## Horizon Minecraft 功能（Rust 重写的 Java 客户端）

**Horizon** 用 **Rust** 重写 **Minecraft: Java Edition 26.3**：相同世界与规则，原生渲染取代 JVM。请仅从 **[horizonlauncher.net]({SITE}/zh/)** 下载启动器。

| 搜索意图 | 页面 |
|----------|------|
| 下载 Horizon、Win+R | [{SITE}/zh/download-horizon/]({SITE}/zh/download-horizon/) |
| Rust 版 Minecraft、更高 FPS | [{SITE}/zh/minecraft-rust/]({SITE}/zh/minecraft-rust/) · [{SITE}/zh/performance/]({SITE}/zh/performance/) |
| Distant Horizons、Create、光影 | [{SITE}/zh/distant-horizons/]({SITE}/zh/distant-horizons/) · [{SITE}/zh/create-mod/]({SITE}/zh/create-mod/) · [{SITE}/zh/shaders/]({SITE}/zh/shaders/) |
| 多人 | [{SITE}/zh/server/]({SITE}/zh/server/) |
| LGPL | [{SITE}/zh/legal/]({SITE}/zh/legal/) |

### 一致性与 FPS

数百个 **differential harnesses** 对比原版 Java 与 Horizon Rust。

### 游戏内

单人、LAN、**LOD** 远景、手柄、原生 **`.hnmod`** 模组、**shader API 0.2**、**LGPL**（0.2.69 起）。[{REL}]({REL})

Win+R：`irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["ja"] = """
## Horizon Minecraft の機能（Rust 製 Java クライアント）

**Horizon** は **Minecraft: Java Edition 26.3** を **Rust** で再実装。同じ世界とルール、JVM の代わりにネイティブ描画。**[horizonlauncher.net]({SITE}/ja/)** からのみダウンロード。

| 検索 | ページ |
|------|--------|
| Horizon ダウンロード、Win+R | [{SITE}/ja/download-horizon/]({SITE}/ja/download-horizon/) |
| Rust 版 Minecraft、FPS | [{SITE}/ja/minecraft-rust/]({SITE}/ja/minecraft-rust/) · [{SITE}/ja/performance/]({SITE}/ja/performance/) |
| Distant Horizons、Create、シェーダー | [{SITE}/ja/distant-horizons/]({SITE}/ja/distant-horizons/) · [{SITE}/ja/create-mod/]({SITE}/ja/create-mod/) · [{SITE}/ja/shaders/]({SITE}/ja/shaders/) |
| マルチ | [{SITE}/ja/server/]({SITE}/ja/server/) |
| LGPL | [{SITE}/ja/legal/]({SITE}/ja/legal/) |

### パリティと FPS

数百の **differential harnesses** がバニラ Java と Horizon Rust を比較。

### ゲーム内

シングル、LAN、**LOD**、ゲームパッド、**`.hnmod`** モッド、**shader API 0.2**、**LGPL**（0.2.69〜）。[{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["ko"] = """
## Horizon Minecraft 기능 (Rust Java 클라이언트)

**Horizon**은 **Minecraft: Java Edition 26.3**을 **Rust**로 다시 구현합니다. 동일한 월드, JVM 대신 네이티브 렌더링. **[horizonlauncher.net]({SITE}/ko/)** 에서만 다운로드.

| 검색 | 페이지 |
|------|--------|
| Horizon 다운로드, Win+R | [{SITE}/ko/download-horizon/]({SITE}/ko/download-horizon/) |
| Rust Minecraft, FPS | [{SITE}/ko/minecraft-rust/]({SITE}/ko/minecraft-rust/) · [{SITE}/ko/performance/]({SITE}/ko/performance/) |
| Distant Horizons, Create, 셰이더 | [{SITE}/ko/distant-horizons/]({SITE}/ko/distant-horizons/) · [{SITE}/ko/create-mod/]({SITE}/ko/create-mod/) · [{SITE}/ko/shaders/]({SITE}/ko/shaders/) |
| 멀티 | [{SITE}/ko/server/]({SITE}/ko/server/) |
| LGPL | [{SITE}/ko/legal/]({SITE}/ko/legal/) |

### 패리티와 FPS

수백 개의 **differential harnesses**가 바닐라 Java와 Horizon Rust를 비교합니다.

### 게임

싱글, LAN, **LOD**, 패드, **`.hnmod`** 모드, **shader API 0.2**, **LGPL**(0.2.69~). [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["ar"] = """
## ميزات Horizon Minecraft (عميل Java بلغة Rust)

**Horizon** يعيد بناء **Minecraft: Java Edition 26.3** بـ **Rust**: نفس العوالم، عرض أصلي بدون JVM. حمّل اللانشر من **[horizonlauncher.net]({SITE}/ar/)** فقط.

| البحث | الصفحة |
|-------|--------|
| تنزيل Horizon، Win+R | [{SITE}/ar/download-horizon/]({SITE}/ar/download-horizon/) |
| Minecraft على Rust، FPS | [{SITE}/ar/minecraft-rust/]({SITE}/ar/minecraft-rust/) · [{SITE}/ar/performance/]({SITE}/ar/performance/) |
| Distant Horizons وCreate والشيدر | [{SITE}/ar/distant-horizons/]({SITE}/ar/distant-horizons/) · [{SITE}/ar/create-mod/]({SITE}/ar/create-mod/) · [{SITE}/ar/shaders/]({SITE}/ar/shaders/) |
| متعدد اللاعبين | [{SITE}/ar/server/]({SITE}/ar/server/) |
| LGPL | [{SITE}/ar/legal/]({SITE}/ar/legal/) |

### التطابق والأداء

مئات **harnesses** تُقارن Java الفانيلا وHorizon Rust.

### داخل اللعبة

فردي، LAN، **LOD**، أذرع تحكم، مودات **`.hnmod`**، **shader API 0.2**، **LGPL** من 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["hi"] = """
## Horizon Minecraft की सुविधाएँ (Rust में Java क्लाइंट)

**Horizon** **Minecraft: Java Edition 26.3** को **Rust** में दोबारा लिखता है: वही दुनिया, JVM के बिना नेटिव रेंडर। लॉन्चर केवल **[horizonlauncher.net]({SITE}/hi/)** से।

| खोज | पेज |
|-----|-----|
| Horizon डाउनलोड, Win+R | [{SITE}/hi/download-horizon/]({SITE}/hi/download-horizon/) |
| Rust में Minecraft, FPS | [{SITE}/hi/minecraft-rust/]({SITE}/hi/minecraft-rust/) · [{SITE}/hi/performance/]({SITE}/hi/performance/) |
| Distant Horizons, Create, शेडर | [{SITE}/hi/distant-horizons/]({SITE}/hi/distant-horizons/) · [{SITE}/hi/create-mod/]({SITE}/hi/create-mod/) · [{SITE}/hi/shaders/]({SITE}/hi/shaders/) |
| मल्टीप्लेयर | [{SITE}/hi/server/]({SITE}/hi/server/) |
| LGPL | [{SITE}/hi/legal/]({SITE}/hi/legal/) |

### पैरिटी और FPS

सैकड़ों **differential harnesses** वैनिला Java और Horizon Rust की तुलना करते हैं।

### गेम में

सिंगल प्लेयर, LAN, **LOD**, गेमपैड, **`.hnmod`** मॉड, **shader API 0.2**, **LGPL** 0.2.69 से। [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["id"] = """
## Fitur Horizon Minecraft (klien Java di Rust)

**Horizon** menulis ulang **Minecraft: Java Edition 26.3** dalam **Rust**: dunia sama, render native tanpa JVM. Unduh launcher hanya dari **[horizonlauncher.net]({SITE}/id/)**.

| Pencarian | Halaman |
|-----------|---------|
| unduh Horizon, Win+R | [{SITE}/id/download-horizon/]({SITE}/id/download-horizon/) |
| Minecraft di Rust, FPS | [{SITE}/id/minecraft-rust/]({SITE}/id/minecraft-rust/) · [{SITE}/id/performance/]({SITE}/id/performance/) |
| Distant Horizons, Create, shader | [{SITE}/id/distant-horizons/]({SITE}/id/distant-horizons/) · [{SITE}/id/create-mod/]({SITE}/id/create-mod/) · [{SITE}/id/shaders/]({SITE}/id/shaders/) |
| multipemain | [{SITE}/id/server/]({SITE}/id/server/) |
| LGPL | [{SITE}/id/legal/]({SITE}/id/legal/) |

### Paritas & FPS

Ratusan **differential harnesses** membandingkan Java vanilla dan Horizon Rust.

### Dalam game

Singleplayer, LAN, **LOD**, gamepad, mod **`.hnmod`**, **shader API 0.2**, **LGPL** sejak 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    bodies["vi"] = """
## Tính năng Horizon Minecraft (client Java trên Rust)

**Horizon** viết lại **Minecraft: Java Edition 26.3** bằng **Rust**: cùng thế giới, render native thay JVM. Chỉ tải launcher tại **[horizonlauncher.net]({SITE}/vi/)**.

| Tìm kiếm | Trang |
|----------|-------|
| tải Horizon, Win+R | [{SITE}/vi/download-horizon/]({SITE}/vi/download-horizon/) |
| Minecraft trên Rust, FPS | [{SITE}/vi/minecraft-rust/]({SITE}/vi/minecraft-rust/) · [{SITE}/vi/performance/]({SITE}/vi/performance/) |
| Distant Horizons, Create, shader | [{SITE}/vi/distant-horizons/]({SITE}/vi/distant-horizons/) · [{SITE}/vi/create-mod/]({SITE}/vi/create-mod/) · [{SITE}/vi/shaders/]({SITE}/vi/shaders/) |
| multiplayer | [{SITE}/vi/server/]({SITE}/vi/server/) |
| LGPL | [{SITE}/vi/legal/]({SITE}/vi/legal/) |

### Parity & FPS

Hàng trăm **differential harnesses** so sánh Java vanilla và Horizon Rust.

### Trong game

Singleplayer, LAN, **LOD**, tay cầm, mod **`.hnmod`**, **shader API 0.2**, **LGPL** từ 0.2.69. [{REL}]({REL})

Win+R: `irm {SITE}/install.ps1 | iex` · **[horizon-launcher-setup.exe]({EXE})**
""".strip()

    return bodies.get(lang, "")


def apply_translations(
    T: dict,
    *,
    SITE: str,
    EXE: str,
    REL: str,
    LATEST: str,
) -> None:
    fmt = dict(SITE=SITE, EXE=EXE, REL=REL, LATEST=LATEST)
    for code in T:
        if code in ("ru", "en"):
            continue
        body_tpl = feat_body(code)
        if body_tpl:
            T[code]["feat_body"] = body_tpl.format(**fmt)
        extra_faq = faq_extra(code, SITE=SITE, EXE=EXE, REL=REL, LATEST=LATEST)
        if extra_faq:
            T[code]["faq"] = list(T[code]["faq"]) + extra_faq
        extra_seo = seo_extra(code, LATEST=LATEST)
        if extra_seo:
            T[code]["seo"] = list(T[code]["seo"]) + extra_seo