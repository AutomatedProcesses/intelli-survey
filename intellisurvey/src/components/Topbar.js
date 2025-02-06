import React from "react";
import { FiSearch, FiBell } from "react-icons/fi";

const TopBar = () => {
  return (
    <header className="flex items-center justify-between p-4 bg-white shadow w-full">
      {/* Search Bar */}
      <div className="flex items-center bg-gray-100 rounded-full px-4 py-2 w-full max-w-lg">
        <FiSearch className="w-5 h-5 text-gray-400" />
        <input
          type="text"
          placeholder="Search Projects, Surveys etc."
          className="ml-3 bg-transparent focus:outline-none text-gray-600 w-full"
        />
      </div>

      {/* Right Section */}
      <div className="flex items-center space-x-6 ml-4">
        {/* Notification Icon */}
        <button className="text-gray-500 hover:text-gray-800">
          <FiBell className="w-6 h-6" />
        </button>

        {/* Product Tour */}
        <div className="text-gray-700 hidden sm:block">Product Tour</div>

        {/* Divider */}
        <div className="w-px h-6 bg-gray-300"></div>

        {/* Profile Section */}
        <div className="flex items-center space-x-2">
          <img
            src="https://via.placeholder.com/32"
            alt="Profile"
            className="w-8 h-8 rounded-full"
          />
          <span className="text-gray-700">Martina Navratilova</span>
        </div>
      </div>
    </header>
  );
};

export default TopBar;