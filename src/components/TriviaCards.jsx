import React from 'react';
const TriviaCards = () => {
    return(
        <div className="shadow-lg rounded-lg bg-slate-800 p-6 text-center border border-green-400">
            <h2 className="text-xl font-bold text-green-500 mb-2">Question 1</h2>
            <p>Which is the largest planet in our solar system?</p>
            <ul className='rounded-lg border border-green-100 text-green-500 p-4'>
                <li>jupiter</li>
                <li>saturn</li>
                <li>neptune</li>
                <li>uranus</li>
            </ul>
        </div>
    )
}


