
import React from 'react';
import ColorPalette from './components/ColorPalette';
import ColorSuggestions from './components/ColorSuggestions';
import './App.css'; // Import the CSS file

function App() {
    return (
        <div className="App">
            <h1 className="heading">Welcome to Colorzaki!</h1>
            <div className="colorPaletteContainer">
                <ColorPalette />
            </div>
            <div className="colorSuggestionsContainer">
                <ColorSuggestions />
            </div>
            {/* You can add more components or content here */}
        </div>
    );
}

export default App;
