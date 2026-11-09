import React from 'react';
import { motion } from 'framer-motion';

const Experience = () => {
  return (
    <section className="py-24 md:py-32 bg-gray-50 dark:bg-[#0d0d14]">
      <div className="max-w-7xl mx-auto px-6 md:px-12 grid md:grid-cols-2 gap-16">
        
        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
          <h2 className="font-display text-2xl mb-8 text-gray-900 dark:text-white border-b border-gray-200 dark:border-white/10 pb-4">Professional Experience</h2>
          <div className="relative pl-6 border-l border-gray-200 dark:border-white/10">
            <div className="absolute w-3 h-3 bg-gray-200 dark:bg-white/20 rounded-full -left-[6.5px] top-2"></div>
            <h4 className="text-lg font-medium text-gray-900 dark:text-white">Full Stack Development Focus</h4>
            <p className="text-sm text-primary mb-3">Independent | Present</p>
            <p className="text-sm text-gray-600 dark:text-gray-400 font-light leading-relaxed">
              Actively conceptualizing, architecting, and deploying sophisticated MERN stack applications. Focus on building scalable data structures, implementing secure JWT authentication, and designing responsive, accessible user interfaces.
            </p>
          </div>
        </motion.div>

        <motion.div initial={{ opacity: 0, y: 20 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }} transition={{ delay: 0.2 }}>
          <h2 className="font-display text-2xl mb-8 text-gray-900 dark:text-white border-b border-gray-200 dark:border-white/10 pb-4">Education & Certifications</h2>
          <div className="relative pl-6 border-l border-gray-200 dark:border-white/10">
            <div className="absolute w-3 h-3 bg-gray-200 dark:bg-white/20 rounded-full -left-[6.5px] top-2"></div>
            <h4 className="text-lg font-medium text-gray-900 dark:text-white">Computer Science Fundamentals</h4>
            <p className="text-sm text-primary mb-3">India</p>
            <p className="text-sm text-gray-600 dark:text-gray-400 font-light leading-relaxed">
              Comprehensive study of algorithmic problem solving, database management systems (SQL/NoSQL), and modern software engineering principles, forming the foundation of robust web development.
            </p>
          </div>
        </motion.div>

      </div>
    </section>
  );
};

export default Experience;