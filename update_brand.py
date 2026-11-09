import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
    "src/components/Navbar.jsx": """
import React, { useState, useEffect } from 'react';
import { Moon, Sun, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Navbar = ({ theme, toggleTheme }) => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'About', href: '#about' },
    { name: 'Expertise', href: '#expertise' },
    { name: 'Work', href: '#work' },
    { name: 'Contact', href: '#contact' },
  ];

  return (
    <header className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? 'glass py-4' : 'bg-transparent py-6'}`}>
      <div className="max-w-7xl mx-auto px-6 md:px-12 flex justify-between items-center">
        <a href="#" className="font-mono font-bold text-xl md:text-2xl tracking-tight text-gray-900 dark:text-white flex items-center gap-1 group">
          <span className="text-neon-blue">&lt;</span>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">AY</span>
          <span className="text-neon-purple">/&gt;</span>
        </a>
        
        <nav className="hidden md:flex items-center gap-8 text-sm font-medium">
          {navLinks.map((link) => (
            <a key={link.name} href={link.href} className="text-gray-600 dark:text-gray-300 hover:text-neon-blue dark:hover:text-neon-blue transition-colors">
              {link.name}
            </a>
          ))}
          <button onClick={toggleTheme} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-white/10 transition-colors" aria-label="Toggle Theme">
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </nav>

        <div className="md:hidden flex items-center gap-4">
          <button onClick={toggleTheme} className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-white/10 transition-colors">
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
          <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="p-2">
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="absolute top-full left-0 w-full glass border-t border-gray-200 dark:border-white/5 py-4 px-6 flex flex-col gap-4 md:hidden shadow-lg"
          >
            {navLinks.map((link) => (
              <a 
                key={link.name} 
                href={link.href} 
                onClick={() => setMobileMenuOpen(false)}
                className="text-lg font-medium text-gray-800 dark:text-gray-200"
              >
                {link.name}
              </a>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
};

export default Navbar;
""",
    "src/components/Footer.jsx": """
import React from 'react';
import { Github, Linkedin, ArrowUp } from 'lucide-react';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="border-t border-gray-200 dark:border-white/5 bg-white dark:bg-dark-bg py-8">
      <div className="max-w-7xl mx-auto px-6 md:px-12 flex flex-col md:flex-row justify-between items-center gap-4">
        <div className="flex items-center gap-4">
          <a href="#" className="font-mono font-bold text-lg tracking-tight text-gray-900 dark:text-white flex items-center gap-0.5">
            <span className="text-neon-blue">&lt;</span>
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">AY</span>
            <span className="text-neon-purple">/&gt;</span>
          </a>
          <p className="text-sm text-gray-500 dark:text-gray-400 font-light border-l border-gray-200 dark:border-white/10 pl-4">
            &copy; {new Date().getFullYear()} Abhishek Yadav. All rights reserved.
          </p>
        </div>
        
        <div className="flex items-center gap-6">
          <a href="https://github.com/Abh1sh3ky" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-neon-blue transition-colors">
            <Github size={20} />
          </a>
          <a href="https://www.linkedin.com/in/abhishek-yadav-63089b271" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-neon-purple transition-colors">
            <Linkedin size={20} />
          </a>
          <button onClick={scrollToTop} className="ml-4 p-2 bg-gray-100 dark:bg-white/5 rounded-full text-gray-500 hover:text-gray-900 dark:hover:text-white transition-colors">
            <ArrowUp size={16} />
          </button>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Updated: {file_path}")

print("\nSuccess: Brand name updated to <AY/> across navigation and footer.")
