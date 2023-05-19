/* eslint-disable react/prop-types */
import { useState } from "react";

export function Formulaire({onBtnClick}) {
    const [title, setTitle] = useState('');

    function handleBtnClick(){
        //e.preventDefault();
        onBtnClick(title);
        setTitle('');
    }

    function handleInputChange(e){
        setTitle(e.target.value);
    }

    return (
        <form>
            <input value={title} onChange={handleInputChange} type="text" />
            <input disabled={title.length == 0} onClick={handleBtnClick} type="button" value="ajouter" />
        </form>
    );
}