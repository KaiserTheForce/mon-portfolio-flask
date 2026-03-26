from flask import Flask, render_template
from datetime import datetime  
app = Flask(__name__)

# --- DONNÉES STRUCTURÉES (Tirées de ton vrai CV) ---
infos_perso = {
    'prenom': 'Yassine',
    'nom': 'Dahmane',
    'titre': 'Développeur Web et Web Designer - UX/UI',
    'classe': 'BTS SIO SLAM (CFA ITIS)',
    'recherche': 'À la recherche d\'une alternance de 2 ans',
    'accroche': "Passionné par l'informatique et la cybersécurité, je souhaite intégrer une entreprise innovante pour mettre en pratique mes compétences en développement et en design.",
    'photo': 'profil.jpg', 
    'cv': 'cv_yassine_dahmane.pdf',
    'email': 'dahmaneyassine446@gmail.com',
    'telephone': '+33 7 49 48 45 95',
    'linkedin': 'https://www.linkedin.com/in/yassinedahmane/',
    
    'competences': {
        'Développement': ['HTML', 'CSS', 'JavaScript', 'Python', 'SQL', 'Java'],
        'Design & Multimédia': ['UX/UI', 'Photoshop', 'Canva', 'Figma', 'Premiere Pro', 'CapCut'],
        'Outils': ['VS Code', 'PyCharm', 'GitHub', 'DB Browser']
    },
    
    'langues': ['Français (Maternel)', 'Anglais (B2)', 'Arabe (B1)'],
    'passions': ['Cinématographie', 'Montage vidéo', 'Jeux vidéo (UX & Stratégie)'],
    
    'projets': [
        {
            'titre': 'Bento Bliss',
            'date': 'Octobre 2025',
            'description': 'Création d\'un site web vitrine responsive et moderne pour une entreprise de bento cakes. Conception du design et intégration.',
            'technos': ['HTML', 'CSS', 'JavaScript', 'UX/UI'],
            'lien': 'http://www.bentobliss.fr',
            'github': 'https://github.com/TonPseudo/BentoBliss' 
        },
        {
            'titre': 'Concours Cybersécurité & Hackathon',
            'date': 'Printemps 2025',
            'description': 'Participation à "Passe Ton Hack" (analyse réseau, hacking éthique) et "La Nuit du Code" (création d\'un projet en temps limité).',
            'technos': ['Cybersécurité', 'Logique', 'Travail d\'équipe']
        },
        {
            'titre': 'Bénévole - Tremplin Citoyen',
            'date': 'Avril - Mai 2024',
            'description': 'Animation éducative et installation/branchement de matériel informatique (PC, écrans, consoles).',
            'technos': ['Support Info', 'Pédagogie']
        }
    ]
}

# --- ROUTES PRINCIPALES ---

@app.route('/')
def accueil():
    # On récupère l'année en cours (ex: 2026) via Python
    annee_actuelle = datetime.now().year
    # On envoie l'année au template HTML avec la variable "annee"
    return render_template('index.html', moi=infos_perso, annee=annee_actuelle)

@app.route('/competences')
def competences():
    annee_actuelle = datetime.now().year
    return render_template('competences.html', moi=infos_perso, annee=annee_actuelle)

@app.route('/projets')
def projets():
    annee_actuelle = datetime.now().year
    return render_template('projets.html', moi=infos_perso, annee=annee_actuelle)

# --- BONUS ORIGINALITÉ : GESTION DES ERREURS ---
@app.errorhandler(404)
def page_non_trouvee(e):
    annee_actuelle = datetime.now().year
    return render_template('404.html', moi=infos_perso, annee=annee_actuelle), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)