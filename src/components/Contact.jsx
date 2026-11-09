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
    const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`);
    
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