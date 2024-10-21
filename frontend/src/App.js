import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [questions, setQuestions] = useState([]);
  const [selectedQuestion, setSelectedQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    // Fetch available questions when component mounts
    fetch('http://172.16.159.135:5000/questions')
      .then(response => response.json())
      .then(data => setQuestions(data.questions))
      .catch(error => setError('Failed to load questions'));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch('http://172.16.159.135:5000/evaluate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question_type: selectedQuestion,
          answer: answer
        }),
      });

      const data = await response.json();
      
      if (response.ok) {
        setResult(data);
      } else {
        setError(data.message || 'Failed to evaluate answer');
      }
    } catch (error) {
      setError('Error connecting to server');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Answer Evaluation System</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Select Question:</label>
          <select 
            value={selectedQuestion} 
            onChange={(e) => setSelectedQuestion(e.target.value)}
            required
          >
            <option value="">-- Select a question --</option>
            {questions.map((q, index) => (
              <option key={index} value={q.type}>
                {q.question}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Your Answer:</label>
          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            required
            placeholder="Type your answer here..."
            rows="6"
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Evaluating...' : 'Submit'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}
      
      {result && (
        <div className="result">
          <h2>Evaluation Results:</h2>
          <p className={result.is_original ? 'good' : 'bad'}>
            Originality: {result.is_original ? 'Original' : 'Potential plagiarism detected'}
            <br />
            <small>Similarity Score: {result.similarity_score.toFixed(2)}%</small>
          </p>
          <p>English Quality Score: {(result.english_quality * 100).toFixed(2)}%</p>
          <p>Overall Score: {(result.accuracy * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
