import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
    "src/components/Hero.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Download, Code } from 'lucide-react';
import { downloadResume } from '../utils/generateResume';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center pt-24 pb-12 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full z-10 grid md:grid-cols-2 gap-12 md:gap-8 items-center">
        
        {/* Profile Image: Top on Mobile (order-1), Right Side on Desktop (md:order-2) */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative w-full flex justify-center md:justify-end items-center order-1 md:order-2 mt-4 md:mt-0"
        >
          <div className="relative w-64 h-64 md:w-[380px] md:h-[380px] animate-float">
            <div className="absolute inset-0 rounded-full bg-gradient-to-tr from-neon-purple via-transparent to-neon-blue opacity-50 blur-xl animate-pulse-slow"></div>
            
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
            
            <motion.div 
              animate={{ y: [0, -15, 0] }} 
              transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              className="absolute -right-2 top-10 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(59,130,246,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-neon-blue animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">React.js</span>
            </motion.div>
            
            <motion.div 
              animate={{ y: [0, 15, 0] }} 
              transition={{ duration: 5, repeat: Infinity, ease: "easeInOut", delay: 1 }}
              className="absolute -left-6 bottom-16 glass-card px-4 py-2 rounded-2xl flex items-center gap-2 z-20 border border-white/20 shadow-[0_0_15px_rgba(16,185,129,0.3)]"
            >
              <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>
              <span className="text-sm font-bold text-gray-800 dark:text-white">Node.js</span>
            </motion.div>
          </div>
        </motion.div>

        {/* Text & CTA: Below Image on Mobile (order-2), Left Side on Desktop (md:order-1) */}
        <motion.div 
          initial={{ opacity: 0, x: -30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6 order-2 md:order-1"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-neon-purple/30 bg-neon-purple/5 backdrop-blur-md w-fit text-xs font-semibold tracking-wide uppercase text-neon-purple dark:text-neon-cyan shadow-[0_0_15px_rgba(139,92,246,0.15)]">
            <span className="w-2 h-2 rounded-full bg-neon-purple dark:bg-neon-cyan animate-pulse"></span>
            Available for new opportunities
          </div>
          
          <h1 className="font-display text-5xl md:text-7xl font-bold leading-[1.1] tracking-tight text-gray-900 dark:text-white">
            Abhishek <span className="text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple">Kumar</span>
          </h1>
          <h2 className="text-2xl md:text-4xl font-medium text-gray-700 dark:text-gray-300">
            MERN Stack Developer
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

      </div>
    </section>
  );
};

export default Hero;
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Updated: {file_path}")

print("\nSuccess: Mobile ordering corrected.")
