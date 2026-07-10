#!/bin/bash

# 🎫 Script de démarrage - Ticket Verify

echo "================================"
echo "🎫 Ticket Verify - Démarrage"
echo "================================"
echo ""

# Vérifier si node_modules existe
if [ ! -d "node_modules" ]; then
    echo "📦 Installation des dépendances..."
    npm install
    echo "✅ Dépendances installées"
    echo ""
fi

echo "🚀 Démarrage du serveur..."
echo "📍 Adresse: http://localhost:3000"
echo "📁 Fichier data.json: $(pwd)/data.json"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo "================================"
echo ""

npm start
