import React, { useState, useEffect } from 'react'

function App() {
  
  const [data, setData] = useState([{}])
  const [body, setBody] = useState('')
  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
        data => {
          setData(data)
          // console.log(data )
        }
    )
  }, [])

  const handleShit = (event) => {
    setBody('')
  };

  return (
    <div>
        {(typeof data.members === 'undefined') ? (
          <p>Loading...</p>
        ): (
            data.members.map( (member, i) => (
                <p key={i}>{member}</p>
            ))
        )}

        <div>
          <h2>
            <button>
              Relaxing/Lighthearted
            </button>
            &nbsp;&nbsp; or &nbsp;&nbsp;
            {/* <button onClick="doStuff()">
              Serious/Intense
            </button> */}
          </h2>
        </div>
    </div>
  )
}

export default App