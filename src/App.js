import logo from './logo.svg';
import './App.css';
import SearchBar from './components/SearchBar';
import Results from './components/Results';
import { useState } from 'react';

function App() {

  const [response, setResponse] = useState([])

  const handleClick = params => {
    fetch('/search?' + params).then(res => res.json()).then(data => {
      setResponse(data)
    });
  }


  return (
    <div id="container">
      <SearchBar onSearch={(params) => handleClick(params)} />
      <Results response={response} />
    </div>
  );
}

export default App;
