
# Gibadolce Scalping Bot

Un bot di scalping automatico per crypto su Bybit, con notifiche su Telegram.

## Funzionalità

- Controlla il mercato ogni minuto
- Invia messaggi su Telegram quando rileva un'opportunità
- Connesso alle API live di Bybit
- Capitale minimo: $10
- Pensato per funzionare anche da mobile (tramite Telegram)

## Requisiti

- Account Bybit con API KEY e SECRET
- Bot Telegram con TOKEN e CHAT ID
- Render per l’hosting gratuito del bot

## Installazione

1. Carica i file su GitHub:
   - `bot.py`
   - `requirements.txt`
   - `README.md`

2. Crea un nuovo Web Service su [Render](https://render.com):
   - Collega il repository GitHub
   - Imposta il comando di avvio a: `python bot.py`

3. Aggiungi le seguenti variabili d’ambiente su Render:

   | Nome               | Valore                      |
   |--------------------|-----------------------------|
   | `BYBIT_API_KEY`    | La tua chiave API Bybit     |
   | `BYBIT_API_SECRET` | Il tuo secret API Bybit     |
   | `TELEGRAM_TOKEN`   | Token del bot Telegram      |
   | `TELEGRAM_CHAT_ID` | Tuo chat ID Telegram        |

4. Avvia il servizio. Riceverai i messaggi su Telegram!

---

Creato con amore e follia da Gibadolce.
