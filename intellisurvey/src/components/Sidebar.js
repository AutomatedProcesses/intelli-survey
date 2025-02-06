import React from "react";
import { FiInbox, FiLayers, FiBarChart2, FiDatabase, FiFileText, FiSettings, FiHelpCircle } from "react-icons/fi";

const Sidebar = () => {
  return (
    <div className="h-screen bg-black text-white w-64 p-4 flex flex-col justify-between">
      <div>
        <div className="text-lg font-bold mb-8">IntelliSurvey</div>
        {/* Adjust spacing here */}
        <div className="space-y-10"> {/* Valid Tailwind spacing class */}
          <div className="flex items-center">
            <FiInbox size={24} className="mr-6" />
            <span>Inbox</span>
          </div>
          <div className="flex items-center">
            <FiLayers size={24} className="mr-6" />
            <span>Projects & Tasks</span>
          </div>
          <div className="flex items-center text-green-500">
            <FiBarChart2 size={24} className="mr-6" />
            <span>Survey</span>
          </div>
          <div className="flex items-center">
            <FiFileText size={24} className="mr-6" />
            <span>Templates</span>
          </div>
          <div className="flex items-center">
            <FiBarChart2 size={24} className="mr-6" />
            <span>Reports</span>
          </div>
          <div className="flex items-center">
            <FiDatabase size={24} className="mr-6" />
            <span>Repository</span>
          </div>
          <div className="flex items-center">
            <FiFileText size={24} className="mr-6" />
            <span>Custom Process</span>
          </div>
        </div>
      </div>

      <div>
        <div className="space-y-10 text-sm"> {/* Adjusted spacing */}
          <div className="flex items-center">
            <FiSettings size={22} className="mr-6" />
            <span>Settings</span>
          </div>
          <div className="flex items-center">
            <FiHelpCircle size={22} className="mr-6" />
            <span>Help</span>
          </div>
          <div className="flex items-center">
            <span>Privacy Policy</span>
          </div>
        </div>
        <div className="text-xs text-gray-400 mt-8">IntelliSurvey Version 0.1</div>
      </div>
    </div>
  );
};

export default Sidebar;