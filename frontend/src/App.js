import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const askBot = async () => {
    const res = await fetch('/api/ask_bot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query: query }),
    });
    const data = await res.json();
    setResponse(data.answer || data.error);
  };

  return (
    <div className="App">
      <h1>Ask Bot</h1>
      <p className="disclaimer">
        The knowledge of this bot extends mainly to help advise students on which professors they should engage with based on their interests.
      </p>
      <div className="query-container">
        <input
          type="text"
          placeholder="Your Query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
          className="query-box"
        />
        <button onClick={askBot} className="ask-button">Ask</button>
      </div>
      <div className="response-container">
        <p>Response:</p>
        <div className="response-box">
          <span>{response}</span>
        </div>
      </div>
    </div>
  );
}

export default App;