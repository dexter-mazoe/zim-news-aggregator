import React, { useState } from 'react'

export default function SearchBar({ onSearch }) {
    const [query, setQuery] = useState('')

    const handleChange = e => {
        setQuery(e.target.value);
        onSearch(`title=${query}`);
    }
    return (
        <div id="search-area">
            <p id="name">Zimbabwe News</p>
            <form id="search-form">
                <input name="query"
                    type="search" placeholder="Search by title"
                    onChange={e => handleChange(e)} />
            </form>
            <div>
                <ul class="categories">
                    <li ><a href="#" onClick={() => onSearch(`category=News`)}>News</a></li> |
                    <li ><a href="#" onClick={() => onSearch(`category=Business`)}>Business</a></li> |
                    <li ><a href="#" onClick={() => onSearch(`category=Entertainment`)}>Entertainment</a></li>|
                    <li ><a href="#" onClick={() => onSearch(`category=Sport`)}>Sport</a></li>|
                    <li ><a href="#" onClick={() => onSearch(`category=Opinion and Analysis`)}>Opinion and Analysis</a></li>|
                    <li ><a href="#" onClick={() => onSearch(`category=Africa`)}>Africa</a></li>|
                    <li ><a href="#" onClick={() => onSearch(`category=World`)}>World</a></li>
                </ul>
            </div>
        </div>
    )
}
