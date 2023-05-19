/* eslint-disable react/prop-types */
import './App.css'
import { Navbar } from './components/Navbar';
import { Formulaire } from './components/Formulaire';
import { ListeTaches } from './components/ListeTaches';
import { useState } from 'react';
import { v4 as uuid } from 'uuid';
import Proptypes from 'prop-types';


function App() {
  const [tasks, setTask] = useState([]);

  function handleDelete(id){
    setTask(currentTask => currentTask.filter(task => task.id !== id))
  }
  //npm install uuidv4
  function addTask(title){
    setTask([...tasks, {id: uuid(), title: title, completed: false}])
  }

  function handleCheckInput(id){
    tasks.map((task) => {
      if (task.id === id){
        task.completed = !task.completed;
        return task;
      } else {
        return task;
      }
    });
  }
  
  return (
    <>
      <Navbar />
      <Formulaire onBtnClick={addTask} />
      <ListeTaches task_list={tasks} onDeleteClick={handleDelete} updateTaskStatus={handleCheckInput} />
    </>
  )
}


const taskPropType = Proptypes.shape({
  id: Proptypes.string.isRequired,
  title: Proptypes.string.isRequired,
  completed: Proptypes.bool.isRequired,
});


ListeTaches.propTypes = {
  task_list: Proptypes.arrayOf(taskPropType).isRequired,
};

App.propTypes = {
  tasks: Proptypes.arrayOf(taskPropType),
};

ListeTaches.propTypes = {
  onDeleteClick: Proptypes.func.isRequired,
};

export default App
