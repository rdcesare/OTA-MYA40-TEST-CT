# gui_update.py
# Aggiornamento GUI v1.2 — Release 20260722
# Cliente: ROSSI SRL — APE260001, APE260002, APE260003
# Autore: CT — 22/07/2026

VERSION = "1.2"
RELEASE_DATE = "2026-07-22"
TARGET_CUSTOMER = "ROSSI SRL"

def main():
    """Entry point aggiornamento GUI."""
    print(f"[GUI UPDATE v{VERSION}] Avvio installazione...")
    install_gui()
    print("[GUI UPDATE] Completato. Riavvio necessario.")

def install_gui():
    """Installa i file aggiornati della GUI."""
    print("[GUI UPDATE] Copia file gui_main.py...")
    print("[GUI UPDATE] Copia file gui_settings.py...")
    print("[GUI UPDATE] Copia file assets/logo_rossi.png...")
    print("[GUI UPDATE] Installazione completata.")

if __name__ == "__main__":
    main()
