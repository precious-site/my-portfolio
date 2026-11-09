import React from 'react';
import { Github, Linkedin, ArrowUp } from 'lucide-react';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="border-t border-gray-200 dark:border-white/5 bg-white dark:bg-dark-bg py-8">
      <div className="max-w-7xl mx-auto px-6 md:px-12 flex flex-col md:flex-row justify-between items-center gap-4">
        <p className="text-sm text-gray-500 dark:text-gray-400 font-light">
          &copy; {new Date().getFullYear()} Abhishek Yadav. All rights reserved.
        </p>
        
        <div className="flex items-center gap-6">
          <a href="https://github.com/Abh1sh3ky" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
            <Github size={20} />
          </a>
          <a href="https://www.linkedin.com/in/abhishek-yadav-63089b271" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
            <Linkedin size={20} />
          </a>
          <button onClick={scrollToTop} className="ml-4 p-2 bg-gray-100 dark:bg-white/5 rounded-none text-gray-500 hover:text-gray-900 dark:hover:text-white transition-colors">
            <ArrowUp size={16} />
          </button>
        </div>
      </div>
    </footer>
  );
};

export default Footer;