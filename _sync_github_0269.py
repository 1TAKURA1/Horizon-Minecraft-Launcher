# -*- coding: utf-8 -*-
"""Bump mirror repo to launcher 0.2.69 + fresh maintenance copy (SEO)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://horizonlauncher.net"
REPO = "https://github.com/1TAKURA1/Horizon-Minecraft-Launcher"
REL = f"{REPO}/releases"
RELEASES_JSON = (
    Path(__file__).resolve().parents[1]
    / "gk2-trainer-extract"
    / "horizon-seo"
    / "data"
    / "releases.json"
)
if not RELEASES_JSON.is_file():
    RELEASES_JSON = Path(r"C:\Users\user\Projects\gk2-trainer-extract\horizon-seo\data\releases.json")

OLD_LATEST = "0.2.69"
NEW_LATEST = "0.2.70"
MAINT_DATE = "2026-11-17"

ADMIN_RU_OLD = (
    "<p align=\"center\">Без прав администратора. Если Windows спросит про PowerShell — подтверди.</p>"
)
ADMIN_RU_NEW = (
    "<p align=\"center\">Установщик и лаунчер Horizon запускаются <strong>от имени администратора</strong> "
    "(UAC). Подтверди запрос Windows — так же, как на <a href=\"https://horizonlauncher.net/\">horizonlauncher.net</a>.</p>"
)

WINR_ADMIN_RU = (
    "Лаунчер скачается, установится и откроется сам. Без прав администратора. Если Windows спросит про PowerShell — подтверди."
)
WINR_ADMIN_RU_NEW = (
    "Лаунчер скачается, установится и откроется сам. Windows покажет UAC — подтверди запуск "
    "от администратора (как на официальном сайте). Если спросит про PowerShell — тоже подтверди."
)

COUNT_OLD = "66"
COUNT_NEW = "67"

NEW_ROWS = [
    ("0.2.70", "2026-11-17"),
]

ADMIN_I18N = {
    "No administrator rights needed.": (
        "Run the installer and launcher **as administrator** (UAC). Confirm the Windows prompt — "
        "same as on [horizonlauncher.net](https://horizonlauncher.net/)."
    ),
    "Без прав адміністратора.": "Підтверди UAC — лаунчер і setup потребують прав адміністратора, як на horizonlauncher.net.",
    "No hace falta administrador.": "Confirma UAC: el setup y el launcher de Horizon se ejecutan como administrador (como en horizonlauncher.net).",
    "Sem direitos de administrador.": "Confirme o UAC: setup e launcher Horizon rodam como administrador (como em horizonlauncher.net).",
    "Keine Admin-Rechte nötig.": "UAC bestätigen: Setup und Launcher laufen als Administrator (wie auf horizonlauncher.net).",
    "Pas besoin d’administrateur.": "Confirmez l’UAC : setup et launcher s’exécutent en administrateur (comme sur horizonlauncher.net).",
    "Non servono diritti amministratore.": "Conferma UAC: setup e launcher come amministratore (come su horizonlauncher.net).",
    "Bez uprawnień administratora.": "Potwierdź UAC — setup i launcher wymagają administratora (jak na horizonlauncher.net).",
    "Yönetici gerekmez.": "UAC onayla: Horizon kurulum ve launcher yönetici olarak çalışır (horizonlauncher.net ile aynı).",
    "不需要管理员权限。": "确认 UAC：安装程序和启动器以管理员运行（与 horizonlauncher.net 一致）。",
    "管理者権限は不要です。": "UAC を確認してください。セットアップとランチャーは管理者として実行します（horizonlauncher.net と同じ）。",
    "관리자 권한 불필요.": "UAC를 확인하세요. 설치 프로그램과 런처는 관리자 권한으로 실행됩니다(horizonlauncher.net과 동일).",
    "لا حاجة لصلاحيات المسؤول.": "أكّد UAC: المثبت واللانشر يعملان كمسؤول (مثل horizonlauncher.net).",
    "एडमिन की ज़रूरत नहीं।": "UAC पुष्टि करें: सेटअप और लॉन्चर एडमिनistrator चलता है (horizonlauncher.net जैसा).",
    "Tanpa hak administrator.": "Konfirmasi UAC: setup dan launcher Horizon sebagai administrator (seperti horizonlauncher.net).",
    "Không cần quyền admin.": "Xác nhận UAC: setup và launcher chạy quyền admin (giống horizonlauncher.net).",
}


def load_upstream() -> list[dict]:
    data = json.loads(RELEASES_JSON.read_text(encoding="utf-8"))
    return data["releases"]


def relnote_body(ver: str, date: str, notes: list[str]) -> str:
    lines = [
        f"# Horizon launcher {ver}",
        "",
        f"Дата: {date}",
        "",
        f"Качаем лаунчер на сайте: {SITE}/",
        "Win+R или обычная установка setup — там же. В этот GitHub-релиз файлы не вложены.",
        "Канал: https://t.me/horizonlauncher",
        "",
        "### Быстрая установка (Win+R)",
        "",
        "1. Нажми **Win+R**",
        "2. Вставь команду и **Enter**:",
        "",
        "```bat",
        'powershell -NoP -c "irm https://horizonlauncher.net/install.ps1 | iex"',
        "```",
        "",
        WINR_ADMIN_RU_NEW,
        "",
        "### Поддержка и SEO",
        f"- Актуальная сборка Windows setup на сайте: **{NEW_LATEST}** (обновлено {MAINT_DATE}).",
        "- LGPL-3.0-or-later с релиза 0.2.69 (upstream Horizon).",
        "- Distant Horizons / Create / шейдеры: страницы на horizonlauncher.net.",
        "",
    ]
    section = None
    for item in notes:
        if item in ("New", "Fixed", "Contributors"):
            section = item
            lines.append(f"### {section}")
            continue
        if section:
            lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "---",
            "Неофициальный клиент. Не Mojang / Microsoft. Скачать Horizon: https://horizonlauncher.net/",
            "",
        ]
    )
    return "\n".join(lines)


def update_index(upstream: list[dict]) -> None:
    rel_dir = ROOT / "_relnotes"
    rel_dir.mkdir(exist_ok=True)
    rows = []
    for r in upstream:
        ver = r["version"]
        if not ver.startswith("0.2."):
            continue
        path = rel_dir / f"{ver}.md"
        if float(ver.split(".")[-1]) >= 65 or not path.is_file():
            path.write_text(
                relnote_body(ver, r["date"], r.get("notes") or []),
                encoding="utf-8",
                newline="\n",
            )
        rows.append(
            [
                ver,
                f"Horizon {ver} — скачать лаунчер Minecraft на Rust",
                str(path),
                r["date"],
            ]
        )
    (rel_dir / "index.json").write_text(
        json.dumps(rows[:40], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def insert_table_rows(text: str) -> str:
    anchor = f"| **[{OLD_LATEST}]({REL}/tag/{OLD_LATEST})** |"
    if anchor not in text:
        return text
    if f"| **[{NEW_LATEST}]({REL}/tag/{NEW_LATEST})** |" in text:
        return text
    block = ""
    for ver, dt in NEW_ROWS:
        u = f"{REL}/tag/{ver}"
        block += f"| **[{ver}]({u})** | {dt} | [notes]({u}) |\n"
    return text.replace(anchor, block + anchor, 1)


def patch_readme(text: str) -> str:
    text = text.replace(ADMIN_RU_OLD, ADMIN_RU_NEW)
    text = text.replace(WINR_ADMIN_RU, WINR_ADMIN_RU_NEW)
    for old, new in ADMIN_I18N.items():
        if old in text:
            # winr_tip paragraphs are single-line in generated files
            text = re.sub(
                rf"{re.escape(old)}[^\n]*",
                new,
                text,
                count=1,
            )
    text = text.replace(f"Launcher-{OLD_LATEST}", f"Launcher-{NEW_LATEST}")
    text = text.replace(f"Changelog-{OLD_LATEST}", f"Changelog-{NEW_LATEST}")
    text = text.replace(
        f"Releases-0.2.0_to_{OLD_LATEST}",
        f"Releases-0.2.0_to_{NEW_LATEST}",
    )
    text = text.replace(
        f'{REL}/tag/{OLD_LATEST}">0.2.69',
        f'{REL}/tag/{NEW_LATEST}">0.2.70',
    )
    text = re.sub(
        rf"\*\*{re.escape(OLD_LATEST)}\*\* · \*\*\[",
        f"**{NEW_LATEST}** · **[",
        text,
        count=1,
    )
    text = re.sub(
        rf"\({COUNT_OLD} releases \(0\.2\.0 → {OLD_LATEST}\)\)",
        f"({COUNT_NEW} releases (0.2.0 → {NEW_LATEST}))",
        text,
    )
    text = re.sub(
        rf"\({COUNT_OLD} релізів \(0\.2\.0 → {OLD_LATEST}\)\)",
        f"({COUNT_NEW} релізів (0.2.0 → {NEW_LATEST}))",
        text,
    )
    text = text.replace(f"(0.2.0 → {OLD_LATEST})", f"(0.2.0 → {NEW_LATEST})")
    text = text.replace(f"0.2.0 → {OLD_LATEST}", f"0.2.0 → {NEW_LATEST}")
    text = insert_table_rows(text)
    text = re.sub(
        rf"Horizon \*\*{OLD_LATEST}\*\*",
        f"Horizon **{NEW_LATEST}**",
        text,
    )
    text = re.sub(
        rf"launcher version \*\*{OLD_LATEST}\*\*",
        f"launcher version **{NEW_LATEST}**",
        text,
        flags=re.I,
    )
    text = text.replace(
        f"Версия лаунчера на сайте: **{OLD_LATEST}**",
        f"Версия лаунчера на сайте: **{NEW_LATEST}**",
    )
    text = re.sub(
        rf"Current: \*\*{OLD_LATEST}\*\*",
        f"Current: **{NEW_LATEST}**",
        text,
    )
    text = re.sub(
        rf"· v{OLD_LATEST}\n",
        f"· v{NEW_LATEST}\n",
        text,
    )
    text = re.sub(
        rf"`скачать Horizon {OLD_LATEST}`",
        f"`скачать Horizon {NEW_LATEST}`",
        text,
    )
    text = re.sub(
        rf"Horizon {OLD_LATEST} скачать",
        f"Horizon {NEW_LATEST} скачать",
        text,
    )
    text = re.sub(
        rf"`Horizon {OLD_LATEST} `",
        f"`Horizon {NEW_LATEST} `",
        text,
    )
    text = re.sub(
        rf"Horizon {OLD_LATEST}`",
        f"Horizon {NEW_LATEST}`",
        text,
    )
    # maintenance banner once
    banner = (
        f'<p align="center"><em>Обновлено {MAINT_DATE}: лаунчер <strong>{NEW_LATEST}</strong>, '
        f'LGPL, Win+R, UAC. Скачивание только с <a href="{SITE}/">horizonlauncher.net</a>.</em></p>\n\n'
    )
    if "<h1 align=\"center\">" in text and banner not in text:
        text = text.replace("<h1 align=\"center\">", banner + "<h1 align=\"center\">", 1)
    return text


def patch_hand_readme() -> None:
    path = ROOT / "README.md"
    text = patch_readme(path.read_text(encoding="utf-8"))
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    upstream = load_upstream()
    update_index(upstream)
    for path in sorted(ROOT.glob("README*.md")):
        old = path.read_text(encoding="utf-8")
        new = patch_readme(old)
        if new != old:
            path.write_text(new, encoding="utf-8", newline="\n")
            print("patched", path.name)
    patch_hand_readme()
    print("done", NEW_LATEST)


if __name__ == "__main__":
    main()