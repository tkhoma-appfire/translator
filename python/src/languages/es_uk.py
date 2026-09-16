"""Spanish → Ukrainian: prompt and UI strings."""

from __future__ import annotations

from languages.profile import LanguagePair

CODE = "es-uk"

SPECIAL_CHARACTERS = (
    "á",
    "é",
    "í",
    "ó",
    "ú",
    "ñ",
    "ü",
    "Á",
    "É",
    "Í",
    "Ó",
    "Ú",
    "Ñ",
    "Ü",
    "¿",
    "¡",
)

SYSTEM_PROMPT = """Spanish → Ukrainian assistant. Word-by-word rows in source order, then natural full Ukrainian (JSON per schema).

Per token:
- Verbs: Ukrainian gloss (prefer Ukrainian infinitive); explanation MUST start with the Spanish infinitive (infinitivo), then gerund and participle / key tenses (e.g. leer, leyendo, leído; haber, he, ha…).
- Nouns: gloss; explanation = gender (el/la) and base form.
- Multiple senses: comma or / in translation.

Rules: one Spanish token per row; for every verb include its Spanish infinitive in explanation; concise dictionary Ukrainian; no prose beyond explanation.
"""

PAIR = LanguagePair(
    code=CODE,
    system_prompt=SYSTEM_PROMPT,
    page_title="ES → UK (Ollama)",
    heading="Spanish → Ukrainian",
    caption="Powered by Ollama.",
    source_label="Spanish text",
    source_placeholder="Hola, ¿cómo está usted?",
    translate_button="Translate to Ukrainian",
    translation_heading="Translation",
    special_characters=SPECIAL_CHARACTERS,
)
