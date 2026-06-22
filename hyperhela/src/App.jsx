import { useState } from "react";
import Sidebar from "./Sidebar";
import Dashboard from "./Dashboard";
import TriviaCards from "./components/TriviaCards";
import Blogs from "./components/Blogs"
import Youtube from "./components/Youtube"
import Instagramreels from "./components/instagramreels";
import Timetable from "./timetable.jsx";


function App() {
  const [page, setPage] = useState("home");

  return (
    <div className="flex">
      <Sidebar setPage={setPage} />

      <div className="flex-1">
        {page === "home" && <Dashboard />}
        {page === "trivia" && <TriviaCards />}
        {page === "blogs" && <Blogs />}
        {page === "youtube" && <Youtube />}
        {page === "instagram" && <Instagramreels />}
        {page === "timetable" && <Timetable />}
      </div>
    </div>
  );
}

export default App;