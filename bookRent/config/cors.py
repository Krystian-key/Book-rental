from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    origins = [
        "http://localhost:5173",  # Twoje frontendowe URL
        "http://127.0.0.1:5173",  # Alternatywny adres localhost
        # Możesz dodać inne dozwolone źródła, jeśli to konieczne
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,              # Lista dozwolonych adresów
        allow_credentials=True,             # Pozwól na ciasteczka i nagłówki autoryzacyjne
        allow_methods=["*"],                # Pozwól na wszystkie metody HTTP (GET, POST itd.)
        allow_headers=["*"],                # Pozwól na wszystkie nagłówki
    )