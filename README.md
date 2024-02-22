# azerbaijani

Check if your text is in Azerbaijani.

```py
from azerbaijani import is_azerbaijani

input_text = """
Bakı şəhərində və Abşeron yarımadasında insanlar çox qədim zamanlardan məskunlaşmış və burada yaşayış məntəqələri yaratmışlar.[7] Buna səbəb Bakı şəhərinin fiziki-coğrafi şəraiti şimaldan-cənuba, qərbdən-şərqə gedən miqrasiya və ticarət yollarının kəsişməsi mərkəzində yerləşməsi, iqlim şəraiti və ən qədim zamanlardan yer üzünə çıxan "Nafta" adlanan yanacaq və enerji sərvəti olmuşdur.[7] Abşeron ərazisində tapılmış arxeoloji materiallar Bakının qədim yaşayış məskəni olduğunu sübut edir.[7] Pirallahı, Zığ gölü ətrafı, Şüvəlan, Mərdəkan, Əmircan və s. yerlərdə e. ə. III-I-ci minilliklərə aid arxeoloji materiallar tapılmışdır.[7] Bakının salındığı tarix dəqiq məlum deyildir.
"""
is_azerbaijani(input_text)
# True
```
