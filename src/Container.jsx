function Container() {

   

    
  return (
    <div className="bg-slate-950 h-screen">
      <header className="bg-white flex justify-between p-4">
        <button className="lg:hidden"><i class="fa-solid fa-bars"></i></button>
        <h1 className="text-2xl font-semibold">Dashboard</h1>
        <div className="bg-gray-300 w-10 h-10 rounded-full"></div>
      </header>

      <div className="grid grid-cols-2 gap-4 p-4">

        {/* card 1 - full width on its own */}
        <div className="col-span-2 bg-slate-950 shadow-lg rounded-lg  border border-green-400 p-6">
          <h2 className="font-bold text-green-500 text-2xl"> HYPERHELA AGENCIES</h2>
          <p className="text-xl p-6 text-green-500">   Hyperhela Agencies is a dynamic platform where users watch engaging videos<br></br> and answer questions to earn rewards. Simple, interactive, and designed to make your time online count</p>
        </div>

        {/* card 2 and 3 - side by side */}
        <div className="col-span-1 bg-green-500 shadow-lg rounded-lg p-6 text-center font-semibold" >
          <h2>Expense</h2>
          <p>550</p>
        </div>

        <div className="col-span-1 bg-green-500 shadow-lg rounded-lg border  border-green-500 p-6 text-center font-semibold">
          <h2 className="text-slate-950 ">Profit</h2>
          <p className="text-blac">#</p>
        </div>

        {/* card 4 - full width on its own */}
        <div className="col-span-2  shadow-lg rounded-lg  bg-slate-950 p-6 text-center  border border-green-500 font-semibold">
          <h2 className="text-green-500 ">Account Balance</h2>
          <p>hello there</p>
        </div>

        {/* card 5 - full width on its own */}
        <div className="col-span-2 bg-green-500 shadow-lg rounded-lg p-6 font-semibold text-center">
          <h2 className="text-black">Total Withdrawn</h2>
          <p>hello there</p>
        </div>

      </div>
    </div>
  );
}

export default Container;