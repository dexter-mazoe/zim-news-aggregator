import React from 'react'

export default function ListItem({title, desc,link})  {
    return (
        <div className='list-item'>
            <h3><a href={link}>{title}</a></h3>
            <p>{desc}</p>
        </div>
    )
}
