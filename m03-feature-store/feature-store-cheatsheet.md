# Feature-Store-Cheatsheet

Schnellreferenz für die in Modul 3 verwendeten Begriffe und Befehle.

| Begriff/Befehl | Bedeutung |
| --- | --- |
| Entity | Schlüssel, zu dem Features gehören (hier: `person_id`) |
| Feature View | Gruppe zusammengehöriger Features für eine Entity |
| Online Store | schneller Speicher für aktuelle Feature-Werte, für Echtzeit-Anfragen |
| `feast apply` | liest `features.py`, registriert Entity und Feature View |
| `feast materialize <von> <bis>` | befüllt den Online Store mit Werten aus der Quelle für den angegebenen Zeitraum |
| `store.get_online_features(...)` | ruft aktuelle Feature-Werte für eine oder mehrere Entities ab |

## Faustregeln

- `.py`-Dateien, die selbst Features abfragen, dürfen nicht im `feature_repo/`-Ordner liegen – `feast apply` durchsucht diesen Ordner und würde abstürzen.
- `value_type` bei der `Entity` immer explizit angeben, sonst bleibt der Online Store nach `materialize` leer.
- `feast materialize` mit explizitem Zeitraum ist zuverlässiger als `feast materialize-incremental` für eine einmalige Demo.
