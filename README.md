# 🎫 Ticket Verify - Générateur de Tickets PDF

Générateur de tickets PDF avec QR codes uniques et gestion centralisée des données.

## 🚀 Installation & Démarrage

### 1. **Installer les dépendances**
```bash
cd /home/mano/ticket-verify
npm install
```

### 2. **Démarrer le serveur**
```bash
npm start
```

Le serveur démarre sur `http://localhost:3000`

### 3. **Accéder à l'application**
- Ouvrir votre navigateur : `http://localhost:3000`
- Ou directement le fichier `creation.html`

---

## 📋 Fonctionnalités

### ✅ Onglet "Générer"
1. **Charger une image** - Importer votre template de ticket
2. **Configurer les détails** - Événement, date, lieu, prix, etc.
3. **Personnaliser** - Police, taille, couleur des numéros
4. **Optimiser** - Réduire la taille du PDF (30-95% de qualité)
5. **Générer** - Crée le PDF + sauvegarde les données

### 📊 Onglet "Données"
- **Tableau des tickets** - Visualiser tous les tickets générés
- **Recherche & filtres** - Par statut, catégorie, numéro
- **Actions** - Voir détails, marquer comme utilisé, supprimer
- **Import/Export** - Charger ou exporter en JSON

---

## 💾 Sauvegarde des Données

### Automatique (Serveur)
Après chaque génération de PDF :
- ✅ Les données sont **automatiquement sauvegardées** dans `/data.json`
- ✅ Pas besoin de cliquer sur "Exporter"
- ✅ Les données persistent sur le serveur

### Manuel (Téléchargement)
- Cliquez sur **"Exporter"** dans l'onglet Données
- Un fichier `data.json` sera téléchargé sur votre ordinateur

---

## 📁 Structure du Projet

```
ticket-verify/
├── creation.html        # Application HTML/JS
├── index.html          # Page de vérification
├── server.js           # API Backend (Node.js)
├── package.json        # Dépendances
├── data.json           # Données des tickets (créé auto)
└── README.md           # Ce fichier
```

---

## 🔧 API Endpoints

### `POST /api/save-tickets`
Sauvegarde les tickets dans `data.json`

**Payload:**
```json
{
  "generated_at": "2026-05-09T10:00:00.000Z",
  "event": "Mon Événement",
  "site_verification": "https://ticket-verify.vercel.app/",
  "tickets": [
    {
      "token": "TKT-XXXX-XXXX-XXXX",
      "numero": "0001",
      "label": "Ticket #0001",
      "qr_url": "https://...",
      "statut": "valide",
      "prix": 3000,
      ...
    }
  ]
}
```

**Réponse:**
```json
{
  "success": true,
  "message": "✅ 150 tickets sauvegardés dans data.json",
  "path": "/home/mano/ticket-verify/data.json"
}
```

### `GET /api/tickets`
Récupère les tickets stockés

---

## 📊 Optimization

### Taille du PDF

| Qualité | Taille (600 tickets) | Usage |
|---------|---------------------|-------|
| 95% | ~150 MB | Archivage qualité |
| 70% | ~60-80 MB | Standard |
| **60%** | **~40-50 MB** | ⭐ Recommandé |
| 50% | ~30-40 MB | Archive compacte |

**💡 Conseil:** Utilisez **60%** pour un bon compromis taille/qualité

---

## 🐛 Dépannage

### Le serveur n'est pas disponible?
Si le endpoint `/api/save-tickets` échoue :
- ❌ Les données ne seront PAS sauvegardées
- ✅ Fallback: Le fichier sera téléchargé en local (ancien mode)

### Les données ne se sauvegardent pas?
Vérifiez que:
1. Le serveur est bien démarré: `npm start`
2. L'URL est correcte: `http://localhost:3000`
3. Les permissions d'écriture existent: `chmod 755 /home/mano/ticket-verify`

---

## 📝 Notes

- **QR Code** : Contient uniquement l'URL + token unique
- **Données** : Stockées dans `data.json` (accès serveur)
- **Vérification** : Via `index.html` qui lit le token du QR
- **Compression** : Image JPEG + compression PDF intégrée

---

## 📞 Support

Pour toute question ou bug, consultez le code source ou les logs serveur.

---

**Développé avec ❤️ pour STK-AFI**
