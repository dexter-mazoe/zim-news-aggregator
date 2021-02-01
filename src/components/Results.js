import React from 'react'
import ListItem from './ListItem'

function Results({response}) {

    return (
        <div>
            {response.map((article, index) => (
                <ListItem  key = {index}
                    title={article.title}
                    desc={article.desc}
                    link={article.link} />
            ))}
        </div>
    )
}

export default Results
