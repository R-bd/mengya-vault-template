# A参考摘录（默认读取）

来源：`../../ai-text-detection/references/ai-text-detection-research.md` 第170–180行（第8节）和第202–233行（C节），逐字摘录，未改写。上游提交548d534，原文件SHA-256为18533618d4ca6c3776684a36bbfc4bd829f440bdebff2f040095d57c9874fffa；哈希不一致时本摘录作废，改读原文并重新摘录。

上游技能正文的三条立场，解释信号时每次适用：所有方法都只是概率信号，不能证明某一篇文本的作者身份；检测器对非母语写作者和表达简明的文本存在系统性误判；经过改写或人工编辑的文本，检测结果基本失去意义。

摘录中的研究数字和可靠性评分未经本地回查，引用前回到原始来源核实。问到具体检测器、准确率、水印或需要文献时，再读上游技能正文及原文的相应章节（3.2、3.3、6、D、F）。

---

## 8. Wichtige Einschränkung: Merkmal ≠ Beweis

Alle in dieser Recherche zusammengetragenen Verfahren — von der Wortwahl-Heuristik bis zum aufwendigsten Zero-Shot-Klassifikator — liefern **Wahrscheinlichkeitsaussagen auf Basis statistischer Muster**, keine Tatsachenfeststellung im Sinne eines Beweises. Der entscheidende Unterschied:

- *"Der Text weist Merkmale auf, die häufig bei KI-generiertem Text vorkommen"* ist eine Aussage über statistische Ähnlichkeit zu einem Trainingskorpus.
- *"Der Text wurde definitiv von einer KI geschrieben"* wäre eine Tatsachenbehauptung über die tatsächliche Entstehung des konkreten Textes — dafür reicht Stilanalyse allein grundsätzlich nicht aus, weil dieselben Muster auch bei Menschen auftreten (die ja die Trainingsdaten der Modelle geschrieben haben) und weil jede Form der Bearbeitung, Paraphrasierung oder Übersetzung die statistischen Spuren verändert oder verwischt.

Selbst die zuverlässigste heute verfügbare Methode — geschulte menschliche Einschätzung durch Vielnutzer von LLMs — erreichte im besten dokumentierten Fall eine Fehlerquote von rund einem Text unter 300, nicht null. Rechtlich ist diese Unschärfe bereits anerkannt: Nach Art. 22 DSGVO dürfen in der EU keine Sanktionen ausschließlich auf Basis eines automatisierten Detektor-Ergebnisses verhängt werden — eine menschliche Prüfung und Abwägung bleibt zwingend erforderlich.

---


## C. Praktische Checkliste: 20 Prüfpunkte für einen verdächtigen Text

**Sehr aussagekräftig** *(deutet stark auf maschinelle Erzeugung hin, aber immer noch kein Beweis)*
1. Ein von der Plattform selbst durchgeführter, positiver Wasserzeichen-Test (z. B. SynthID-Prüfung bei Google-Inhalten) — sofern der Text seit der Erstellung nicht wesentlich umformuliert wurde.
2. Ein gültiges, kryptografisch signiertes C2PA-Manifest, das den Text als KI-generiert ausweist.
3. Übereinstimmung mit einem bekannten, dokumentierten Fall aus einem Retrieval-Korpus eines Modellanbieters.
4. Mehrheitliches, unabhängiges Urteil mehrerer erfahrener LLM-Vielnutzer, die den Text unabhängig voneinander bewerten.

**Möglicherweise aussagekräftig** *(sinnvolle Hinweise, aber mit spürbarer Fehlerquote)*
5. Auffällige Häufung mehrerer typischer KI-Formulierungen gleichzeitig (nicht nur eine einzelne).
6. Durchgängig gleichmäßiger Schwierigkeitsgrad und Satzrhythmus über den gesamten Text (geringe "Burstiness").
7. Fehlen jeglicher konkreter, überprüfbarer persönlicher Details oder spezifischer Fakten.
8. Ergebnis eines seriösen, forschungsbasierten Zero-Shot-Detektors (z. B. Binoculars) bei nachweislich unbearbeitetem Text.
9. Wiederkehrende, identische rhetorische Strukturen in mehreren Absätzen desselben Textes.
10. Auffällige Widersprüche zwischen behauptetem Fachwissen und tatsächlicher inhaltlicher Tiefe.

**Schwache Indizien** *(für sich allein nicht ausreichend)*
11. Einzelne "typische" KI-Vokabeln (z. B. "maßgeblich", "vielschichtig", "unterstreichen").
12. Ergebnis eines einzelnen kommerziellen Online-Detektors ohne Zweitmeinung.
13. Betont ausgewogener, neutraler Tonfall ("einerseits … andererseits").
14. Formelhafte Einleitungen oder Schlussfolgerungen.
15. Auffällige Nutzung von Aufzählungspunkten oder Fettungen in an sich fließtext-üblichen Kontexten.
16. Rein subjektiver Bauchgefühl-Eindruck ("klingt irgendwie nach KI").

**Keine verlässlichen Beweise**
17. Kurze Textlänge unter etwa 200–300 Wörtern — hier versagen fast alle statistischen Verfahren nachweislich.
18. Texte von erkennbaren Nicht-Muttersprachlern oder in einfacher, klarer Sprache — hohes Risiko einer Fehleinstufung durch Bias-Effekte.
19. Ein einzelner, nicht bestätigter Score eines kostenlosen Online-Tools ohne Angabe der Falsch-Positiv-Rate.
20. Die bloße Tatsache, dass ein Text "zu gut" oder "zu druckreif" wirkt — das ist ebenso häufig bei sorgfältig arbeitenden Menschen der Fall.

---

