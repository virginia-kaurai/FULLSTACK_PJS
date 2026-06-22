const Timetable = ({setPage}) => {
  return (
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
            <td className="p-3">📺 YouTube Video</td>
            <td className="p-3">1 Video</td>
          </tr>

          <tr className="border-b border-green-500">
            <td className="p-3">Tuesday</td>
            <td className="p-3">📖 Blog Post</td>
            <td className="p-3">1 Blog</td>
          </tr>

          <tr className="border-b border-green-500">
            <td className="p-3">Wednesday</td>
            <td className="p-3">🎬 Instagram Reel</td>
            <td className="p-3">1 Reel</td>
          </tr>

          <tr>
            <td className="p-3">Thursday</td>
            <td className="p-3">❓ Trivia Questions</td>
            <td className="p-3">5 Questions</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Timetable;