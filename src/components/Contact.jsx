import React from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Github, Linkedin } from 'lucide-react';

const Contact = () => {
  return (
    <section id="contact" className="py-24 md:py-32 bg-white dark:bg-dark-bg">
      <div className="max-w-7xl mx-auto px-6 md:px-12 grid md:grid-cols-2 gap-16">
        
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
          <h2 className="text-xs font-semibold tracking-widest uppercase text-gray-400 dark:text-gray-500 mb-4">Get In Touch</h2>
          <h3 className="font-display text-4xl md:text-5xl text-gray-900 dark:text-white mb-8">Let's build the extraordinary.</h3>
          <p className="text-gray-600 dark:text-gray-400 font-light leading-relaxed mb-12 max-w-md">
            I am currently open to new opportunities and international collaborations. Whether you have a project in mind or simply want to connect, my inbox is always open.
          </p>
          
          <div className="flex flex-col gap-6">
            <a href="mailto:abhi997353@gmail.com" className="flex items-center gap-4 text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary transition-colors group">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none group-hover:border-primary transition-colors"><Mail size={18} /></span>
              <span className="font-medium">abhi997353@gmail.com</span>
            </a>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none"><Phone size={18} /></span>
              <span className="font-medium">+91 9973530779</span>
            </div>
            <div className="flex items-center gap-4 text-gray-600 dark:text-gray-300">
              <span className="p-3 border border-gray-200 dark:border-white/10 rounded-none"><MapPin size={18} /></span>
              <span className="font-medium">India</span>
            </div>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: 0.2 }} className="glass p-8 md:p-12">
          <form className="flex flex-col gap-6">
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Name</label>
              <input type="text" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors rounded-none" />
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Email</label>
              <input type="email" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors rounded-none" />
            </div>
            <div className="flex flex-col gap-2">
              <label className="text-xs uppercase tracking-wider text-gray-500">Message</label>
              <textarea rows="4" className="w-full bg-transparent border-b border-gray-300 dark:border-white/20 pb-2 text-gray-900 dark:text-white focus:outline-none focus:border-primary dark:focus:border-primary transition-colors resize-none rounded-none"></textarea>
            </div>
            <button type="button" className="mt-4 bg-gray-900 dark:bg-white text-white dark:text-gray-900 py-4 font-medium text-sm hover:bg-primary dark:hover:bg-primary hover:text-white transition-colors duration-300 w-full rounded-none">
              Send Message
            </button>
          </form>
        </motion.div>

      </div>
    </section>
  );
};

export default Contact;