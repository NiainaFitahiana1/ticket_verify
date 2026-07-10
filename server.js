const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(cors());
app.use(express.json({ limit: '50mb' }));
app.use(express.static('.'));

// Route pour sauvegarder les tickets
app.post('/api/save-tickets', (req, res) => {
  try {
    const { tickets, event, site_verification, generated_at } = req.body;
    
    if (!tickets || !Array.isArray(tickets)) {
      return res.status(400).json({ error: 'Format invalide : tickets doit être un tableau' });
    }

    const data = {
      generated_at: generated_at || new Date().toISOString(),
      event: event || 'Événement',
      site_verification: site_verification || 'https://ticket-verify.vercel.app/',
      total: tickets.length,
      tickets: tickets
    };

    const filePath = path.join(__dirname, 'data.json');
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');

    return res.json({ 
      success: true, 
      message: `✅ ${tickets.length} tickets sauvegardés dans data.json`,
      path: filePath
    });
  } catch (error) {
    console.error('Erreur lors de la sauvegarde:', error);
    return res.status(500).json({ error: error.message });
  }
});

// Route pour récupérer les tickets
app.get('/api/tickets', (req, res) => {
  try {
    const filePath = path.join(__dirname, 'data.json');
    if (fs.existsSync(filePath)) {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
      return res.json(data);
    }
    return res.json({ tickets: [], total: 0 });
  } catch (error) {
    console.error('Erreur lors de la lecture:', error);
    return res.status(500).json({ error: error.message });
  }
});

// Servir les fichiers statiques
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'creation.html'));
});

app.listen(PORT, () => {
  console.log(`🎫 Serveur Ticket Verify lancé sur http://localhost:${PORT}`);
  console.log(`📁 Fichier data.json: ${path.join(__dirname, 'data.json')}`);
});
