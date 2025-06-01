import React, { useState } from 'react';
import './App.css';

function App() {
  const [userQuery, setUserQuery] = useState('');
  const [sqlQuery, setSqlQuery] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSqlQuery('');
    setResults([]);

    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_query: userQuery })
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Error processing query');
      
      setSqlQuery(data.sql);
      setResults(data.results);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="App">
      <h1>LLM-Powered Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your query..."
          value={userQuery}
          onChange={(e) => setUserQuery(e.target.value)}
          required
        />
        <button type="submit">Submit</button>
      </form>

      {error && <p className="error">{error}</p>}
      {sqlQuery && (
        <div className="output">
          <h3>Generated SQL:</h3>
          <pre>{sqlQuery}</pre>
        </div>
      )}
      {results.length > 0 && (
        <div className="output">
        <h3>Query Results:</h3>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Gender</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {results.map((row, i) => (
              <tr key={i}>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      )}
    </div>
  );
}

export default App;
