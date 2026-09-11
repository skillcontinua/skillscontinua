import requests

def get_igbo_translation(english_word):
    """Connect to mkomigbo.com for Igbo"""
    try:
        # MkomIgbo dictionary API
        url = f"https://mkomigbo.com/api/v1/translate?word={english_word}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"MkomIgbo error: {e}")
    
    # Fallback for Aba market - manual Igbo for 105 courses
    aba_dict = {
        "Solar": "Anyanwu",
        "Installation": "Ntinye",
        "Battery": "Batrị",
        "Market Women": "Umu nwanyi ahia",
        "Phone Repair": "Idozi ekwenti",
        "Computer": "Kọmputa",
    }
    return aba_dict.get(english_word, english_word)