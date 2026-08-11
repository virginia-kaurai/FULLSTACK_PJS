import { Profiler } from "react"
import Sidebar from "./Sidebar"
import {BrowserRouter , Routes, Route} from "react-router-dom"

function App() {
  

  return (

    <BrowserRouter>
    <div >
     <div>

      <Sidebar/>
     </div>

     <div className="">

      <Routes>

        <Route path="/" element={<Dashboard/>}>Dashboard</Route>
        <Route path="/students" element={<Students/>}>Students</Route>
        <Route path="/teachers" element={<Teachers/>}>Teachers</Route>
        <Route path="/classes" element={<Classes/>}>classes</Route>
        <Route path="/results" element={<Results/>}>Results</Route>
        <Route path="/attendance" element={<Attendance/>}>Attendance</Route>
        <Route path="/enrollments" element={<Enrollments/>}>Enrollments</Route>
        <Route path="/profile" element={<Profile/>}>Profile</Route>
      </Routes>
     </div>
      
    </div>

    </BrowserRouter>
  )
}

export default App

function Dashboard(){

  return(
    <h1>home components</h1>
  )
}

function Students(){

  return(
    <h1>home components</h1>
  )
}

function Teachers(){

  return(
    <h1>home components</h1>
  )
}

function Results(){

  return(
    <h1>home components</h1>
  )
}

function Enrollments(){

  return(
    <h1>home components</h1>
  )
}
function Attendance(){

  return(
    <h1>home components</h1>
  )
}




function Classes(){

  return(
    <h1>home components</h1>
  )
}

function Profile(){

  return(
    <h1>home components</h1>
  )
}