import React from 'react'
import { Link } from 'react-router-dom';


function Sidebar() {
  return (
    <div className='bg-blue-400 h-full text-white'>
          <div>

            <a>

                <span>School LMS</span>
            </a>
          </div>
          <div className="">
             <ul>


                <li>  
                    <Link to='/'>Dashboard</Link></li>
                <li>
                        
                    <Link to ="/students">Students</Link>
                    </li>
                <li>
                    
                    <Link to ="/techers">Teachers</Link>
                    </li>
                <li>
                    <Link to="/classes"> Classes</Link>
                    </li>
                <li>
                    <Link to="results">Results</Link>
                    </li>
                <li>
                    <Link to="/enrollments"> Enrollments</Link>
                    </li>

                <li>
                    <Link to ="/attendance">Attendance</Link>
                    </li>
                <li>
                    <Link to="/profile"> Profile</Link>
                    </li>

             </ul>
          </div>



    </div>
  )
}

export default Sidebar