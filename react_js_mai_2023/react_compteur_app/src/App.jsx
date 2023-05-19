import { useState } from 'react';
import './App.css';

export default function App() {
  
  const [count, setCount] = useState(0);

  function diminuer(){
    return setCount((count) => count-1);
  }

  function ajouter(){
    return setCount((count) => count+1);
  }

  return (
    <div className='compteur'>
      <button onClick={diminuer} className='diminuer'>-</button>
        <div className='nombre'>{count}</div>
      <button onClick={ajouter} className='ajouter'>+</button>
    </div>
  );
}
