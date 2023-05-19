/* eslint-disable react/prop-types */
import { useState } from 'react';
import Proptypes from 'prop-types';

function Tache({ tache, onDeleteClick, updateTaskStatus }) {

    const [isChecked, setIsChecked] = useState(false);

    function checkHandler() {
        setIsChecked(!isChecked);
        updateTaskStatus(tache.id);
    }

    return (
        <div className="task_row">
            <input checked={isChecked} onChange={checkHandler} type="checkbox" name={tache.id} id={tache.id} />
            <label htmlFor={tache.id}> {tache.completed ? <strike>{tache.title}</strike> : tache.title} </label>
            <button onClick={() => onDeleteClick(tache.id)} style={{ marginLeft: 'auto' }}>supprimer</button>
            <button style={{ marginLeft: '10px' }}>modifier</button>
        </div>
    );
}

export function ListeTaches({ task_list, onDeleteClick, updateTaskStatus }) {
    return (
    <>
    {task_list.map(task =>
        <Tache key={task.id} tache={task} onDeleteClick={onDeleteClick} updateTaskStatus={updateTaskStatus} />
    )}
    </>
    );
}

const taskPropType = Proptypes.shape({
    id: Proptypes.string.isRequired,
    title: Proptypes.string.isRequired,
    completed: Proptypes.bool.isRequired,
});

Tache.propTypes = {
    tache: taskPropType.isRequired,
};

Tache.propTypes = {
    onDeleteClick: Proptypes.func.isRequired,
};
