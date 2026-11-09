import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
    "tailwind.config.js": """
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        dark: {
          bg: '#050511',
          surface: '#0a0a1a',
          accent: '#1b1448', 
        },
        light: {
          bg: '#f8fafc',
          surface: '#ffffff',
          accent: '#e2e8f0',
        },
        neon: {
          blue: '#3b82f6',
          purple: '#8b5cf6',
          cyan: '#06b6d4'
        }
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        display: ['"Playfair Display"', 'serif'],
      },
      animation: {
        'blob': 'blob 7s infinite',
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        blob: {
          '0%': { transform: 'translate(0px, 0px) scale(1)' },
          '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
          '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
          '100%': { transform: 'translate(0px, 0px) scale(1)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        }
      }
    },
  },
  plugins: [],
}
""",
    "src/index.css": """
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer utilities {
  .glass {
    @apply bg-white/70 dark:bg-[#0a0a1a]/70 backdrop-blur-xl border border-gray-200/50 dark:border-white/10;
  }
  .glass-card {
    @apply bg-white dark:bg-[#0a0a1a]/60 backdrop-blur-lg border border-gray-100 dark:border-white/10 shadow-lg dark:shadow-[0_8px_32px_0_rgba(31,38,135,0.37)] transition-all duration-300;
  }
  .text-glow {
    text-shadow: 0 0 20px rgba(139, 92, 246, 0.5);
  }
}

body {
  @apply bg-light-bg dark:bg-dark-bg text-gray-900 dark:text-gray-100 transition-colors duration-500 antialiased overflow-x-hidden;
}
""",
    "src/App.jsx": """
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
""",
    "src/components/Hero.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Download, Code } from 'lucide-react';
import { downloadResume } from '../utils/generateResume';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center pt-24 pb-12 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full z-10 grid lg:grid-cols-2 gap-12 lg:gap-8 items-center">
        
        <motion.div 
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6 order-2 lg:order-1"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-neon-purple/30 bg-neon-purple/5 backdrop-blur-md w-fit text-xs font-semibold tracking-wide uppercase text-neon-purple dark:text-neon-cyan shadow-[0_0_15px_rgba(139,92,246,0.15)]">
            <span className="w-2 h-2 rounded-full bg-neon-purple dark:bg-neon-cyan animate-pulse"></span>
            Available for new opportunities
          </div>
          
          <h1 className="font-display text-5xl md:text-7xl font-bold leading-[1.1] tracking-tight text-gray-900 dark:text-white">
            Abhishek <span className="text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">Kumar</span>
          </h1>
          <h2 className="text-2xl md:text-4xl font-medium text-gray-700 dark:text-gray-300">
            Full Stack Developer
          </h2>
          
          <p className="text-lg text-gray-600 dark:text-gray-400 max-w-lg leading-relaxed font-light">
            I build modern, fast, and scalable web applications that turn ideas into reality. Specializing in high-performance digital experiences.
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mt-6">
            <a href="#work" className="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-neon-purple to-neon-blue text-white px-8 py-3.5 rounded-full text-sm font-bold shadow-[0_0_20px_rgba(139,92,246,0.4)] hover:shadow-[0_0_30px_rgba(139,92,246,0.6)] hover:scale-105 transition-all duration-300">
              View My Work <ArrowRight size={18} />
            </a>
            <button onClick={downloadResume} className="inline-flex items-center justify-center gap-2 bg-white/10 dark:bg-white/5 border border-gray-200 dark:border-white/10 backdrop-blur-md text-gray-900 dark:text-white px-8 py-3.5 rounded-full text-sm font-bold hover:bg-gray-50 dark:hover:bg-white/10 transition-all duration-300">
              Download Résumé <Download size={18} />
            </button>
          </div>
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative w-full flex justify-center items-center order-1 lg:order-2 mt-8 lg:mt-0"
        >
          <div className="relative w-64 h-64 md:w-[400px] md:h-[400px] animate-float">
            {/* Outer Glowing Ring */}
            <div className="absolute inset-0 rounded-full bg-gradient-to-tr from-neon-purple via-transparent to-neon-blue opacity-50 blur-xl animate-pulse-slow"></div>
            
            {/* Image Container */}
            <div className="absolute inset-2 rounded-full p-1 bg-gradient-to-br from-white/40 to-white/5 backdrop-blur-sm z-10 border border-white/20 shadow-2xl overflow-hidden">
              <img 
                src="/profile.jpg" 
                alt="Abhishek Yadav" 
                className="w-full h-full object-cover rounded-full"
                onError={(e) => {
                  e.target.style.display = 'none';
                  e.target.nextSibling.style.display = 'flex';
                }}
              />
              <div className="hidden w-full h-full bg-[#111] flex-col items-center justify-center text-white/50 rounded-full">
                <Code size={48} className="mb-2 text-neon-purple" />
                <span className="text-xs font-mono">Image Missing</span>
              </div>
            </div>
            
            {/* Floating Tech Badges */}
            <motion.div 
              animate={{ y: [0, -15, 0] }} 
              transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              className="absolute -right-4 top-10 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(59,130,246,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-neon-blue animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">React.js</span>
            </motion.div>
            
            <motion.div 
              animate={{ y: [0, 15, 0] }} 
              transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", delay: 1 }}
              className="absolute -left-8 bottom-20 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(16,185,129,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">Node.js</span>
            </motion.div>
          </div>
        </motion.div>

      </div>
    </section>
  );
};

