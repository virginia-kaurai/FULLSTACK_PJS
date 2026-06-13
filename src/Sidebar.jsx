import React, { useState } from "react";
import { FaHome, FaYoutube, FaInstagram } from "react-icons/fa";
import { IoIosMenu } from "react-icons/io";
import { LiaBlogSolid, LiaQuestionSolid } from "react-icons/lia";
import { IoCloseSharp } from "react-icons/io5";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex">
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
            <li className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer">
              <FaHome size={24} />
              <span
                className={`${
                  isOpen ? "block" : "hidden"
                } md:block ml-4`}
              >
                Home
              </span>
            </li>

            <li className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer">
              <FaYoutube size={24} />
              <span
                className={`${
                  isOpen ? "block" : "hidden"
                } md:block ml-4`}
              >
                Youtube Videos
              </span>
            </li>

            <li className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer">
              <FaInstagram size={24} />
              <span
                className={`${
                  isOpen ? "block" : "hidden"
                } md:block ml-4`}
              >
                Instagram Reels
              </span>
            </li>

            <li className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer">
              <LiaBlogSolid size={24} />
              <span
                className={`${
                  isOpen ? "block" : "hidden"
                } md:block ml-4`}
              >
                Blogs
              </span>
            </li>

            <li className="flex items-center p-4 hover:bg-green-500 hover:text-slate-950 cursor-pointer">
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

      <div className="flex-1 bg-slate-950 min-h-screen">
        <header className="bg-white flex justify-between items-center p-4">
          <button
            className="lg:hidden"
            onClick={() => setIsOpen(!isOpen)}
          >
            <IoIosMenu size={24} />
          </button>

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
              Simple, interactive, and designed to make your time online
              count.
            </p>
          </div>

          <div className="bg-green-500 shadow-lg rounded-lg p-6 text-center font-semibold">
            <h2>Expense</h2>
            <p>550</p>
          </div>

          <div className="bg-green-500 shadow-lg rounded-lg border border-green-500 p-6 text-center font-semibold">
            <h2 className="text-slate-950">Profit</h2>
            <p>#</p>
          </div>

          <div className="md:col-span-2 shadow-lg rounded-lg bg-slate-950 p-6 text-center border border-green-500 font-semibold">
            <h2 className="text-green-500">Account Balance</h2>
            <p className="text-green-500">hello there</p>
          </div>

          <div className="md:col-span-2 bg-green-500 shadow-lg rounded-lg p-6 font-semibold text-center">
            <h2 className="text-black">Total Withdrawn</h2>
            <p>hello there</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;