from arr.services import sonarr, radarr

active = []

def get():
    """Get active arr services"""
    activeservices = []
    for servicename in active:
        if servicename == 'Sonarr':
            activeservices.append(sonarr)
        elif servicename == 'Radarr':
            activeservices.append(radarr)
    return activeservices

def setup(cls, new=False):
    """Setup arr service"""
    if not new:
        # Test connection
        if hasattr(cls, 'test_connection'):
            cls.test_connection()