export default Hero;
""",
    "src/components/ConnectScanners.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import QRCode from 'react-qr-code';
import { Linkedin, Github, Camera } from 'lucide-react';

const ConnectScanners = () => {
  return (
    <section className="py-24 relative overflow-hidden">
      <div className="max-w-4xl mx-auto px-6">
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="glass-card p-8 md:p-12 rounded-[2rem] border border-white/10 relative z-10 overflow-hidden bg-gradient-to-b from-[#0a0a1a]/90 to-[#050511]/90 shadow-[0_0_50px_rgba(139,92,246,0.1)]"
        >
          {/* Background Glows within card */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-neon-purple/20 rounded-full blur-[80px] -z-10"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-neon-blue/20 rounded-full blur-[80px] -z-10"></div>

          <div className="mb-10 text-center md:text-left">
            <h3 className="text-sm font-bold tracking-widest uppercase text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple mb-2">
              Let's Connect
            </h3>
            <h2 className="text-3xl md:text-4xl text-gray-900 dark:text-white font-bold">
              Scan to visit my profiles
            </h2>
            <p className="text-gray-500 mt-2">Connect with me on LinkedIn or explore my code.</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            
            {/* LinkedIn Scanner */}
            <div className="group relative p-8 rounded-2xl bg-white/5 border border-white/10 hover:border-neon-blue/50 transition-all duration-300 flex flex-col items-center justify-center overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-b from-neon-blue/0 to-neon-blue/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              
              <div className="bg-white p-4 rounded-xl shadow-xl mb-6 transform group-hover:scale-105 transition-transform duration-300">
                <QRCode value="https://www.linkedin.com/in/abhishek-yadav-63089b271" size={160} level="H" className="w-full h-full" />
              </div>
              
              <div className="flex flex-col items-center gap-2 z-10">
                <div className="flex items-center gap-2">
                  <Linkedin className="text-neon-blue" size={24} />
                  <h4 className="text-xl font-bold text-gray-900 dark:text-white tracking-wide uppercase">LinkedIn</h4>
                </div>
                <p className="text-sm text-gray-500 font-medium">Professional profile</p>
              </div>
            </div>

            {/* GitHub Scanner */}
            <div className="group relative p-8 rounded-2xl bg-white/5 border border-white/10 hover:border-neon-purple/50 transition-all duration-300 flex flex-col items-center justify-center overflow-hidden">
              <div className="absolute inset-0 bg-gradient-to-b from-neon-purple/0 to-neon-purple/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              
              <div className="bg-white p-4 rounded-xl shadow-xl mb-6 transform group-hover:scale-105 transition-transform duration-300">
                <QRCode value="https://github.com/Abh1sh3ky" size={160} level="H" className="w-full h-full" />
              </div>
              
              <div className="flex flex-col items-center gap-2 z-10">
                <div className="flex items-center gap-2">
                  <Github className="text-neon-purple" size={24} />
                  <h4 className="text-xl font-bold text-gray-900 dark:text-white tracking-wide uppercase">GitHub</h4>
                </div>
                <p className="text-sm text-gray-500 font-medium">Projects & code</p>
              </div>
            </div>

          </div>

          <div className="mt-8 flex items-center justify-center gap-2 text-sm text-gray-500">
            <Camera size={16} />
            <p>Tip: Scan with your phone camera</p>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default ConnectScanners;
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Updated: {file_path}")

print("\nArchitecture updated with Neon Glassmorphism & Scanners.")
