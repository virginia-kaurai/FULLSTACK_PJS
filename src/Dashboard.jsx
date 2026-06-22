
import { useState, useEffect } from 'react'
import api from './api.js'
const Dashboard = () => {

  const [profile, setProfile] = useState(null)

useEffect(() => {
  api.get('/person/')
    .then(response => {
      setProfile(response.data[0])
    })
}, [])
  return (
    <>
    <div className="flex-1 bg-slate-950 min-h-screen">
      <header className="bg-white flex justify-between items-center p-4">
        <h1 className="text-2xl font-semibold">Dashboard</h1>
        <div className="bg-gray-300 w-10 h-10 rounded-full"></div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
        <div className="md:col-span-2 bg-slate-950 shadow-lg rounded-lg border border-green-400 p-6">
          <h2 className="font-bold text-green-500 text-2xl">
            HYPERHELA AGENCIES
          </h2>

          <p className="text-xl p-6 text-green-500">
            Hyperhela Agencies is a dynamic platform where users watch
            engaging videos and answer questions to earn rewards.
          </p>
        </div>

        <div className="bg-green-500 shadow-lg rounded-lg p-6 text-center font-semibold">
          <h2>Expense</h2>
          <p>{profile ? profile.profit : 'Loading...'}</p>
        </div>

        <div className="bg-green-500 shadow-lg rounded-lg p-6 text-center font-semibold">
          <h2>Profit</h2>
          <p>{profile ? profile.profit : 'Loading...'}</p>
        </div>

        <div className="md:col-span-2 bg-slate-950 shadow-lg rounded-lg border border-green-500 p-6 text-center font-semibold">
          <h2 className="text-green-500">Account Balance</h2>
          <p className="text-green-500">
  {profile ? profile.referal_code * 300 : 'Loading...'}
</p>
        </div>

        <div className="md:col-span-2 bg-green-500 shadow-lg rounded-lg p-6 text-center font-semibold">
          <h2>Total Withdrawn</h2>
          <p>{profile ? profile.Total_withdrawn : 'Loading...'}</p>
        </div>
      </div>
    </div>

   



    <div className="bg-slate-950 p-6 rounded-lg border border-green-500">
      <h2 className="text-2xl font-bold text-green-500 mb-4">
        Weekly Timetable
      </h2>

      <table className="w-full text-center border-collapse">
        <thead>
          <tr className="bg-green-500 text-slate-950">
            <th className="p-3">Day</th>
            <th className="p-3">Activity</th>
            <th className="p-3">Quantity</th>
          </tr>
        </thead>

        <tbody className="text-green-500">
          <tr className="border-b border-green-500">
            <td className="p-3">Monday</td>
            <td className="p-3">YouTube Video</td>
            <td className="p-3">1 Video</td>
          </tr>

          <tr className="border-b border-green-500">
            <td className="p-3">Tuesday</td>
            <td className="p-3"> Blog Post</td>
            <td className="p-3">1 Blog</td>
          </tr>

          <tr className="border-b border-green-500">
            <td className="p-3">Wednesday</td>
            <td className="p-3"> Instagram Reel</td>
            <td className="p-3">1 Reel</td>
          </tr>

          <tr>
            <td className="p-3">Thursday</td>
            <td className="p-3"> Trivia Questions</td>
            <td className="p-3">5 Questions</td>
          </tr>
        </tbody>
      </table>
    </div>
    </>
  );
};





export default Dashboard;