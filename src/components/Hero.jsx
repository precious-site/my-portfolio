import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Download } from 'lucide-react';
import { downloadResume } from '../utils/generateResume';

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center pt-20 overflow-hidden">
      <div className="absolute inset-0 z-0 opacity-30 dark:opacity-20 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-[#1b1448] via-transparent to-transparent"></div>
      
      <div className="max-w-7xl mx-auto px-6 md:px-12 w-full z-10 grid md:grid-cols-2 gap-12 items-center">
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex flex-col gap-6"
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-gray-200 dark:border-white/10 w-fit text-xs font-medium tracking-wide uppercase">
            <span className="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
            Available for new opportunities
          </div>
          
          <h1 className="font-display text-5xl md:text-7xl font-medium leading-[1.1] tracking-tight text-gray-900 dark:text-white">
            Quiet Luxury.<br/>
            <span className="text-gray-400 dark:text-gray-500">Technical Excellence.</span>
          </h1>
          
          <p className="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-lg leading-relaxed font-light">
            I am Abhishek Yadav, a MERN Stack Developer engineering sophisticated, high-performance digital experiences.
          </p>
          
          <div className="flex flex-wrap items-center gap-4 mt-4">
            <a href="#work" className="inline-flex items-center justify-center gap-2 bg-gray-900 dark:bg-white text-white dark:text-gray-900 px-6 py-3 rounded-none text-sm font-medium hover:bg-primary dark:hover:bg-primary hover:text-white dark:hover:text-white transition-all duration-300">
              Explore My Work <ArrowRight size={16} />
            </a>
            <button onClick={downloadResume} className="inline-flex items-center justify-center gap-2 bg-transparent border border-gray-300 dark:border-white/20 text-gray-900 dark:text-white px-6 py-3 rounded-none text-sm font-medium hover:bg-gray-50 dark:hover:bg-white/5 transition-all duration-300">
              Download Résumé <Download size={16} />
            </button>
          </div>
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative h-[60vh] md:h-[80vh] w-full hidden md:block"
        >
          <div className="absolute inset-0 bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 overflow-hidden">
            {/* If user provides profile.jpg in public folder, it will load here. Otherwise falls back to elegant abstract. */}
            <img 
              src="/profile.jpg" 
              alt="Abhishek Yadav" 
              className="w-full h-full object-cover object-center grayscale hover:grayscale-0 transition-all duration-700"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'block';
              }}
            />
            <div className="hidden w-full h-full bg-gradient-to-tr from-[#1b1448]/20 to-transparent"></div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Hero;