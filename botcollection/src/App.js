import React, { useState, useEffect } from 'react';
import BotCollection from './Components/BotCollection.js';
import YourBotArmy from './Components/YourBotArmy.js';
import BotSpecs from './Components/BotSpecs';
import SortBar from './Components/SortBar';
import './App.css';

function App() {
    const [bots, setBots] = useState([]);
    const [yourBotArmy, setYourBotArmy] = useState([]);
    const [selectedBot, setSelectedBot] = useState(null);
    const [sortOption, setSortOption] = useState('health');
  
    useEffect(() => {
      // Fetch bots from the API (replace with your actual API endpoint)
      fetch('/bots')
        .then(response => response.json())
        .then(data => setBots(data));
    }, []);
  
    const enlistBot = bot => {
      // Check if the bot is already enlisted
      if (!yourBotArmy.find(b => b.id === bot.id)) {
        setYourBotArmy([...yourBotArmy, bot]);
      }
    };
  
    const releaseBot = bot => {
      setYourBotArmy(yourBotArmy.filter(b => b.id !== bot.id));
    };
  
    const dischargeBot = botId => {
      // Remove the bot from the frontend
      setYourBotArmy(yourBotArmy.filter(b => b.id !== botId));
  
      // Delete the bot from the backend
      fetch(`/bots/${botId}`, { method: 'DELETE' })
        .catch(error => console.error('Error discharging bot:', error));
    };
  
    const sortBots = option => {
      setSortOption(option);
      setBots([...bots].sort((a, b) => b[option] - a[option]));
    };
  
    const viewBotSpecs = bot => {
      setSelectedBot(bot);
    };
  
    const goBack = () => {
      setSelectedBot(null);
    };
  
    return (
      <div className="container">
        <SortBar sortBots={sortBots} />
        {selectedBot ? (
          <BotSpecs bot={selectedBot} goBack={goBack} enlistBot={enlistBot} />
        ) : (
          <>
            <BotCollection bots={bots} enlistBot={enlistBot} viewBotSpecs={viewBotSpecs} />
            <YourBotArmy army={yourBotArmy} releaseBot={releaseBot} dischargeBot={dischargeBot} />
          </>
        )}
      </div>
    );
  }
  
  export default App;