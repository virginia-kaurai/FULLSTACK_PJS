import React, { useState } from "react";
import { FaHome, FaYoutube, FaInstagram } from "react-icons/fa";
import { IoIosMenu } from "react-icons/io";
import { LiaBlogSolid, LiaQuestionSolid } from "react-icons/lia";
import { IoCloseSharp } from "react-icons/io5";

const Sidebar = ({ setPage }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div
      className={`${
        isOpen ? "w-64" : "w-20"
      } md:w-64 bg-slate-950 text-green-500 min-h-screen transition-all duration-300`}
    >
      <div className="flex justify-between items-center p-4">
        <h2
          className={`${
            isOpen ? "block" : "hidden"
          } md:block text-xl font-bold`}
        >
          MyApp
        </h2>

        <button
          className="md:hidden"
          onClick={() => setIsOpen(!isOpen)}
        >
          {isOpen ? (
            <IoCloseSharp size={24} />
          ) : (
            <IoIosMenu size={24} />
          )}
        </button>
      </div>

      <nav>
        <ul>
          <li
            onClick={() => setPage("home")}
            className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer"
          >
            <FaHome size={24} />
            <span
              className={`${
                isOpen ? "block" : "hidden"
              } md:block ml-4`}
            >
              Home
            </span>
          </li>

          <li
            onClick={() => setPage("youtube")}
            className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer"
          >
            <FaYoutube size={24} />
            <span
              className={`${
                isOpen ? "block" : "hidden"
              } md:block ml-4`}
            >
              Youtube Videos
            </span>
          </li>

          <li
            onClick={() => setPage("instagram")}
            className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer"
          >
            <FaInstagram size={24} />
            <span
              className={`${
                isOpen ? "block" : "hidden"
              } md:block ml-4`}
            >
              Instagram Reels
            </span>
          </li>

          <li
            onClick={() => setPage("blogs")}
            className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer"
          >
            <LiaBlogSolid size={24} />
            <span
              className={`${
                isOpen ? "block" : "hidden"
              } md:block ml-4`}
            >
              Blogs
            </span>
          </li>

          <li
            onClick={() => setPage("trivia")}
            className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer"
          >
            <LiaQuestionSolid size={24} />
            <span
              className={`${
                isOpen ? "block" : "hidden"
              } md:block ml-4`}
            >
              Trivia
            </span>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;