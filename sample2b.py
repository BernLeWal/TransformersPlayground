#!\bin\python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/bert2bert_L-24_wmt_de_en", pad_token="<pad>", eos_token="</s>", bos_token="<s>")
model = AutoModelForSeq2SeqLM.from_pretrained("google/bert2bert_L-24_wmt_de_en")

sentence = """Beurteilungskriterien für die Abgaben:
* Korrektheit und Vollständigkeit der abgegebenen Ausarbeitungen laut Aufgabenstellung
* Code Quality
  * Finale Abgabe ist ausführbar
  * Erfüllung aller funktionalen Anforderungen
  * Erfüllung aller non-funktionalen Anforderungen
  * Edge Cases und Fehler werden richtig gehandhabt
  * Korrekte Verwendung aller Tools
  * Online-Ressourcen sind erlaubt (Kennzeichnung durch Kommentar, genaue URL)
* Dokumentation des Semesterprojekts
* Termintreue
* Eigenanteil (jedes Teammitglied muss gleich viel Leistung erbringen)"""

input_ids = tokenizer(sentence, return_tensors="pt", add_special_tokens=False).input_ids
output_ids = model.generate(input_ids)[0]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
