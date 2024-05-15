import React from 'react';

const SortBar = ({ sortBots }) => {
  return (
    <div>
      <label>Sort By:</label>
      <select onChange={e => sortBots(e.target.value)}>
        <option value="health">Health</option>
        <option value="damage">Damage</option>
        <option value="armor">Armor</option>
      </select>
    </div>
  );
};

export default SortBar;