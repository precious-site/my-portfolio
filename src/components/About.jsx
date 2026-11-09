import React from 'react';
import { motion } from 'framer-motion';

const About = () => {
  return (
    <section id="about" className="py-24 md:py-32 bg-white dark:bg-dark-bg">
      <div className="max-w-7xl mx-auto px-6 md:px-12">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="grid md:grid-cols-12 gap-12"
        >
          <div className="md:col-span-4">
            <h2 className="text-xs font-semibold tracking-widest uppercase text-gray-400 dark:text-gray-500 mb-4">Biography</h2>
            <h3 className="font-display text-3xl md:text-4xl text-gray-900 dark:text-white">Effortless Sophistication in Code.</h3>
          </div>
          
          <div className="md:col-span-8 flex flex-col gap-6 text-gray-600 dark:text-gray-300 text-lg leading-relaxed font-light">
            <p>
              I am Abhishek Yadav, a passionate MERN Stack Developer with an uncompromising dedication to building modern, responsive, and user-centric web applications.
            </p>
            <p>
              My expertise lies in full-stack architecture utilizing MongoDB, Express.js, React.js, and Node.js. I approach software engineering not just as writing code, but as crafting premium digital solutions that solve complex problems with elegant simplicity.
            </p>
            <p>
              Whether structuring robust backend APIs or designing intuitive frontend interfaces, my focus remains on scalability, technical excellence, and continuous growth.
            </p>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default About;