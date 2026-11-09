import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

files = {
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
            {/* Forced white text for the dark gradient background */}
            <h2 className="text-3xl md:text-4xl text-white font-bold">
              Scan to visit my profiles
            </h2>
            <p className="text-gray-300 mt-2">Connect with me on LinkedIn or explore my code.</p>
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
                  <h4 className="text-xl font-bold text-white tracking-wide uppercase">LinkedIn</h4>
                </div>
                <p className="text-sm text-gray-400 font-medium">Professional profile</p>
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
                  <h4 className="text-xl font-bold text-white tracking-wide uppercase">GitHub</h4>
                </div>
                <p className="text-sm text-gray-400 font-medium">Projects & code</p>
              </div>
            </div>

          </div>

          <div className="mt-8 flex items-center justify-center gap-2 text-sm text-gray-400">
            <Camera size={16} />
            <p>Tip: Scan with your phone camera</p>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default ConnectScanners;
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

        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.2 }}
          className="relative w-full flex justify-center items-center order-1 lg:order-2 mt-8 lg:mt-0"
        >
          <div className="relative w-64 h-64 md:w-[400px] md:h-[400px] animate-float">
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
    "src/components/Contact.jsx": """
import React from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Send } from 'lucide-react';

const Contact = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');
    
    // Dynamically generate standard mailto link
    const subject = encodeURIComponent(`Portfolio Inquiry from ${name}`);
    const body = encodeURIComponent(`Name: ${name}\\nEmail: ${email}\\n\\nMessage:\\n${message}`);
    
    window.location.href = `mailto:abhi997353@gmail.com?subject=${subject}&body=${body}`;
  };

  return (
    <section id="contact" className="py-24 md:py-32 bg-white dark:bg-dark-bg relative">
      <div className="max-w-7xl mx-auto px-6 md:px-12 grid md:grid-cols-2 gap-16 relative z-10">
        
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
          <h2 className="text-xs font-semibold tracking-widest uppercase text-transparent bg-clip-text bg-gradient-to-r from-neon-blue to-neon-purple mb-4">Get In Touch</h2>
          <h3 className="font-display text-4xl md:text-5xl text-gray-900 dark:text-white mb-8">Let's build the extraordinary.</h3>
          <p className="text-gray-600 dark:text-gray-400 font-light leading-relaxed mb-12 max-w-md">
            I am currently open to new opportunities and collaborations. Whether you have a project in mind or simply want to connect, my inbox is always open.
          </p>
          
          <div className="flex flex-col gap-6">
            <a href="mailto:abhi997353@gmail.com" className="flex items-center gap-4 text-gray-600 dark:text-gray-300 hover:text-neon-purple dark:hover:text-neon-purple transition-colors group">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-xl group-hover:border-neon-purple transition-colors shadow-sm"><Mail size={18} /></span>
              <span className="font-medium">abhi997353@gmail.com</span>
            </a>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-xl shadow-sm"><Phone size={18} /></span>
              <span className="font-medium">+91 9973530779</span>
            </div>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-xl shadow-sm"><MapPin size={18} /></span>
              <span className="font-medium">India</span>
            </div>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: 0.2 }} className="glass-card p-8 md:p-10 rounded-3xl">
          <form onSubmit={handleSubmit} className="flex flex-col gap-6">
            <div className="flex flex-col gap-2">
              <label htmlFor="name" className="text-xs uppercase tracking-wider text-gray-500 font-bold">Name</label>
              <input type="text" id="name" name="name" required className="w-full bg-gray-50/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 p-3 rounded-xl text-gray-900 dark:text-white focus:outline-none focus:border-neon-purple dark:focus:border-neon-purple focus:ring-1 focus:ring-neon-purple transition-all" />
            </div>
            <div className="flex flex-col gap-2">
              <label htmlFor="email" className="text-xs uppercase tracking-wider text-gray-500 font-bold">Email</label>
              <input type="email" id="email" name="email" required className="w-full bg-gray-50/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 p-3 rounded-xl text-gray-900 dark:text-white focus:outline-none focus:border-neon-purple dark:focus:border-neon-purple focus:ring-1 focus:ring-neon-purple transition-all" />
            </div>
            <div className="flex flex-col gap-2">
              <label htmlFor="message" className="text-xs uppercase tracking-wider text-gray-500 font-bold">Message</label>
              <textarea id="message" name="message" required rows="4" className="w-full bg-gray-50/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 p-3 rounded-xl text-gray-900 dark:text-white focus:outline-none focus:border-neon-purple dark:focus:border-neon-purple focus:ring-1 focus:ring-neon-purple resize-none transition-all"></textarea>
            </div>
            <button type="submit" className="mt-2 flex items-center justify-center gap-2 bg-gradient-to-r from-neon-purple to-neon-blue text-white py-4 font-bold text-sm hover:shadow-[0_0_20px_rgba(139,92,246,0.4)] transition-shadow duration-300 w-full rounded-xl">
              Send Message <Send size={16} />
            </button>
          </form>
        </motion.div>

      </div>
    </section>
  );
};

export default Contact;
"""
}

for file_path, content in files.items():
    create_file(file_path, content)
    print(f"Fixed: {file_path}")

print("\nSuccess: Text contrast, Hero title, and Functional Contact Form applied.")
