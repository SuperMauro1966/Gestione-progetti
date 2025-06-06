from core.progetto import stampa_progetto

def visualizza_struttura_progetto(id):
    stampa_progetto(id)
    stampa_figli_diretti(id)
    stampa_wbs(id)
    stampa_wp(id)
    stampa_milestone(id)
    stampa_task(id)
    stampa_risorsa(id)
