import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import Projects from './components/Projects';
import Experience from './components/Experience';
import ConnectScanners from './components/ConnectScanners';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
  const [theme, setTheme] = useState('dark');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className="min-h-screen font-sans relative selection:bg-neon-purple selection:text-white">
      {/* Global Glowing Background Orbs */}
      <div className="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40vw] h-[40vw] rounded-full bg-neon-purple/20 dark:bg-neon-purple/20 blur-[120px] animate-blob"></div>
        <div className="absolute top-[20%] right-[-10%] w-[35vw] h-[35vw] rounded-full bg-neon-blue/20 dark:bg-neon-blue/20 blur-[120px] animate-blob animation-delay-2000"></div>
        <div className="absolute bottom-[-20%] left-[20%] w-[45vw] h-[45vw] rounded-full bg-neon-cyan/10 dark:bg-neon-cyan/10 blur-[120px] animate-blob animation-delay-4000"></div>
      </div>

      <Navbar theme={theme} toggleTheme={toggleTheme} />
      <main>
        <Hero />
        <About />
        <Expertise />
        <Projects />
        <Experience />
        <ConnectScanners />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;