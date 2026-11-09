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