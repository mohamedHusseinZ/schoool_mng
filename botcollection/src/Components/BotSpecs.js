import React from 'react';

const BotSpecs = ({ bot, goBack, enlistBot }) => {
  return (
    <div>
      <h2>Bot Specs</h2>
      <img src={bot.avatar_url} alt={bot.name} />
      <p>{bot.name}</p>
      {/* Display other bot details here */}
      <button onClick={goBack}>Go Back</button>
      <button onClick={() => enlistBot(bot)}>Enlist</button>
    </div>
  );
};

export default BotSpecs;